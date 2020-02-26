-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: shoeims_db
-- ------------------------------------------------------
-- Server version	5.7.25-google-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `shoeims_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `shoeims_db` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `shoeims_db`;

--
-- Table structure for table `shoes_tb`
--

DROP TABLE IF EXISTS `shoes_tb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shoes_tb` (
  `shoe_id` int(3) NOT NULL,
  `shoe_name` varchar(20) NOT NULL,
  `shoe_size` varchar(2) NOT NULL,
  `shoe_price` float NOT NULL,
  PRIMARY KEY (`shoe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_tb`
--

LOCK TABLES `shoes_tb` WRITE;
/*!40000 ALTER TABLE `shoes_tb` DISABLE KEYS */;
INSERT INTO `shoes_tb` VALUES (101,'Flight Origin 4','S',95),(102,'Flight Origin 4','M',95),(103,'Flight Origin 4','L',95),(201,'Air Max 1','S',110.5),(202,'Air Max 1','M',110.5),(203,'Air Max 1','L',110.5),(301,'One Star x GOLF','S',80),(302,'One Star x GOLF','M',80),(303,'One Star x GOLF','L',80),(401,'Air Force 1','S',300),(402,'Air Force 1','M',300),(403,'Air Force 1','L',300),(501,'Nike Lite 2','S',59.99),(502,'Nike Lite 2','M',59.99),(503,'Nike Lite 2','L',59.99),(601,'Puma Ikaz','S',30),(602,'Puma Ikaz','M',30),(603,'Puma Ikaz','L',30),(701,'Adidas Runfalcon','S',35),(702,'Adidas Runfalcon','M',35),(703,'Adidas Runfalcon','L',35),(801,'Nike Revolution 5','S',45.99),(802,'Nike Revolution 5','M',45.99),(803,'Nike Revolution 5','L',45.99),(901,'SHAQ Ceptor','S',29.99),(902,'SHAQ Ceptor','M',29.99),(903,'SHAQ Ceptor','L',29.99);
/*!40000 ALTER TABLE `shoes_tb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoesshops_tb`
--

DROP TABLE IF EXISTS `shoesshops_tb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shoesshops_tb` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `shoe_id` int(3) NOT NULL,
  `shop_id` int(3) NOT NULL,
  `shoe_name` varchar(20) NOT NULL,
  `shoe_size` varchar(2) NOT NULL,
  `stock_quantity` int(3) NOT NULL,
  `shoe_price` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shoe_id` (`shoe_id`),
  KEY `shop_id` (`shop_id`),
  CONSTRAINT `shoesshops_tb_ibfk_1` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_tb` (`shoe_id`),
  CONSTRAINT `shoesshops_tb_ibfk_2` FOREIGN KEY (`shop_id`) REFERENCES `shops_tb` (`shop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoesshops_tb`
--

LOCK TABLES `shoesshops_tb` WRITE;
/*!40000 ALTER TABLE `shoesshops_tb` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoesshops_tb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shops_tb`
--

DROP TABLE IF EXISTS `shops_tb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shops_tb` (
  `shop_id` int(3) NOT NULL,
  `shop_address` varchar(100) NOT NULL,
  `shop_city` varchar(30) NOT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shops_tb`
--

LOCK TABLES `shops_tb` WRITE;
/*!40000 ALTER TABLE `shops_tb` DISABLE KEYS */;
INSERT INTO `shops_tb` VALUES (1,'64 Shoes Lane','Manchester'),(2,'7 Laces Road','Manchester'),(3,'45 Aglet Avenue','Manchester'),(4,'73 Sole Street','York'),(5,'4 Pair Place','York');
/*!40000 ALTER TABLE `shops_tb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-26 14:29:40
