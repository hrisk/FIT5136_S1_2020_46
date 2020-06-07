-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2020 at 12:55 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mission_to_mars`
--

-- --------------------------------------------------------

--
-- Table structure for table `candidate`
--

CREATE TABLE `candidate` (
  `candidate_id` int(11) NOT NULL,
  `candidate_dob` datetime NOT NULL,
  `candidate_phone` varchar(20) NOT NULL,
  `candidate_identification_type` varchar(10) NOT NULL,
  `candidate_gender` varchar(10) NOT NULL,
  `candidate_allergies` varchar(20) NOT NULL,
  `candidate_food_preference` varchar(20) NOT NULL,
  `candidate_qualification` varchar(20) DEFAULT NULL,
  `candidate_experience` varchar(20) DEFAULT NULL,
  `candidate_occupation` varchar(50) DEFAULT NULL,
  `candidate_computer_skills` varchar(30) NOT NULL,
  `candidate_languages_known` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `candidate`
--

INSERT INTO `candidate` (`candidate_id`, `candidate_dob`, `candidate_phone`, `candidate_identification_type`, `candidate_gender`, `candidate_allergies`, `candidate_food_preference`, `candidate_qualification`, `candidate_experience`, `candidate_occupation`, `candidate_computer_skills`, `candidate_languages_known`, `user_id`, `mission_id`) VALUES
(1, '2020-06-10 00:00:00', '+3892932', 'aadsjlka', 'Male', 'none', 'none', 'BA', '10', 'Doctor', 'python', 'English', 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL,
  `employee_title` varchar(100) NOT NULL,
  `employee_permissions` varchar(10000) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `employee_title`, `employee_permissions`, `user_id`) VALUES
(1, 'Mission Coordinator', 'None', 1),
(5, 'Administrator', 'None', 2),
(6, 'Mission Coordinator', 'None', 3),
(7, 'Administrator', 'None', 2),
(8, 'Mission Coordinator', 'None', 3);

-- --------------------------------------------------------

--
-- Table structure for table `mission`
--

CREATE TABLE `mission` (
  `mission_id` int(11) NOT NULL,
  `mission_name` varchar(100) NOT NULL,
  `mission_description` text DEFAULT NULL,
  `mission_origin_country` varchar(100) NOT NULL,
  `mission_countries_allowed` varchar(1000) DEFAULT NULL,
  `mission_coordinator_id` int(11) DEFAULT NULL,
  `mission_employment_requirement` varchar(1000) DEFAULT NULL,
  `mission_cargo_requirements` varchar(1000) DEFAULT NULL,
  `mission_launch_date` datetime DEFAULT NULL,
  `mission_location` varchar(1000) DEFAULT NULL,
  `mission_duration` int(11) DEFAULT NULL,
  `mission_status` enum('Planning Phase','Departed Earth','Landed on Mars','Mission in progress','Returned to Earth','Mission Completed') NOT NULL,
  `mission_shuttle_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mission`
--

INSERT INTO `mission` (`mission_id`, `mission_name`, `mission_description`, `mission_origin_country`, `mission_countries_allowed`, `mission_coordinator_id`, `mission_employment_requirement`, `mission_cargo_requirements`, `mission_launch_date`, `mission_location`, `mission_duration`, `mission_status`, `mission_shuttle_id`) VALUES
(1, 'Mission1', 'This mission is very important', 'India', 'India, Australia', 1, '{\'Civil Engineers\': 10}', 'none', '2020-06-30 00:00:00', 'Delhi, India', 10, 'Planning Phase', 1);

-- --------------------------------------------------------

--
-- Table structure for table `shuttle`
--

CREATE TABLE `shuttle` (
  `shuttle_id` int(11) NOT NULL,
  `shuttle_name` varchar(100) NOT NULL,
  `shuttle_manufacture_year` int(11) DEFAULT NULL,
  `shuttle_fuel_capacity` int(11) DEFAULT NULL,
  `shuttle_passenger_capacity` int(11) DEFAULT NULL,
  `shuttle_cargo_capacity` int(11) DEFAULT NULL,
  `shuttle_speed` int(11) DEFAULT NULL,
  `shuttle_origin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shuttle`
--

INSERT INTO `shuttle` (`shuttle_id`, `shuttle_name`, `shuttle_manufacture_year`, `shuttle_fuel_capacity`, `shuttle_passenger_capacity`, `shuttle_cargo_capacity`, `shuttle_speed`, `shuttle_origin`) VALUES
(1, 'shuttle1', 1990, 100, 12, 12, 1201, ''),
(2, 'shuttle_name', 0, 0, 0, 0, 0, 'shuttle_origin'),
(765, 'magna. Sed', 10, 977899900, 249, 502, 31837, 'Russian Federation'),
(770, 'dapibus gravida.', 4, 922124065, 249, 1203, 34676, 'United Kingdom'),
(775, 'tristique neque', 9, 604094652, 277, 1697, 30552, 'Russian Federation'),
(780, 'magna a', 1, 3365269, 260, 779, 30930, 'India'),
(785, 'accumsan convallis,', 6, 578248695, 248, 1054, 34503, 'Australia'),
(790, 'non, egestas', 8, 663650125, 238, 1764, 31200, 'United Kingdom'),
(795, 'eros. Nam', 5, 44923495, 232, 1634, 29415, 'United Kingdom'),
(800, 'dui augue', 6, 904495444, 214, 673, 31972, 'United States'),
(805, 'tellus faucibus', 8, 30897766, 233, 919, 30305, 'Canada'),
(810, 'gravida sagittis.', 3, 938197299, 235, 1776, 30568, 'United Kingdom'),
(815, 'nunc interdum', 1, 767708030, 206, 587, 31486, 'United States'),
(820, 'lacus, varius', 2, 491004413, 263, 1295, 31686, 'Austria'),
(825, 'lorem ac', 4, 818967197, 236, 1012, 34979, 'Russian Federation'),
(830, 'id magna', 5, 314476636, 242, 764, 28974, 'Australia'),
(835, 'hendrerit consectetuer,', 1, 885097786, 202, 789, 29266, 'Canada'),
(840, 'sem semper', 2, 45907518, 265, 1707, 30681, 'Germany'),
(845, 'cursus. Nunc', 10, 246072480, 230, 1001, 34360, 'Austria'),
(850, 'nisi a', 12, 212610363, 200, 1605, 34508, 'New Zealand'),
(855, 'egestas. Aliquam', 1, 430772492, 229, 870, 32763, 'United States'),
(860, 'magna sed', 3, 59177127, 260, 1015, 33991, 'India'),
(865, 'lorem, auctor', 5, 691985160, 240, 1693, 32766, 'Russian Federation'),
(870, 'dictum ultricies', 6, 724330737, 220, 1231, 34760, 'Australia'),
(875, 'gravida non,', 1, 14148549, 245, 1579, 28684, 'Austria'),
(880, 'odio. Nam', 4, 940253481, 200, 1375, 28233, 'United States'),
(885, 'faucibus id,', 8, 816691904, 208, 1097, 33302, 'Russian Federation'),
(890, 'mi. Duis', 3, 405856985, 251, 1931, 31381, 'Australia'),
(895, 'et libero.', 12, 500197680, 249, 1119, 30346, 'India'),
(900, 'lacus. Aliquam', 5, 330189562, 273, 1435, 29814, 'United States'),
(905, 'dolor dolor,', 9, 541413037, 238, 1850, 34464, 'United States'),
(910, 'risus. Morbi', 1, 461764956, 278, 1135, 30092, 'United States'),
(915, 'id risus', 8, 496130685, 275, 1651, 29430, 'Russian Federation'),
(920, 'et netus', 1, 221084734, 217, 1703, 31625, 'New Zealand'),
(925, 'vitae mauris', 11, 835102283, 255, 1372, 29350, 'Australia'),
(930, 'Etiam bibendum', 4, 700159166, 247, 941, 28157, 'Australia'),
(935, 'tellus. Nunc', 1, 139034563, 259, 1557, 31104, 'Australia'),
(940, 'arcu iaculis', 3, 9108305, 245, 1160, 30241, 'Germany'),
(945, 'Maecenas malesuada', 11, 39349510, 274, 506, 28220, 'Germany'),
(950, 'risus. Duis', 11, 145886969, 241, 1061, 28960, 'Russian Federation'),
(955, 'cursus vestibulum.', 3, 24000994, 210, 1638, 30671, 'Australia'),
(960, 'augue malesuada', 11, 43795251, 274, 501, 30213, 'Russian Federation'),
(965, 'pede. Praesent', 7, 841236043, 229, 988, 32621, 'Canada'),
(970, 'in magna.', 5, 960307904, 279, 886, 31522, 'Russian Federation'),
(975, 'vitae dolor.', 11, 712999390, 255, 1356, 32676, 'New Zealand'),
(980, 'enim diam', 6, 75816884, 250, 846, 33482, 'United Kingdom'),
(985, 'felis, adipiscing', 11, 944321683, 266, 1378, 32686, 'India'),
(990, 'lacinia at,', 10, 10905885, 263, 1291, 33588, 'Russian Federation'),
(995, 'eu, euismod', 11, 497955666, 227, 1740, 33000, 'Austria'),
(1000, 'risus quis', 9, 506004903, 213, 1992, 32745, 'Canada'),
(1005, 'enim. Suspendisse', 9, 101235915, 238, 628, 32275, 'Australia'),
(1010, 'a, auctor', 10, 569144870, 202, 1123, 31259, 'Canada'),
(1015, 'luctus. Curabitur', 12, 784198889, 249, 723, 30989, 'Austria'),
(1020, 'dui, in', 9, 714736944, 225, 1043, 31364, 'Germany'),
(1025, 'non nisi.', 12, 527861194, 203, 940, 33873, 'Austria'),
(1030, 'non massa', 8, 927418010, 224, 1377, 32962, 'Canada'),
(1035, 'Etiam vestibulum', 3, 737140240, 225, 730, 31224, 'United Kingdom'),
(1040, 'tempor diam', 10, 616822381, 264, 1855, 31156, 'India'),
(1050, 'vitae semper', 4, 909282194, 214, 1875, 29536, 'India'),
(1055, 'et ultrices', 3, 226090213, 225, 1162, 31141, 'Germany'),
(1060, 'metus vitae', 2, 388824205, 226, 1048, 34791, 'Australia'),
(1065, 'ac ipsum.', 11, 767443467, 215, 1641, 30411, 'India'),
(1075, 'at pede.', 6, 216963803, 263, 1858, 29338, 'United States'),
(1080, 'ullamcorper magna.', 2, 422150015, 213, 1592, 31110, 'Germany'),
(1085, 'velit justo', 10, 794657560, 230, 1237, 32127, 'Germany'),
(1090, 'a, dui.', 3, 225936341, 257, 1943, 29345, 'Australia'),
(1095, 'ac metus', 4, 108531676, 204, 1181, 30625, 'India'),
(1100, 'lorem, vehicula', 4, 469281348, 226, 1049, 32588, 'Austria'),
(1105, 'pulvinar arcu', 7, 266106973, 253, 627, 31908, 'India'),
(1110, 'ipsum non', 11, 826037855, 226, 539, 29892, 'Australia'),
(1115, 'mollis. Phasellus', 4, 143962011, 258, 1103, 30918, 'Canada'),
(1120, 'cursus purus.', 3, 689848590, 247, 1990, 31204, 'United Kingdom'),
(1125, 'Suspendisse ac', 1, 452920677, 258, 1115, 32067, 'India'),
(1130, 'id, libero.', 11, 593752036, 257, 1254, 31157, 'Austria'),
(1135, 'pede sagittis', 1, 705202373, 266, 1486, 29332, 'Germany'),
(1140, 'Praesent eu', 2, 780874619, 222, 1999, 33314, 'India'),
(1145, 'dictum placerat,', 5, 847516679, 235, 1430, 29262, 'Russian Federation'),
(1150, 'accumsan interdum', 7, 102550151, 257, 974, 32561, 'Austria'),
(1155, 'enim. Nunc', 2, 359745354, 249, 1366, 28765, 'Austria'),
(1160, 'diam eu', 11, 191145133, 240, 1262, 31415, 'United States'),
(1165, 'sed, sapien.', 5, 26692030, 273, 656, 34724, 'United States'),
(1170, 'Fusce aliquet', 7, 343786083, 258, 1666, 34617, 'Germany'),
(1175, 'Fusce aliquam,', 1, 373102602, 233, 1742, 33772, 'Russian Federation'),
(1180, 'Aenean eget', 8, 616110353, 232, 1269, 28255, 'New Zealand'),
(1190, 'egestas a,', 9, 583752877, 212, 1509, 33283, 'Austria'),
(1195, 'sem ut', 3, 573594170, 221, 1281, 30544, 'Germany'),
(1200, 'Cras vulputate', 11, 743760370, 278, 1390, 30455, 'New Zealand'),
(1205, 'sit amet,', 7, 690973197, 262, 1835, 31212, 'Germany'),
(1210, 'eget laoreet', 1, 917563297, 262, 1053, 29991, 'Russian Federation'),
(1215, 'ante lectus', 12, 704164219, 265, 973, 28622, 'Australia'),
(1220, 'sit amet', 10, 340473845, 218, 1017, 34711, 'Germany'),
(1225, 'Nulla dignissim.', 8, 386632337, 280, 1221, 31061, 'United Kingdom'),
(1230, 'magnis dis', 5, 337462286, 265, 585, 31790, 'Austria'),
(1240, 'pharetra ut,', 10, 413569076, 254, 1370, 35000, 'United Kingdom'),
(1245, 'vulputate eu,', 4, 925293620, 277, 889, 33930, 'Russian Federation'),
(1250, 'mauris sapien,', 11, 344254326, 241, 1635, 33906, 'Canada'),
(1255, 'Mauris quis', 11, 326061009, 209, 1351, 31124, 'Austria'),
(1260, 'enim. Mauris', 8, 207182491, 277, 1631, 33240, 'Austria');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `user_type` enum('Candidate','Employee') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `name`, `user_type`) VALUES
(1, 'krish.born2shine@gmail.com', 'sha256$p6UcBw2W$60c222356f7d8ceaf2de3c4eb05bba95e1da03e5ba62436eb8f252e1c88c58da', 'Krishna kanth Mundada', 'Candidate'),
(2, 'krishna.mundada27@gmail.com', 'sha256$By55SMPC$a80c13ba66a137cc7bc5d1f0d8fe22fbbc31762a1419aaf1f46bda2d3af5e81c', 'Krishna kanth Mundada', 'Employee'),
(3, 'demo@gmail.com', 'sha256$Z0vtFoG4$016a14e32071903afc036c6490e6380fbb4f1eaba445dd80abb44bd92f365313', 'demo account', 'Employee'),
(4, 'demo_candidate@gmail.com', 'sha256$nffctYbe$04971fa856cc805ddb54154c895445a6215153f5a6db1a7ffd74f88a396c7dce', 'candidate', 'Candidate'),
(5, 'demo_admin@gmail.com', 'sha256$K1FPappB$360fb80b5719132153fe306bbab1df476a628df106ccba5155a2c5213a7b9b65', 'Administrator', 'Employee'),
(6, 'demo_mc@gmail.com', 'sha256$nIOlOaNt$630d11892eeaa5cf780e903d56747548888726fac834c7761e9fbb7f9914a254', 'Mission Coordinator', 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candidate`
--
ALTER TABLE `candidate`
  ADD PRIMARY KEY (`candidate_id`),
  ADD UNIQUE KEY `candidate_phone` (`candidate_phone`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employee_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `mission`
--
ALTER TABLE `mission`
  ADD PRIMARY KEY (`mission_id`),
  ADD UNIQUE KEY `mission_name` (`mission_name`),
  ADD KEY `mission_coordinator_id` (`mission_coordinator_id`),
  ADD KEY `mission_shuttle_id` (`mission_shuttle_id`);

--
-- Indexes for table `shuttle`
--
ALTER TABLE `shuttle`
  ADD PRIMARY KEY (`shuttle_id`),
  ADD UNIQUE KEY `shuttle_name` (`shuttle_name`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `candidate`
--
ALTER TABLE `candidate`
  MODIFY `candidate_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `mission`
--
ALTER TABLE `mission`
  MODIFY `mission_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `shuttle`
--
ALTER TABLE `shuttle`
  MODIFY `shuttle_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1261;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `candidate`
--
ALTER TABLE `candidate`
  ADD CONSTRAINT `candidate_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `mission`
--
ALTER TABLE `mission`
  ADD CONSTRAINT `mission_ibfk_1` FOREIGN KEY (`mission_coordinator_id`) REFERENCES `employee` (`employee_id`),
  ADD CONSTRAINT `mission_ibfk_2` FOREIGN KEY (`mission_shuttle_id`) REFERENCES `shuttle` (`shuttle_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
