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
-- Table structure for table `Individual`
--

DROP TABLE IF EXISTS `Individual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Individual` (
  `driverlicensenumber` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `customerID` int NOT NULL,
  `firstname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lastname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`driverlicensenumber`),
  UNIQUE KEY `customerID` (`customerID`),
  CONSTRAINT `fk_Individual_customerID_Customer_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Individual`
--

LOCK TABLES `Individual` WRITE;
/*!40000 ALTER TABLE `Individual` DISABLE KEYS */;
INSERT INTO `Individual` VALUES ('A0301796521',108,'Tresa','Karpel'),('A0536865675',70,'Charlene','Saras'),('A0750292190',21,'Leslie','Knipp'),('A0836288701',112,'Dyan','Dallen'),('A0923389692',62,'Barrett','Sergi'),('A0943466017',164,'Sage','Schirpke'),('A0965866036',160,'Garry','Merced'),('A1100965794',76,'Sherita','Flister'),('A1148700069',64,'Xuan','Plumer'),('A1652643602',121,'Belen','Onofrio'),('A1919786459',90,'Irma','Loader'),('A2150826458',35,'Vincent','Ennaco'),('A2356695475',68,'Rozella','Bowley'),('A2549561818',92,'Alease','Vinning'),('A2781606676',113,'Margart','Koppinger'),('A3410814072',60,'Freeman','Paskin'),('A3642699140',117,'Tiffiny','Zepp'),('A3706458629',15,'Kris','Manno'),('A4114790699',141,'Alease','Lipke'),('A4195059665',105,'Irma','Hughey'),('A4307733572',27,'Selma','Hirpara'),('A5182568516',36,'Benedict','Vizarro'),('A5224016442',71,'Mitzie','Blunk'),('A5920668662',166,'Elza','Demesa'),('A6107738399',167,'Ernest','Ehmann'),('A6562833622',52,'Alisha','Springe'),('A7135730876',7,'Gary','Poullion'),('A7336665337',165,'Regenia','Paskin'),('A7394786391',162,'Daron','Limmel'),('A7476663773',93,'Regenia','Buvens'),('A7656008373',11,'Ammie','Hoa'),('A7974811992',25,'Carmela','Regusters'),('A8301013876',45,'Olive','Frerking'),('A8857026223',89,'Celeste','Hidvegi'),('A8857188903',23,'Martina','Kitty'),('A9110995031',140,'Lai','Ogg'),('A9383285395',5,'Tegan','Haufler'),('A9499931848',133,'Kirk','Lindall'),('A9501753054',156,'Stevie','Maile'),('A9824759625',63,'Pamella','Arias'),('B0490229322',95,'Maurine','Poquette'),('B0529778191',122,'Annelle','Andreason'),('B0667673329',4,'Caprice','Skulski'),('B1047114421',13,'Vi','Royster'),('B1302071867',139,'Lili','Lueckenbach'),('B1905472111',46,'Dean','Kippley'),('B2391029488',118,'Cammy','Kalafatis'),('B2456071697',77,'Brett','Sturiale'),('B2503869534',47,'Mireya','Upthegrove'),('B2831352575',87,'Meaghan','Kannady'),('B3114961337',73,'Cammy','Aquas'),('B3135098307',130,'Yuki','Rulapaugh'),('B3493541660',81,'Lili','Acey'),('B3560453812',146,'Staci','Perin'),('B3613796899',154,'Janine','Ennaco'),('B4222493197',135,'Layla','Steier'),('B4329886405',109,'Lorrine','Dickerson'),('B4430396935',120,'Gayla','Jurney'),('B4747383483',159,'Kristeen','Rodefer'),('B4901838775',145,'Twana','Timenez'),('B5240692276',1,'Gladys','Threets'),('B5647927687',84,'Elke','Varriano'),('B6287650227',148,'Nickolas','Scriven'),('B6594307920',41,'Detra','Uyetake'),('B6629932093',103,'Carmelina','Lary'),('B7250129830',78,'Luisa','Rochin'),('B7649567338',149,'Britt','Arias'),('B7932999712',56,'Eladia','Rantanen'),('B8116028762',116,'France','Gobern'),('B8118245955',99,'Kirk','Klusman'),('B8267603424',30,'Lezlie','Hidvegi'),('B8426722523',161,'Stephane','Caldarera'),('B8560719297',151,'Kayleigh','Upthegrove'),('B9153577327',26,'Shalon','Manno'),('B9479074244',59,'Myra','Royster'),('B9701873535',2,'Vilma','Giguere'),('B9986557803',150,'Jovita','Ankeny'),('C0199518923',110,'Felicidad','Rulapaugh'),('C0315829968',94,'Yoko','Nunlee'),('C0550572802',147,'Lavonda','Weglarz'),('C0659557688',69,'Yolando','Labreche'),('C0840217146',155,'Chau','Maile'),('C1301696678',138,'Haydee','Beech'),('C1874682232',85,'Frederica','Candlish'),('C2451484744',98,'Jani','Kiel'),('C2477021110',83,'Vincent','Demesa'),('C2486363271',137,'Laurel','Jeanty'),('C2527866885',18,'Glory','Luczki'),('C2530704207',3,'Harrison','Patak'),('C2665896847',104,'Alecia','Greenbush'),('C2673914348',51,'Tracey','Denooyer'),('C3623479361',67,'Britt','Restrepo'),('C4721215300',82,'Cassi','Mccullan'),('C4785358885',58,'Arlene','Birkner'),('C5232024518',158,'Kayleigh','Francescon'),('C5471875763',131,'Fausto','Dallen'),('C5564885117',33,'Lonny','Parvis'),('C5684393032',97,'Theodora','Modzelewski'),('C5820441797',86,'Loreta','Discipio'),('C6390913308',53,'Casie','Gesick'),('C6563700744',14,'Ruthann','Waycott'),('C6697208198',12,'Lorean','Mcrae'),('C6938144357',9,'Cassi','Tagala'),('C7405915994',143,'Lynelle','Cronauer'),('C7720975467',129,'Elza','Diestel'),('C7749249695',19,'Lindsey','Felger'),('C7836526302',153,'Laurel','Yum'),('C7966010586',152,'Raina','Nicka'),('C8180681803',88,'Ty','Hiatt'),('C8349669264',61,'Mattie','Reiber'),('C8363248808',106,'Kimberlie','Silvestrini'),('C8387651854',32,'Glory','Dallen'),('C8487820691',6,'Janine','Riden'),('C8521553415',142,'Cecilia','Dilello'),('C8565047824',127,'Nickolas','Wildfong'),('C9468553584',125,'Pamella','Honeywell'),('C9607630052',111,'Lizette','Oles'),('C9725877677',16,'Jess','Wieser'),('C9883149255',102,'Clay','Eroman'),('D0328630274',48,'Laurel','Mclaird'),('D0369069698',115,'Peggie','Thyberg'),('D0751253658',91,'Sheridan','Neither'),('D0979557056',34,'Donette','Hellickson'),('D0985294389',50,'Rikki','Oles'),('D1203722082',144,'Tiera','Emard'),('D1263382492',124,'Nan','Stem'),('D1938774729',22,'Herminia','Steffensmeier'),('D2205967267',20,'Abel','Weirather'),('D2440363626',40,'Chantell','Amyot'),('D2507219873',128,'Tyra','Mulqueen'),('D3341952649',54,'Rozella','Zepp'),('D3405738399',42,'Mattie','Degroot'),('D3516184517',29,'Derick','Steffensmeier'),('D3516713339',96,'Maurine','Beech'),('D3600877411',132,'Ryan','Sama'),('D3639339127',123,'Carmen','Perigo'),('D3677460785',66,'Kayleigh','Goldammer'),('D3769942713',28,'Elvera','Hoogland'),('D4268387122',119,'Ryan','Shealy'),('D4535340558',10,'Stephaine','Caudy'),('D4638312523',157,'Margart','Lipkin'),('D4681815206',114,'Kattie','Greenbush'),('D4949425401',75,'Daniela','Zagen'),('D5106706321',31,'Dierdre','Cryer'),('D5191373192',43,'Loren','Mccullan'),('D5493718870',44,'Ty','Staback'),('D5515926273',37,'Jovita','Maynerich'),('D5564091609',17,'Refugia','Schoeneck'),('D6534556524',8,'Salome','Jurney'),('D6598074250',72,'James','Lacovara'),('D6887650752',80,'Mariann','Gotter'),('D7197177558',101,'Tyra','Kitty'),('D7871290693',24,'Georgene','Perruzza'),('D8053038202',39,'Ashlyn','Kownacki'),('D8119514417',134,'Delisa','Perin'),('D8269311874',57,'Noah','Meinerding'),('D8282569200',136,'Lenna','Bubash'),('D8356291718',55,'Cecil','Riden'),('D8406096764',38,'Allene','Pagliuca'),('D8549360259',163,'Albina','Herritt'),('D8805924960',74,'Veronika','Sawchuk'),('D8992895517',65,'Helene','Miceli'),('D9622429189',126,'Gayla','Nestle'),('D9726048247',49,'Sylvie','Fallick'),('D9854901324',107,'Belen','Kitty'),('D9868570966',79,'France','Pawlowicz'),('D9983832656',100,'Eden','Calvaresi');
/*!40000 ALTER TABLE `Individual` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-01 16:53:40
