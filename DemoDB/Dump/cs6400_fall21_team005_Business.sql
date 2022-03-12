-- MySQL dump 10.13  Distrib 8.0.19, for macos10.15 (x86_64)
--
-- Host: localhost    Database: cs6400_fall21_team005
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `Business`
--

DROP TABLE IF EXISTS `Business`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Business` (
  `taxID` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `customerID` int NOT NULL,
  `businessname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `primarycontactname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `primarycontacttitle` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`taxID`),
  UNIQUE KEY `customerID` (`customerID`),
  CONSTRAINT `fk_Business_customerID_Customer_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Business`
--

LOCK TABLES `Business` WRITE;
/*!40000 ALTER TABLE `Business` DISABLE KEYS */;
INSERT INTO `Business` VALUES ('07-6913915',193,'Cancity','Graciela Kippley','SalesRep R4'),('09-3973558',194,'Sonron','Pete Tjepkema','Senior Manager R1'),('09-5111889',183,'Hottechi','Annmarie Berganza','Manager M1'),('10-0374336',179,'Treequote','Peggie Sengbusch','Senior Director M9'),('13-6202155',200,'Zathunicon','Jose Birkner','Senior Director R8'),('17-6105195',175,'Inity','Lashawnda Ferrario','Senior Manager L1'),('19-3136322',187,'Bioholding','Rodolfo Adkin','Manager M4'),('24-1651361',195,'Codehow','Ilene Stem','Researcher R3'),('34-0807225',196,'Zumgoity','Clay Discipio','Director M6'),('34-1167025',173,'Faxquote','Daniel Suffield','Director M9'),('35-7670320',168,'Kinnamplus','Buddy Vanausdal','Associate Fellow M2'),('37-8167653',199,'Inity','Helaine Vonasek','Associate Director M4'),('38-5109013',189,'dambase','Venita Ennaco','Executive Manager R2'),('42-4075529',172,'Xx-holding','Benedict Mirafuentes','SalesRep R1'),('45-6711652',181,'Openlane','Martina Bartolet','Senior Manager M4'),('47-6473901',178,'Betatech','Wynell Rodenberger','Executive Manager M2'),('48-1769205',197,'Labdrill','Jina Adkin','Manager R1'),('49-7614440',190,'Scottech','Jennifer Fortino','Senior Manager L4'),('51-3984561',184,'Scotfind','Lisha Rodeigues','SalesRep R1'),('52-9011162',191,'dambase','Claribel Foller','Senior Director R9'),('56-2291887',176,'Mathtouch','Jesusita Degroot','Executive Manager R9'),('59-1521466',186,'Stanredtax','Mari Hirpara','Senior Scientist M1'),('61-1100139',182,'Inity','Mitsue Dilello','Executive Manager L3'),('64-4494473',188,'Ron-tech','Sage Farrow','Senior Manager R7'),('64-7173397',192,'Y-corporation','Corinne Theodorov','Associate Director M2'),('83-4401879',169,'Dalttechnology','Elly Aredondo','Senior Director M1'),('85-3032731',177,'Silis','Mozell Kolmetz','Associate Manager R4'),('86-6324444',180,'Kan-code','Nan Nunlee','Senior Director R8'),('87-8049695',185,'Warephase','Kanisha Slayton','Senior Manager M6'),('94-2432098',198,'Singletechno','Daniel Matuszak','Director M7'),('94-3886618',174,'Rangreen','Sherita Zagen','Manager M1'),('96-9587311',170,'Konex','Candida Hoa','Senior Director R1'),('97-1463799',171,'Faxquote','Merilyn Julia','Director M3');
/*!40000 ALTER TABLE `Business` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-01 16:53:39
