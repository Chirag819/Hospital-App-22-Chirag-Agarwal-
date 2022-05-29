-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient_medical_detail`
--

DROP TABLE IF EXISTS `patient_medical_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_medical_detail` (
  `Person_ID` int NOT NULL,
  `Doctor_ID` int NOT NULL,
  `DateOfCheckup` datetime NOT NULL DEFAULT (now()),
  `Doctor_name` varchar(20) DEFAULT NULL,
  `remark` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_medical_detail`
--

LOCK TABLES `patient_medical_detail` WRITE;
/*!40000 ALTER TABLE `patient_medical_detail` DISABLE KEYS */;
INSERT INTO `patient_medical_detail` VALUES (10001002,1004,'2021-07-25 12:20:30','Anushka Sharma','Test show Ashtma. XYZabc given. Recommeded X Inhaler.'),(10001001,1002,'2021-09-25 11:04:12','Imran Khan','Common cold.Antibiotic \'ABCD XYZ\' and parasitamol. come after 5days'),(10001002,1002,'2021-10-25 10:00:09','Imran Khan','Chest pain. x-ray.'),(10001002,1002,'2021-10-26 13:07:09','Imran Khan','Chest pain-Ashtma.'),(10001003,1001,'2021-10-30 12:19:17','Amitabh Bachchan','Leg pain. Done some test'),(10001003,1001,'2021-11-03 11:10:09','Amitabh Bachchan','All test okay. Pain due to age-vitamin D and calcium given.'),(10001002,1002,'2021-11-07 11:50:50','Imran Khan','eye and head pain. Vision 6/6. MRI'),(10001002,1002,'2021-11-09 10:50:40','Imran Khan','MRI okay. Eye strain.Can\'t give ABX due to asthma medicine XYZabc'),(10001004,1003,'2021-10-12 10:30:49','Shahrukh Khan','teeth decay. filling required.'),(10001002,1001,'2022-05-28 18:31:03','Amitabh Bachchan','Diaarhae');
/*!40000 ALTER TABLE `patient_medical_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-29  0:48:31
