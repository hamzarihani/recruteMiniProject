-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 23, 2023 at 08:07 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


--
-- Database: `recrutement`
--

-- --------------------------------------------------------

--
-- Table structure for table `poste`
--

CREATE TABLE `poste` (
  `ID_poste` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `titre` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `mission` varchar(255) NOT NULL,
  `competence` varchar(255) NOT NULL,
  `diplome` ENUM('Sans_diplome', 'Bac', 'Bac+3' , 'Bac+5'),
  `experience` INT NOT NULL,
  `salaire` INT NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------
--
-- Table structure for table `candidat`
--

CREATE TABLE `candidat` (
  `ID_candidat` INT NOT NULL AUTO_INCREMENT,
  `nom_prenom` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `competence` varchar(255) NOT NULL,
  `diplome` ENUM('Sans_diplome', 'Bac', 'Bac+3' , 'Bac+5'),
  `experience` INT NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` ENUM('Poubelle', 'Pourquoi_Pas', 'Serieux'),
  `note` ENUM('1', '2', '3', '4', '5'),
  `ID_poste` INT,
  PRIMARY KEY (`ID_candidat`),
  FOREIGN KEY (`ID_poste`) REFERENCES `poste`(`ID_poste`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- Dumping data for table `poste`
--

-- INSERT INTO `poste` (`titre`, `description`, `mission`, `competence` , `diplome` , `experience` , `salaire` , `location` ) VALUES
-- (`Offre d emploi `, `Notre societe chereche a recriter les developpeurs`, `Developpeurs full stack` , `angular , nodejs` , `Bac+3` , 2 , 1600, `tunis` );


-- INSERT INTO `poste` (`titre`, `description`, `mission`, `competence` , `diplome` , `experience` , `salaire` , `location` ) VALUES
-- (`Offre d emploi `, `Notre societe chereche a recriter les developpeurs`, `Developpeurs full stack` , `angular , nodejs` , `Bac+3` , 2 , 1600, `tunis` );


INSERT INTO `poste` (`titre`, `description`, `mission`, `competence`, `diplome`, `experience`, `salaire`, `location`) VALUES
('Offre d emploi', 'Notre societe chereche a recriter les developpeurs', 'Developpeurs full stack', 'angular , nodejs', 'Bac+3', 2, 1600, 'tunis');
