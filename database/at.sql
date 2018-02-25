-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 22, 2018 at 12:02 PM
-- Server version: 10.1.26-MariaDB
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `at`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins`
--

CREATE TABLE `admins` (
  `admin_id` int(11) NOT NULL,
  `admin_name` varchar(50) NOT NULL,
  `admin_fingerPrint` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admins`
--

INSERT INTO `admins` (`admin_id`, `admin_name`, `admin_fingerPrint`) VALUES
(0, 'Cigdem Vudali', 'NULL'),
(1, 'Mehmet Topal', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `att_record`
--

CREATE TABLE `att_record` (
  `student_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `attend` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `att_record`
--

INSERT INTO `att_record` (`student_id`, `course_id`, `date`, `time`, `attend`) VALUES
(0, 0, '2017/11/29', '08:00', '1'),
(0, 1, '2017/11/29', '09:00', '0'),
(0, 2, '2017/11/29', '10:00', '1'),
(2, 3, '2017/11/29', '11:00', '0'),
(2, 4, '2017/11/29', '12:00', '1'),
(2, 5, '2017/11/29', '13:00', '0'),
(4, 6, '2017/11/29', '14:00', '0'),
(8, 7, '2017/11/29', '15:00', '1'),
(8, 8, '2017/11/29', '16:00', '1'),
(8, 9, '2017/11/29', '17:00', '1'),
(1, 2, '1/1/1111', '08:00', '1'),
(1, 2, '1/1/1111', '08:00', '1'),
(1, 3, '2018-01-21', '23:25', '1'),
(1, 3, '2018-01-21', '23:25', '1'),
(1, 3, '2018-01-21', '23:36', '1'),
(1, 3, '2018-01-21', '23:40', '1'),
(1, 3, '2018-01-21', '23:41', '1'),
(1, 3, '2018-01-21', '23:42', '1'),
(1, 3, '2018-01-21', '23:42', '1'),
(1, 3, '2018-01-21', '23:59', '1'),
(1, 3, '2018-01-22', '00:18', '1'),
(1, 3, '2018-01-22', '01:35', '1'),
(1, 3, '2018-01-22', '01:35', '1'),
(1, 3, '2018-01-22', '01:35', '1'),
(1, 3, '2018-01-22', '01:35', '1'),
(2, 3, '2018-01-22', '01:43', '1'),
(1, 3, '2018-01-22', '01:51', '1'),
(2, 3, '2018-01-22', '01:51', '1'),
(1, 3, '2018-01-22', '01:51', '1'),
(2, 3, '2018-01-22', '01:51', '1'),
(2, 3, '2018-01-22', '01:51', '1'),
(2, 3, '2018-01-22', '03:17', '1'),
(1, 3, '2018-01-22', '03:17', '1'),
(2, 3, '2018-01-22', '09:17', '1'),
(1, 3, '2018-01-22', '09:17', '1'),
(1, 3, '2018-01-22', '09:41', '1'),
(2, 3, '2018-01-22', '09:41', '1'),
(1, 3, '2018-01-22', '09:53', '1'),
(1, 3, '2018-01-22', '09:56', '1'),
(1, 3, '2018-01-22', '09:58', '1'),
(1, 3, '2018-01-22', '10:00', '1'),
(1, 3, '2018-01-22', '10:02', '1'),
(1, 3, '2018-01-22', '11:25', '1'),
(12, 1, '2018-01-22', '11:55', '1'),
(12, 2, '2018-01-22', '11:56', '1'),
(2, 1, '2018-01-22', '12:05', '1'),
(1, 1, '2018-01-22', '12:05', '1'),
(12, 1, '2018-01-22', '12:05', '1'),
(12, 1, '2018-01-22', '12:05', '1'),
(2, 1, '2018-01-22', '12:05', '1'),
(1, 1, '2018-01-22', '12:05', '1'),
(1, 3, '2018-01-22', '12:25', '1'),
(2, 3, '2018-01-22', '12:25', '1'),
(4, 3, '2018-01-22', '12:28', '1'),
(1, 2, '2018-01-22', '12:30', '1');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `course_code` varchar(20) DEFAULT NULL,
  `course_group` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `course_code`, `course_group`) VALUES
(0, 'CMPE462\r\n', 0),
(1, 'CMPE371', 0),
(2, 'CMPE423', 0),
(3, 'CMPE412', 0),
(4, 'CMPE324\r\n', 0),
(5, 'CMPE471', 0),
(6, 'CMPE223', 0),
(7, 'CMPE224', 0),
(8, 'CMPE108 ', 0),
(9, 'CMPE343', 0);

-- --------------------------------------------------------

--
-- Table structure for table `enrolment`
--

CREATE TABLE `enrolment` (
  `student_Id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `enrolment`
--

INSERT INTO `enrolment` (`student_Id`, `course_id`) VALUES
(1, 0),
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(3, 6),
(4, 3),
(4, 4),
(4, 5),
(4, 6),
(4, 7),
(5, 4),
(5, 5),
(5, 6),
(5, 7),
(5, 8),
(6, 5),
(6, 6),
(6, 7),
(6, 8),
(6, 9),
(7, 0),
(7, 6),
(7, 7),
(7, 8),
(7, 9),
(8, 0),
(8, 1),
(8, 7),
(8, 8),
(8, 9),
(9, 0),
(9, 1),
(9, 2),
(9, 8),
(9, 9),
(10, 0),
(10, 1),
(10, 2),
(10, 3),
(10, 9),
(11, 0),
(11, 1),
(11, 2),
(11, 3),
(11, 4),
(12, 1),
(12, 2),
(12, 3),
(12, 4),
(12, 5);

-- --------------------------------------------------------

--
-- Table structure for table `instructor`
--

CREATE TABLE `instructor` (
  `instructor_id` int(11) NOT NULL,
  `instructor_name` varchar(50) NOT NULL,
  `instructor_fingerPrint` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `instructor`
--

INSERT INTO `instructor` (`instructor_id`, `instructor_name`, `instructor_fingerPrint`) VALUES
(1, 'Muhammed Salamah', 'NULL'),
(2, 'Zeki Bayram', 'NULL'),
(3, 'Mehmet Bodur', 'NULL'),
(4, 'Alexander Chefranov', 'NULL'),
(5, 'Omar Ramadan', 'NULL'),
(6, 'Adnan Acan', 'NULL');

-- --------------------------------------------------------

--
-- Table structure for table `instructor_courses`
--

CREATE TABLE `instructor_courses` (
  `instructor_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `instructor_courses`
--

INSERT INTO `instructor_courses` (`instructor_id`, `course_id`) VALUES
(1, 5),
(2, 0),
(3, 2),
(4, 3),
(5, 4),
(6, 1),
(1, 6),
(1, 7),
(6, 8),
(4, 9);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `fingerPrint` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `fingerPrint`) VALUES
(0, 'test ', 'NULL'),
(1, 'Omar Crumpe', 'NULL'),
(2, 'Seymour Gass', 'NULL'),
(3, 'Maximilian Beeswing', 'NULL'),
(4, 'Luce Ivey', 'NULL'),
(5, 'Elladine Camellini', NULL),
(6, 'Zola Fucher', 'NULL'),
(7, 'Loree Lathee', 'NULL'),
(8, 'Jessee Shmyr', 'NULL'),
(9, 'Shaina Harris', 'NULL'),
(10, 'Kariotta Gravenall', 'NULL'),
(11, 'Ali komomo', 'NULL'),
(12, 'Bombo Sudani', 'NULL');

-- --------------------------------------------------------

--
-- Table structure for table `time_table`
--

CREATE TABLE `time_table` (
  `course_id` int(11) NOT NULL,
  `class` varchar(20) NOT NULL,
  `day` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `time_table`
--

INSERT INTO `time_table` (`course_id`, `class`, `day`, `time`) VALUES
(0, 'CMPE001', 'FRI', '14:00'),
(0, 'CMPE001', 'MON', '08:00'),
(0, 'CMPE001', 'TUE', '17:00'),
(0, 'CMPE002', 'THR', '15:00'),
(0, 'CMPE003', 'WED', '16:00'),
(1, 'CMPE001', 'TUE', '08:00'),
(1, 'CMPE001', 'WED', '17:00'),
(1, 'CMPE002', 'FRI', '15:00'),
(1, 'CMPE002', 'MON', '09:00'),
(1, 'CMPE003', 'THR', '16:00'),
(2, 'CMPE001', 'THR', '17:00'),
(2, 'CMPE001', 'WED', '08:00'),
(2, 'CMPE002', 'TUE', '09:00'),
(2, 'CMPE003', 'FRI', '16:00'),
(2, 'CMPE003', 'MON', '10:00'),
(3, 'CMPE001', 'FRI', '17:00'),
(3, 'CMPE001', 'MON', '11:00'),
(3, 'CMPE001', 'THR', '08:00'),
(3, 'CMPE002', 'WED', '09:00'),
(3, 'CMPE003', 'TUE', '10:00'),
(4, 'CMPE001', 'FRI', '08:00'),
(4, 'CMPE001', 'TUE', '11:00'),
(4, 'CMPE002', 'MON', '12:00'),
(4, 'CMPE002', 'THR', '09:00'),
(4, 'CMPE003', 'WED', '10:00'),
(5, 'CMPE001', 'WED', '11:00'),
(5, 'CMPE002', 'FRI', '09:00'),
(5, 'CMPE002', 'TUE', '12:00'),
(5, 'CMPE003', 'MON', '13:00'),
(5, 'CMPE003', 'THR', '10:00'),
(6, 'CMPE001', 'MON', '14:00'),
(6, 'CMPE001', 'THR', '11:00'),
(6, 'CMPE002', 'WED', '12:00'),
(6, 'CMPE003', 'FRI', '10:00'),
(6, 'CMPE003', 'TUE', '13:00'),
(7, 'CMPE001', 'FRI', '11:00'),
(7, 'CMPE001', 'TUE', '14:00'),
(7, 'CMPE002', 'MON', '15:00'),
(7, 'CMPE002', 'THR', '12:00'),
(7, 'CMPE003', 'WED', '13:00'),
(8, 'CMPE001', 'WED', '14:00'),
(8, 'CMPE002', 'FRI', '12:00'),
(8, 'CMPE002', 'TUE', '15:00'),
(8, 'CMPE003', 'MON', '16:00'),
(8, 'CMPE003', 'THR', '13:00'),
(9, 'CMPE001', 'MON', '17:00'),
(9, 'CMPE001', 'THR', '14:00'),
(9, 'CMPE002', 'WED', '15:00'),
(9, 'CMPE003', 'FRI', '13:00'),
(9, 'CMPE003', 'TUE', '16:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins`
--
ALTER TABLE `admins`
  ADD UNIQUE KEY `admin_id` (`admin_id`) USING BTREE;

--
-- Indexes for table `att_record`
--
ALTER TABLE `att_record`
  ADD KEY `courses_att_record` (`course_id`),
  ADD KEY `student_att_record` (`student_id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `enrolment`
--
ALTER TABLE `enrolment`
  ADD PRIMARY KEY (`student_Id`,`course_id`),
  ADD KEY `course_enrolment` (`course_id`);

--
-- Indexes for table `instructor`
--
ALTER TABLE `instructor`
  ADD PRIMARY KEY (`instructor_id`);

--
-- Indexes for table `instructor_courses`
--
ALTER TABLE `instructor_courses`
  ADD KEY `instructor_id` (`instructor_id`),
  ADD KEY `instructor_course` (`course_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `time_table`
--
ALTER TABLE `time_table`
  ADD PRIMARY KEY (`course_id`,`class`,`day`,`time`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `att_record`
--
ALTER TABLE `att_record`
  ADD CONSTRAINT `courses_att_record` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `student_att_record` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `enrolment`
--
ALTER TABLE `enrolment`
  ADD CONSTRAINT `course_enrolment` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `student_enrolment` FOREIGN KEY (`student_Id`) REFERENCES `students` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `instructor_courses`
--
ALTER TABLE `instructor_courses`
  ADD CONSTRAINT `instructor_course` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`),
  ADD CONSTRAINT `instructor_id` FOREIGN KEY (`instructor_id`) REFERENCES `instructor` (`instructor_id`);

--
-- Constraints for table `time_table`
--
ALTER TABLE `time_table`
  ADD CONSTRAINT `courses_time_table` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
