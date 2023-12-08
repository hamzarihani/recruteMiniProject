-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 08, 2023 at 08:50 PM
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
  `experience` int(11) NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` enum('Poubelle','Pourquoi_Pas','Serieux') DEFAULT NULL,
  `note` enum('1','2','3','4','5') DEFAULT NULL,
  `ID_poste` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `candidat`
--

INSERT INTO `candidat` (`ID_candidat`, `nom_prenom`, `email`, `telephone`, `competence`, `diplome`, `experience`, `location`, `status`, `note`, `ID_poste`) VALUES
(11, 'eeeeeeeee', '', '', '', 'Bac+3', 0, '', '', '', 4),
(12, 'az', '', '', '', 'Bac+3', 0, '', '', '1', 1),
(14, 'dfffff', '', '', '', 'Sans_diplome', 0, '', 'Poubelle', '1', 1),
(15, 'zaaaaaaazzzz', '', '', '', 'Sans_diplome', 0, '', 'Poubelle', '1', 1),
(16, 'nnn', '', '', '', 'Sans_diplome', 0, '', 'Poubelle', '1', 1),
(17, 'kjk', '', '', '', 'Bac+3', 0, '', 'Poubelle', '1', 4);

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
(1, 'Offre d emploi', 'Notre societe chereche a recriter les developpeurs', 'Developpeurs full stack', 'angular , nodejs', 'Bac+3', 2, 1600, 'tunis'),
(4, 'testa', '', '', '', '', 0, 1000, ''),
(6, 'zzz', '', '', '', '', 0, 0, '');

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
  MODIFY `ID_candidat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

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
