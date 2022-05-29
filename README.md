# MicrosoftEngage-22-Chirag-Agarwal-
Face Recognition - Website for Hospital and their members

##Requirements/Step##
Install MySQL installer community version
Keep the passward as- zxcasdqwe and everything as default\
Then in MySQL  workbench dashboard copy and paste text from 'Mysql workbench.txt' file that is in my Github repo. Then execute the command \

##Other requirement##\
-Visual studio for C++ and C# with cmake library\
-python 3.10\
-pip3

Then install library in  requirements.txt by writing in command line\
pip3 install -r requirements.txt\
After that run app.py and click on the server in output to reach the website

##App working##\
When new user need to be added ,he/she has to get registered in corresponding database and his/her photo had to be stored in /static/image and name it as {Designation} {Person_ID}\
Designation=PA for Patient, ST for staff, D for doctor.\
Example- D 1001.\
After that you are all setApp working

What website does\
The website take your face and if you are existing user take you to patient/staff/doctor page accordingly.\
The website mainly focus on doctor.When going to doctor patient take a large amount of files(medical history), and patient can sometime leave important file or some file may 
be misplaced which may be important for doctor for further medication. And it take atleast sometime for doctor to understand the large chunk of file like report that have been
 previously understood by another doctor. The main feature of the website is that it scans the patient and tell doctor, the medical history saved in the database by every doctor he visited in the past written by the doctor himself. After analysis, the doctor update the patient record. He shall write in brief about analysis./
For patient it take you to page that show patient detail. For staff it show them their detail and they can mark their attendance which is stored in CSV file for convenience.\

Future Plans\
-Make a system such When updating, doctor speak and details fills by what he speak\
-Make database online\
**I thought of deploying website but can't do due to bugs. I didn't get how to get MySql database to cloud so i have to tell you to manually copy paste data. Sorry for that.**
