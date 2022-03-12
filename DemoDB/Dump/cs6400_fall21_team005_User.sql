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
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `firstname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lastname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('roland','roland','Roland','Around','owner'),('user01','pass01','Kris','Maisto','sales_person'),('user02','pass02','Dyan','Weglarz','manager'),('user03','pass03','Vi','Shields','inventory_clerk'),('user04','pass04','Pete','Butzen','sales_person'),('user05','pass05','Vi','Hoopengardner','inventory_clerk'),('user06','pass06','Sylvia','Rodenberger','sales_person'),('user07','pass07','Elke','Perez','inventory_clerk'),('user08','pass08','France','Matuszak','sales_person'),('user09','pass09','Novella','Gillian','inventory_clerk'),('user10','pass10','Paz','Sayaphon','sales_person'),('user11','pass11','Margart','Hoopengardner','inventory_clerk'),('user12','pass12','Gearldine','Discipio','service_writer'),('user13','pass13','Amber','Scheyer','service_writer'),('user14','pass14','Melissa','Shealy','inventory_clerk'),('user15','pass15','Yvonne','Poullion','service_writer'),('user16','pass16','Elvera','Funnell','inventory_clerk'),('user17','pass17','Sylvie','Lueckenbach','service_writer'),('user18','pass18','Viola','Reitler','inventory_clerk'),('user19','pass19','Delisa','Lary','sales_person'),('user20','pass20','Stephaine','Kitty','inventory_clerk'),('user21','pass21','Dyan','Lary','sales_person'),('user22','pass22','Glenn','Vocelka','sales_person'),('user23','pass23','Nan','Restrepo','sales_person'),('user24','pass24','Nobuko','Leto','manager'),('user25','pass25','Simona','Pawlowicz','inventory_clerk'),('user26','pass26','Nan','Dilliard','inventory_clerk'),('user27','pass27','Blondell','Juhas','inventory_clerk'),('user28','pass28','Youlanda','Nayar','manager'),('user29','pass29','Yvonne','Tillotson','service_writer'),('user30','pass30','Jenelle','Palaia','service_writer'),('user31','pass31','Leslie','Cloney','manager'),('user32','pass32','Glendora','Butt','sales_person'),('user33','pass33','Jacqueline','Campain','service_writer');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-01 16:53:41
