-- phpMyAdmin SQL Dump
-- version 3.5.8.1
-- http://www.phpmyadmin.net
--
-- Host: vegaasen.com.mysql:3306
-- Generation Time: Jun 21, 2017 at 04:10 PM
-- Server version: 10.1.23-MariaDB-1~xenial
-- PHP Version: 5.4.45-0+deb7u8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `vegaasen_com`
--

-- --------------------------------------------------------

--
-- Table structure for table `iot_home_temperature`
--

CREATE TABLE IF NOT EXISTS `iot_home_temperature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `location` varchar(45) DEFAULT NULL COMMENT 'The location of the registration. E.g livingroom etc',
  `ip` varchar(40) DEFAULT NULL COMMENT 'Represents the device that registered the temperature. E.g IP',
  `temperature` decimal(10,0) DEFAULT NULL,
  `humidity` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='IOT > Home > Temperature' AUTO_INCREMENT=3 ;

--
-- Dumping data for table `iot_home_temperature`
--

INSERT INTO `iot_home_temperature` (`id`, `date`, `location`, `ip`, `temperature`, `humidity`) VALUES
(1, '2017-06-21 14:28:33', 'innovation-lab', '0.0.0.0', '99', '999'),
(2, '2017-06-21 14:28:54', 'innovation-lab', '0.0.0.0', '99', '999');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
