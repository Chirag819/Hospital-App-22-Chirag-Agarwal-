from flask import Flask, render_template, Response, url_for , redirect, request
import cv2
import os
from datetime import datetime
import face_recognition as fr
import numpy as np
from flask_mysqldb import MySQL
# import pymysql as MySQLdb

# tolerance of face recognition - lesser it is more stricter is the face recognition
tolerance=0.54
# webcam camera_number=0, if using other connected camera than change the below value
camera_number=0

# camera = cv2.VideoCapture(camera_number)

app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'zxcasdqwe'
app.config['MYSQL_DB'] = 'test'
 
mysql=MySQL(app)


# Marking attendance function
def mark_attendance_function(code):
    with open('Attendance.csv','r+') as f:
        my_data = f.readlines()
        cur=mysql.connection.cursor()
        cur.execute("USE test")
        cur.execute(f'SELECT Name FROM staff WHERE Person_ID = {code}')
        data=cur.fetchall()
        staff_name=(data[0][0])
        namelist = []
        now = datetime.now()
        dts = now.strftime('%H:%M:%S')
        d4 = datetime.today().strftime('%d-%m-%Y')
        for line in my_data:
            entry = line.split(',')
            da = entry[2]
            if da == d4:
                    namelist.append(entry[0])
        if staff_name not in namelist:
            f.writelines(f'\n{staff_name},{dts},{d4}')

        return(True)

# Dictonary to recognise if person is patient,doctor or staff
Recognition={
    "PA":"Patient",
    "D":"Doctor",
    "ST":"Staff"
}

# function give image encodings
def ecode_img(imges):
    encode_img_list=[]
    for img in imges:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=fr.face_encodings(img)[0]
        encode_img_list.append(encode)
    return encode_img_list

# saving images and person code from image. 
path="static/imag"
image=[]
image_path=[]
designation=[]
person_code=[]
mylist=os.listdir(path)
for a in mylist:
    img=cv2.imread(f'{path}/{a}')
    image_path.append(f'{path}/{a}')
    image.append(img)
    x=(os.path.splitext(a)[0]).split()
    object=x[0]
    person_code.append(x[1])
    designation.append(x[0])

securityguard=[]
path2="Security guard"
security=os.listdir(path2)
for guard in security:
    img=cv2.imread(f'{path2}/{guard}')
    securityguard.append(img)
    

encodelistknown=ecode_img(image)
encoding_security_guard=ecode_img(securityguard)


def gen_frames():  
    camera = cv2.VideoCapture(camera_number)
    while True:
        success, frame = camera.read()  # read the camera frame
        to_return=[]
        if not success:
            break
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faceCurFrame=fr.face_locations(frame)
            encode = fr.face_encodings(frame,faceCurFrame)
            if len(faceCurFrame) ==1:
                for encodeface,loc in zip(encode,faceCurFrame):
                    matches=fr.compare_faces(encodelistknown,encodeface,tolerance)
                    facedist=fr.face_distance(encodelistknown,encodeface)
                    matchindex=np.argmin(facedist)

                    if matches[matchindex]:
                        
                        code=person_code[matchindex]
                        recognition = Recognition[designation[matchindex]]
                        person_image=image_path[matchindex]
                        to_return.append(code)
                        to_return.append(recognition)
                        to_return.append(person_image)
                        to_return.append(matchindex)

                        return (to_return)


def mark_attendance(index):  
    while True:
        camera = cv2.VideoCapture(camera_number)
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faceCurFrame=fr.face_locations(frame)
            encode = fr.face_encodings(frame,faceCurFrame)
            staff_encode=encodelistknown[index]
            is_guard_present=False
            is_staff_present=False
            if len(faceCurFrame) ==2:
                for encodeface,loc in zip(encode,faceCurFrame):
                    matches=fr.compare_faces(encoding_security_guard,encodeface,tolerance)     #list of t/f 
                    is_staff=fr.compare_faces([staff_encode],encodeface,tolerance)
                    for value in matches:
                        is_guard_present=is_guard_present or value
                    
                    is_staff_present=is_staff_present or is_staff[0]
                
                if is_guard_present and is_staff_present:
                    return(mark_attendance_function(person_code[index]))


@app.route('/')
def index():
    return render_template('Index2.html')

@app.route('/login')
def login():
    person=gen_frames()
    Person_ID=person[0]
    who=person[1]
    img_address=f'/{person[2]}'
    detail=[]
    detail.append(Person_ID)
    detail.append(img_address)
    index=person[3]
    if who=="Patient":
        return redirect(url_for('patient',person_index=index))
    if who=="Doctor":
        return redirect(url_for('doctor',person_index=index))
    else:
        return redirect(url_for('staff',person_index=index))
    
