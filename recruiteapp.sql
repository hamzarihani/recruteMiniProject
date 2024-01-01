-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 01, 2024 at 09:50 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recruiteapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `candidat`
--

CREATE TABLE `candidat` (
  `ID_candidat` int(11) NOT NULL,
  `nom_prenom` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `competence` varchar(255) NOT NULL,
  `diplome` enum('Sans_diplome','Bac','Bac+3','Bac+5') DEFAULT NULL,
  `diplomeNum` int(10) NOT NULL,
  `experience` float NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` enum('Poubelle','Pourquoi_Pas','Serieux') DEFAULT NULL,
  `salaire` int(20) NOT NULL,
  `note` enum('1','2','3','4','5') DEFAULT NULL,
  `ID_poste` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `candidat`
--

INSERT INTO `candidat` (`ID_candidat`, `nom_prenom`, `email`, `telephone`, `competence`, `diplome`, `diplomeNum`, `experience`, `location`, `status`, `salaire`, `note`, `ID_poste`) VALUES
(14, 'Ala', 'ala@gmail.com', '2555', 'nodejs,angular,typescript', 'Bac+3', 3, 0, 'Tunis', 'Pourquoi_Pas', 800, '3', 1),
(15, 'ALI', 'ali@gmail.com', '25485125', 'reactjs,react native,nodejs', 'Bac+3', 3, 0.5, 'Nabel', 'Pourquoi_Pas', 1000, '4', 1),
(18, 'med', 'med@gmail.com', '25485155', 'reactjs , frontend', 'Bac+5', 5, 2, 'Nabel', 'Pourquoi_Pas', 1300, '4', 1),
(19, 'Eva Miller', 'eva.miller@example.com', '111111111', 'python,flask,django', 'Bac+3', 3, 2, 'New York', 'Pourquoi_Pas', 1100, '3', 1),
(20, 'David White', 'david.white@example.com', '222222222', 'java,spring,hibernate', 'Bac+5', 5, 3.5, 'London', 'Serieux', 1500, '4', 1),
(21, 'Sophia Davis', 'sophia.davis@example.com', '333333333', 'reactjs,react native,nodejs', 'Bac', 2, 1, 'Paris', 'Poubelle', 600, '2', 1),
(22, 'Liam Harris', 'liam.harris@example.com', '444444444', 'angular,typescript,java', 'Bac+3', 3, 1.5, 'Berlin', 'Pourquoi_Pas', 900, '3', 1),
(23, 'Emma Martinez', 'emma.martinez@example.com', '555555555', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Tokyo', 'Serieux', 1600, '5', 1),
(24, 'Olivia Smith', 'olivia.smith@example.com', '666666666', 'php,laravel,mysql', 'Bac', 1, 0.5, 'Sydney', 'Poubelle', 500, '2', 1),
(25, 'Noah Johnson', 'noah.johnson@example.com', '777777777', 'python,django,flask', 'Bac+3', 3, 1.5, 'San Francisco', 'Pourquoi_Pas', 1300, '3', 1),
(26, 'Ava Brown', 'ava.brown@example.com', '888888888', 'java,spring,hibernate', 'Bac+5', 5, 2.5, 'Los Angeles', 'Serieux', 1500, '4', 1),
(27, 'Liam Davis', 'liam.davis@example.com', '999999999', 'reactjs,react native,nodejs', 'Bac', 1, 1.5, 'Seattle', 'Poubelle', 500, '2', 1),
(28, 'Emma White', 'emma.white@example.com', '1010101010', 'angular,typescript,java', 'Bac+3', 3, 2, 'Vancouver', 'Pourquoi_Pas', 1300, '3', 1),
(29, 'Sophia Johnson', 'sophia.johnson@example.com', '1111111111', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Toronto', 'Serieux', 1600, '5', 1),
(30, 'Oliver Martinez', 'oliver.martinez@example.com', '1212121212', 'php,laravel,mysql', 'Bac', 1, 1.5, 'Montreal', 'Poubelle', 500, '2', 1),
(31, 'Lucas Harris', 'lucas.harris@example.com', '1313131313', 'python,django,flask', 'Bac+3', 3, 1.5, 'Calgary', 'Pourquoi_Pas', 1300, '3', 1),
(32, 'Mia Brown', 'mia.brown@example.com', '1414141414', 'java,spring,hibernate', 'Bac+5', 5, 3.5, 'Ottawa', 'Serieux', 1550, '4', 1),
(33, 'Ethan Davis', 'ethan.davis@example.com', '1515151515', 'reactjs,react native,nodejs', 'Bac', 1, 0.5, 'Quebec City', 'Poubelle', 550, '2', 1),
(34, 'Ava White', 'ava.white@example.com', '1616161616', 'angular,typescript,java', 'Bac+3', 3, 2, 'Edmonton', 'Pourquoi_Pas', 1300, '3', 1),
(35, 'Mia Smith', 'mia.smith@example.com', '1717171717', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Victoria', 'Serieux', 1500, '5', 1),
(36, 'Oliver Johnson', 'oliver.johnson@example.com', '1818181818', 'php,laravel,mysql', 'Bac', 1, 1, 'Halifax', 'Poubelle', 500, '2', 1),
(37, 'Sophia Harris', 'sophia.harris@example.com', '1919191919', 'python,django,flask', 'Bac+3', 3, 1.7, 'Winnipeg', 'Pourquoi_Pas', 1400, '3', 1),
(38, 'Ethan Davis', 'ethan.davis@example.com', '2020202020', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Regina', 'Serieux', 1400, '4', 1),
(39, 'Mia White', 'mia.white@example.com', '2121212121', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Saskatoon', 'Poubelle', 500, '2', 1),
(40, 'Oliver Smith', 'oliver.smith@example.com', '2222222222', 'angular,typescript,java', 'Bac+3', 3, 1.5, 'Calgary', 'Pourquoi_Pas', 1350, '3', 1),
(41, 'Sophia Brown', 'sophia.brown@example.com', '2333333333', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Vancouver', 'Serieux', 2000, '5', 1),
(42, 'Oliver Davis', 'oliver.davis@example.com', '2444444444', 'php,laravel,mysql', 'Bac', 1, 0.5, 'Montreal', 'Poubelle', 2200, '2', 1),
(43, 'Mia Harris', 'mia.harris@example.com', '2555555555', 'python,django,flask', 'Bac+3', 3, 2, 'Ottawa', 'Pourquoi_Pas', 1900, '3', 1),
(44, 'Ethan White', 'ethan.white@example.com', '2666666666', 'java,spring,hibernate', 'Bac+5', 5, 3.5, 'Quebec City', 'Serieux', 1700, '4', 1),
(45, 'Ava Johnson', 'ava.johnson@example.com', '2777777777', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Halifax', 'Poubelle', 1800, '2', 1),
(46, 'Lucas Smith', 'lucas.smith@example.com', '2888888888', 'angular,typescript,java', 'Bac+3', 3, 2, 'Winnipeg', 'Pourquoi_Pas', 2100, '3', 1),
(47, 'Olivia Brown', 'olivia.brown@example.com', '2999999999', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Regina', 'Serieux', 1650, '5', 1),
(48, 'Elijah Martinez', 'elijah.martinez@example.com', '3000000000', 'php,laravel,mysql', 'Bac', 1, 0.5, 'Saskatoon', 'Poubelle', 2500, '2', 1),
(49, 'Ava Davis', 'ava.davis@example.com', '3111111111', 'python,django,flask', 'Bac+3', 3, 1.5, 'Calgary', 'Pourquoi_Pas', 2700, '3', 1),
(50, 'Oliver White', 'oliver.white@example.com', '3222222222', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Vancouver', 'Serieux', 2550, '4', 1),
(51, 'Emma Johnson', 'emma.johnson@example.com', '3333333333', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Montreal', 'Poubelle', 2300, '2', 1),
(52, 'Liam Harris', 'liam.harris@example.com', '3444444444', 'angular,typescript,java', 'Bac+3', 3, 2, 'Ottawa', 'Pourquoi_Pas', 2400, '3', 1),
(53, 'Sophia White', 'sophia.white@example.com', '3555555555', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Quebec City', 'Serieux', 2150, '5', 1),
(54, 'Ethan Smith', 'ethan.smith@example.com', '3666666666', 'php,laravel,mysql', 'Bac', 1, 0.5, 'Halifax', 'Poubelle', 2250, '2', 1),
(55, 'Sophie Harris', 'sophie.harris@example.com', '3777777777', 'python,flask,django', 'Bac+3', 3, 1.5, 'New York', 'Pourquoi_Pas', 2450, '3', 1),
(56, 'Sophie Harris', 'sophie.harris@example.com', '3777777777', 'python,flask,django', 'Bac+3', 3, 2, 'New York', 'Pourquoi_Pas', 2594, '3', 1),
(57, 'Lucas Brown', 'lucas.brown@example.com', '3888888888', 'java,spring,hibernate', 'Bac+5', 5, 3, 'London', 'Serieux', 2385, '4', 1),
(58, 'Eva Turner', 'eva.turner@example.com', '3999999999', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Paris', 'Poubelle', 1140, '2', 1),
(59, 'Oliver Davis', 'oliver.davis@example.com', '4000000000', 'angular,typescript,java', 'Bac+3', 3, 1.5, 'Berlin', 'Pourquoi_Pas', 2147, '3', 1),
(60, 'Sophia White', 'sophia.white@example.com', '4111111111', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Tokyo', 'Serieux', 2114, '5', 1),
(61, 'Liam Turner', 'liam.turner@example.com', '4222222222', 'php,laravel,mysql', 'Bac', 1, 1, 'Sydney', 'Poubelle', 1128, '2', 1),
(62, 'Ava Smith', 'ava.smith@example.com', '4333333333', 'python,django,flask', 'Bac+3', 3, 2, 'San Francisco', 'Pourquoi_Pas', 2902, '3', 1),
(63, 'Oliver Brown', 'oliver.brown@example.com', '4444444444', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Los Angeles', 'Serieux', 1520, '4', 1),
(64, 'Eva Davis', 'eva.davis@example.com', '4555555555', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Seattle', 'Poubelle', 2498, '2', 1),
(65, 'Liam White', 'liam.white@example.com', '4666666666', 'angular,typescript,java', 'Bac+3', 3, 1.5, 'Vancouver', 'Pourquoi_Pas', 2728, '3', 1),
(66, 'Sophie Johnson', 'sophie.johnson@example.com', '4777777777', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Toronto', 'Serieux', 946, '5', 1),
(67, 'Lucas Martinez', 'lucas.martinez@example.com', '4888888888', 'php,laravel,mysql', 'Bac', 1, 1, 'Montreal', 'Poubelle', 2350, '2', 1),
(68, 'Eva Harris', 'eva.harris@example.com', '4999999999', 'python,django,flask', 'Bac+3', 3, 2, 'Calgary', 'Pourquoi_Pas', 1510, '3', 1),
(69, 'Liam Brown', 'liam.brown@example.com', '5000000000', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Ottawa', 'Serieux', 1901, '4', 1),
(70, 'Sophie Davis', 'sophie.davis@example.com', '5111111111', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Quebec City', 'Poubelle', 1974, '2', 1),
(71, 'Lucas White', 'lucas.white@example.com', '5222222222', 'angular,typescript,java', 'Bac+3', 3, 2, 'Edmonton', 'Pourquoi_Pas', 1166, '3', 1),
(72, 'Eva Smith', 'eva.smith@example.com', '5333333333', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Victoria', 'Serieux', 1311, '5', 1),
(73, 'Liam Johnson', 'liam.johnson@example.com', '5444444444', 'php,laravel,mysql', 'Bac', 1, 1, 'Halifax', 'Poubelle', 2255, '2', 1),
(74, 'Sophia Turner', 'sophia.turner@example.com', '5555555555', 'python,django,flask', 'Bac+3', 3, 2, 'Winnipeg', 'Pourquoi_Pas', 2140, '3', 1),
(75, 'Oliver Martinez', 'oliver.martinez@example.com', '5666666666', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Regina', 'Serieux', 937, '4', 1),
(76, 'Eva White', 'eva.white@example.com', '5777777777', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Saskatoon', 'Poubelle', 1866, '2', 1),
(77, 'Liam Smith', 'liam.smith@example.com', '5888888888', 'angular,typescript,java', 'Bac+3', 3, 2, 'Calgary', 'Pourquoi_Pas', 1318, '3', 1),
(78, 'Sophie Brown', 'sophie.brown@example.com', '5999999999', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Vancouver', 'Serieux', 2392, '5', 1),
(79, 'Oliver Davis', 'oliver.davis@example.com', '6000000000', 'php,laravel,mysql', 'Bac', 1, 1, 'Montreal', 'Poubelle', 2807, '2', 1),
(80, 'Sophia Harris', 'sophia.harris@example.com', '6111111111', 'python,django,flask', 'Bac+3', 3, 2, 'Ottawa', 'Pourquoi_Pas', 1657, '3', 1),
(81, 'Lucas Turner', 'lucas.turner@example.com', '6222222222', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Quebec City', 'Serieux', 1265, '4', 1),
(82, 'Eva Johnson', 'eva.johnson@example.com', '6333333333', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Halifax', 'Poubelle', 2757, '2', 1),
(83, 'Oliver Smith', 'oliver.smith@example.com', '6444444444', 'angular,typescript,java', 'Bac+3', 3, 2, 'Winnipeg', 'Pourquoi_Pas', 2585, '3', 1),
(84, 'Sophia White', 'sophia.white@example.com', '6555555555', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Regina', 'Serieux', 1655, '5', 1),
(85, 'Liam Davis', 'liam.davis@example.com', '6666666666', 'php,laravel,mysql', 'Bac', 1, 1, 'Saskatoon', 'Poubelle', 1921, '2', 1),
(86, 'Eva Harris', 'eva.harris@example.com', '6777777777', 'python,django,flask', 'Bac+3', 3, 2, 'Calgary', 'Pourquoi_Pas', 1638, '3', 1),
(87, 'Lucas Turner', 'lucas.turner@example.com', '6888888888', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Vancouver', 'Serieux', 1631, '4', 1),
(88, 'Sophie Johnson', 'sophie.johnson@example.com', '6999999999', 'reactjs,react native,nodejs', 'Bac', 1, 1.5, 'Montreal', 'Poubelle', 2438, '2', 1),
(89, 'Oliver White', 'oliver.white@example.com', '7000000000', 'angular,typescript,java', 'Bac+3', 3, 2, 'Ottawa', 'Pourquoi_Pas', 2098, '3', 1),
(90, 'Eva Brown', 'eva.brown@example.com', '7111111111', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Quebec City', 'Serieux', 2375, '5', 1),
(91, 'Liam Smith', 'liam.smith@example.com', '7222222222', 'php,laravel,mysql', 'Bac', 1, 1, 'Halifax', 'Poubelle', 2580, '2', 1),
(92, 'Sophie Harris', 'sophie.harris@example.com', '3777777777', 'python,flask,django', 'Bac+3', 3, 2, 'New York', 'Pourquoi_Pas', 2629, '3', 1),
(93, 'Lucas Brown', 'lucas.brown@example.com', '3888888888', 'java,spring,hibernate', 'Bac+5', 5, 3, 'London', 'Serieux', 1443, '4', 1),
(94, 'Eva Turner', 'eva.turner@example.com', '3999999999', 'reactjs,react native,nodejs', 'Bac', 1, 1.5, 'Paris', 'Poubelle', 2930, '2', 1),
(95, 'Oliver Davis', 'oliver.davis@example.com', '4000000000', 'angular,typescript,java', 'Bac+3', 3, 2, 'Berlin', 'Pourquoi_Pas', 2920, '3', 1),
(96, 'Sophia White', 'sophia.white@example.com', '4111111111', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Tokyo', 'Serieux', 2807, '5', 1),
(97, 'Liam Turner', 'liam.turner@example.com', '4222222222', 'php,laravel,mysql', 'Bac', 1, 1, 'Sydney', 'Poubelle', 2276, '2', 1),
(98, 'Ava Smith', 'ava.smith@example.com', '4333333333', 'python,django,flask', 'Bac+3', 3, 2, 'San Francisco', 'Pourquoi_Pas', 2161, '3', 1),
(99, 'Oliver Brown', 'oliver.brown@example.com', '4444444444', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Los Angeles', 'Serieux', 978, '4', 1),
(100, 'Eva Davis', 'eva.davis@example.com', '4555555555', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Seattle', 'Poubelle', 2006, '2', 1),
(101, 'Liam White', 'liam.white@example.com', '4666666666', 'angular,typescript,java', 'Bac+3', 3, 2, 'Vancouver', 'Pourquoi_Pas', 1894, '3', 1),
(102, 'Sophie Johnson', 'sophie.johnson@example.com', '4777777777', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Toronto', 'Serieux', 2653, '5', 1),
(103, 'Lucas Martinez', 'lucas.martinez@example.com', '4888888888', 'php,laravel,mysql', 'Bac', 1, 1, 'Montreal', 'Poubelle', 2382, '2', 1),
(104, 'Eva Harris', 'eva.harris@example.com', '4999999999', 'python,django,flask', 'Bac+3', 3, 2, 'Calgary', 'Pourquoi_Pas', 950, '3', 1),
(105, 'Liam Brown', 'liam.brown@example.com', '5000000000', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Ottawa', 'Serieux', 1207, '4', 1),
(106, 'Sophie Davis', 'sophie.davis@example.com', '5111111111', 'reactjs,react native,nodejs', 'Bac', 1, 1.5, 'Quebec City', 'Poubelle', 2383, '2', 1),
(107, 'Lucas White', 'lucas.white@example.com', '5222222222', 'angular,typescript,java', 'Bac+3', 3, 2, 'Edmonton', 'Pourquoi_Pas', 895, '3', 1),
(108, 'Eva Smith', 'eva.smith@example.com', '5333333333', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Victoria', 'Serieux', 925, '5', 1),
(109, 'Liam Johnson', 'liam.johnson@example.com', '5444444444', 'php,laravel,mysql', 'Bac', 1, 1, 'Halifax', 'Poubelle', 1143, '2', 1),
(110, 'Sophia Turner', 'sophia.turner@example.com', '5555555555', 'python,django,flask', 'Bac+3', 3, 2, 'Winnipeg', 'Pourquoi_Pas', 2138, '3', 1),
(111, 'Oliver Martinez', 'oliver.martinez@example.com', '5666666666', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Regina', 'Serieux', 2061, '4', 1),
(112, 'Eva White', 'eva.white@example.com', '5777777777', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Saskatoon', 'Poubelle', 892, '2', 1),
(113, 'Liam Smith', 'liam.smith@example.com', '5888888888', 'angular,typescript,java', 'Bac+3', 3, 2, 'Calgary', 'Pourquoi_Pas', 1877, '3', 1),
(114, 'Sophie Brown', 'sophie.brown@example.com', '5999999999', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Vancouver', 'Serieux', 1509, '5', 1),
(115, 'Oliver Davis', 'oliver.davis@example.com', '6000000000', 'php,laravel,mysql', 'Bac', 1, 1, 'Montreal', 'Poubelle', 1114, '2', 1),
(116, 'Sophia Harris', 'sophia.harris@example.com', '6111111111', 'python,django,flask', 'Bac+3', 3, 2, 'Ottawa', 'Pourquoi_Pas', 2446, '3', 1),
(117, 'Lucas Turner', 'lucas.turner@example.com', '6222222222', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Quebec City', 'Serieux', 1486, '4', 1),
(118, 'Eva Johnson', 'eva.johnson@example.com', '6333333333', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Halifax', 'Poubelle', 1491, '2', 1),
(119, 'Oliver Smith', 'oliver.smith@example.com', '6444444444', 'angular,typescript,java', 'Bac+3', 3, 2, 'Winnipeg', 'Pourquoi_Pas', 2200, '3', 1),
(120, 'Sophia White', 'sophia.white@example.com', '6555555555', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Regina', 'Serieux', 1324, '5', 1),
(121, 'Liam Davis', 'liam.davis@example.com', '6666666666', 'php,laravel,mysql', 'Bac', 1, 1, 'Saskatoon', 'Poubelle', 1421, '2', 1),
(122, 'Eva Harris', 'eva.harris@example.com', '6777777777', 'python,django,flask', 'Bac+3', 3, 2, 'Calgary', 'Pourquoi_Pas', 2334, '3', 1),
(123, 'Lucas Turner', 'lucas.turner@example.com', '6888888888', 'java,spring,hibernate', 'Bac+5', 5, 3, 'Vancouver', 'Serieux', 2204, '4', 1),
(124, 'Sophie Johnson', 'sophie.johnson@example.com', '6999999999', 'reactjs,react native,nodejs', 'Bac', 1, 1, 'Montreal', 'Poubelle', 1019, '2', 1),
(125, 'Oliver White', 'oliver.white@example.com', '7000000000', 'angular,typescript,java', 'Bac+3', 3, 2, 'Ottawa', 'Pourquoi_Pas', 2084, '3', 1),
(126, 'Eva Brown', 'eva.brown@example.com', '7111111111', 'javascript,react,nodejs', 'Bac+5', 5, 4, 'Quebec City', 'Serieux', 2161, '5', 1),
(127, 'Liam Smith', 'liam.smith@example.com', '7222222222', 'php,laravel,mysql', 'Bac', 1, 1, 'Halifax', 'Poubelle', 1553, '2', 1);

-- --------------------------------------------------------

--
-- Table structure for table `poste`
--

CREATE TABLE `poste` (
  `ID_poste` int(11) NOT NULL,
  `titre` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `mission` varchar(255) NOT NULL,
  `competence` varchar(255) NOT NULL,
  `diplome` enum('Sans_diplome','Bac','Bac+3','Bac+5') DEFAULT NULL,
  `experience` int(11) NOT NULL,
  `salaire` int(11) NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `poste`
--

INSERT INTO `poste` (`ID_poste`, `titre`, `description`, `mission`, `competence`, `diplome`, `experience`, `salaire`, `location`) VALUES
(1, 'Offre d emploi', 'Notre societe chereche a recriter les developpeurs', 'Developpeurs full stack', 'angular , nodejs', 'Bac+3', 2, 1600, 'tunis');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candidat`
--
ALTER TABLE `candidat`
  ADD PRIMARY KEY (`ID_candidat`),
  ADD KEY `ID_poste` (`ID_poste`);

--
-- Indexes for table `poste`
--
ALTER TABLE `poste`
  ADD PRIMARY KEY (`ID_poste`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `candidat`
--
ALTER TABLE `candidat`
  MODIFY `ID_candidat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;

--
-- AUTO_INCREMENT for table `poste`
--
ALTER TABLE `poste`
  MODIFY `ID_poste` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `candidat`
--
ALTER TABLE `candidat`
  ADD CONSTRAINT `candidat_ibfk_1` FOREIGN KEY (`ID_poste`) REFERENCES `poste` (`ID_poste`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