@app.route('/patient/<int:person_index>')
def patient(person_index):
    cur=mysql.connection.cursor()
    person=person_code[person_index]
    image=f'/{image_path[person_index]}'
    cur.execute("USE test")
    cur.execute(f'SELECT * FROM patient WHERE Person_ID = {person}')
    field_names = [i[0] for i in cur.description]
    data=cur.fetchall()
    cur.execute(f'SELECT * FROM patient_medical_detail WHERE Person_ID = {person} ORDER bY DateOfCheckup DESC')
    patient_data=cur.fetchall()
    cur.close()
    return render_template('Patient detail.html', patient_data=patient_data , field=field_names,data=data,image=image)


@app.route('/doctor/<int:person_index>')
def doctor(person_index):
    cur=mysql.connection.cursor()
    person=person_code[person_index]
    image=f'/{image_path[person_index]}'
    cur.execute("USE test")
    cur.execute(f'SELECT * FROM doctor WHERE Person_ID = {person}')
    field_names = [i[0] for i in cur.description]
    data=cur.fetchall()
    cur.close()
    return render_template('Doctor.html' , field=field_names,data=data,image=image)

@app.route('/staff/<int:person_index>')
def staff(person_index):
    cur=mysql.connection.cursor()
    person=person_code[person_index]
    image=f'/{image_path[person_index]}'
    cur.execute("USE test")
    cur.execute(f'SELECT * FROM staff WHERE Person_ID = {person}')
    field_names = [i[0] for i in cur.description]
    data=cur.fetchall()
    cur.close()
    return render_template('staff.html' , field=field_names,data=data,image=image, index=person_index)

@app.route('/attendance/<int:index>')
def attendance(index):
    if mark_attendance(index):
        return render_template('Staff2.html')

@app.route('/scanpatient')
def scanpatient():
    patient=gen_frames()
    Person_ID=patient[0]
    who=patient[1]
    img_address=f'/{patient[2]}'
    detail=[]
    detail.append(Person_ID)
    detail.append(img_address)
    index=patient[3]
    if who=="Patient":
        return redirect(url_for('Patient_doctor',person_index=index))

@app.route('/Patient_doctor/<int:person_index>')
def Patient_doctor(person_index):
    cur=mysql.connection.cursor()
    person=person_code[person_index]
    image=f'/{image_path[person_index]}'
    cur.execute("USE test")
    cur.execute(f'SELECT * FROM patient WHERE Person_ID = {person}')
    field_names = [i[0] for i in cur.description]
    data=cur.fetchall()
    cur.execute(f'SELECT * FROM patient_medical_detail WHERE Person_ID = {person} ORDER bY DateOfCheckup DESC')
    patient_data=cur.fetchall()
    cur.close()
    return render_template('Patient_doctor.html', patient_data=patient_data , field=field_names,data=data,image=image)

@app.route('/updatepatient/<int:patient_index>',methods=('GET', 'POST'))
def update_patient(patient_index):
    if request.method=='POST':
        Doctor_ID=int(request.form['Doctor_ID'])
        remark=request.form['Details']
        person=int(patient_index)
        cur=mysql.connection.cursor()
        cur.execute("USE test")
        cur.execute(f'SELECT Name FROM doctor WHERE Person_ID = {Doctor_ID}')
        doctor=cur.fetchall()
        doctor_name=(doctor[0][0])
        cur.execute(f'''INSERT INTO patient_medical_detail ( Person_ID, Doctor_ID, DateOfCheckup, Doctor_name, remark)
        VALUES ( {person} , {Doctor_ID} , DEFAULT , '{doctor_name}' , '{remark}' ) ''')
        mysql.connection.commit()
        index=0
        count=0
        for i in person_code:
            if int(i)==person:
                index=count
                break
            else:
                count=count+1
        return redirect(url_for('Patient_doctor',person_index=index))

    return render_template('Update Patient.html',id=patient_index)

@app.route('/new_user',methods=('GET', 'POST'))
def new_user():
    if request.method=='POST':
        Name=request.form['name']
        Phone=request.form['phone']
        Email=request.form['email']
        Message=request.form['message']
        cur=mysql.connection.cursor()
        cur.execute("USE test")
        cur.execute(f'''INSERT INTO new_user_data
        VALUES ( '{Name}' , '{Phone}' , '{Email}', '{Message}' ) ''')
        mysql.connection.commit()
        return redirect(url_for('index'))

    return render_template('New user.html')


if __name__=='__main__':
    app.run(debug=False)
