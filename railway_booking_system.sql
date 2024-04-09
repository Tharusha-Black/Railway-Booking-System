-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 08, 2024 at 11:40 AM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `railway_booking_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add seat', 7, 'add_seat'),
(26, 'Can change seat', 7, 'change_seat'),
(27, 'Can delete seat', 7, 'delete_seat'),
(28, 'Can view seat', 7, 'view_seat'),
(29, 'Can add train schedule', 8, 'add_trainschedule'),
(30, 'Can change train schedule', 8, 'change_trainschedule'),
(31, 'Can delete train schedule', 8, 'delete_trainschedule'),
(32, 'Can view train schedule', 8, 'view_trainschedule'),
(33, 'Can add train', 9, 'add_train'),
(34, 'Can change train', 9, 'change_train'),
(35, 'Can delete train', 9, 'delete_train'),
(36, 'Can view train', 9, 'view_train'),
(37, 'Can add user', 10, 'add_railwayuser'),
(38, 'Can change user', 10, 'change_railwayuser'),
(39, 'Can delete user', 10, 'delete_railwayuser'),
(40, 'Can view user', 10, 'view_railwayuser'),
(41, 'Can add train', 11, 'add_train'),
(42, 'Can change train', 11, 'change_train'),
(43, 'Can delete train', 11, 'delete_train'),
(44, 'Can view train', 11, 'view_train');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$cE4EK8tVxHj4vnaS9LF73Q$QsdzpgT79zU8gv6bjITa+vEGaVSmaXvZen3ava/7Rbc=', NULL, 1, 'Tharusha', '', '', 'stheshan4@gmail.com', 1, 1, '2024-04-06 06:09:58.982511');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'seat_booking_service', 'seat'),
(8, 'train_schedule_service', 'trainschedule'),
(9, 'train_search_service', 'train'),
(10, 'user_management', 'railwayuser'),
(11, 'train_schedule_service', 'train');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-04-06 06:09:28.522266'),
(2, 'auth', '0001_initial', '2024-04-06 06:09:28.854084'),
(3, 'admin', '0001_initial', '2024-04-06 06:09:28.959371'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-04-06 06:09:28.964409'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-06 06:09:28.971594'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-04-06 06:09:29.016761'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-04-06 06:09:29.042380'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-04-06 06:09:29.068101'),
(9, 'auth', '0004_alter_user_username_opts', '2024-04-06 06:09:29.074263'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-04-06 06:09:29.105136'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-04-06 06:09:29.105136'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-04-06 06:09:29.109393'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-04-06 06:09:29.137246'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-04-06 06:09:29.165979'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-04-06 06:09:29.185886'),
(16, 'auth', '0011_update_proxy_permissions', '2024-04-06 06:09:29.194282'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-04-06 06:09:29.219558'),
(18, 'train_search_service', '0001_initial', '2024-04-06 06:09:29.225139'),
(19, 'seat_booking_service', '0001_initial', '2024-04-06 06:09:29.277312'),
(20, 'sessions', '0001_initial', '2024-04-06 06:09:29.311290'),
(21, 'train_schedule_service', '0001_initial', '2024-04-06 06:09:29.342543'),
(22, 'user_management', '0001_initial', '2024-04-06 06:18:41.241152'),
(23, 'train_search_service', '0002_auto_20240406_1407', '2024-04-06 08:37:35.000870'),
(24, 'train_search_service', '0003_auto_20240407_0908', '2024-04-07 03:38:42.252237'),
(25, 'train_schedule_service', '0002_train_trainschedule_destination_and_more', '2024-04-07 03:45:11.694380'),
(26, 'train_schedule_service', '0003_alter_trainschedule_departure_time', '2024-04-07 07:13:40.033053'),
(27, 'train_schedule_service', '0004_remove_trainschedule_destination_train_route_1_and_more', '2024-04-07 09:25:26.943957'),
(28, 'train_schedule_service', '0005_remove_trainschedule_start_location', '2024-04-07 09:25:26.970401'),
(29, 'train_schedule_service', '0006_remove_train_train_tag', '2024-04-07 09:44:15.999345'),
(30, 'train_schedule_service', '0007_rename_route_trainschedule_destination_and_more', '2024-04-07 10:48:35.008038'),
(31, 'train_schedule_service', '0008_train_route', '2024-04-07 10:53:11.703885'),
(32, 'seat_booking_service', '0002_remove_seat_train_seat_block_letter_seat_schedule_and_more', '2024-04-07 13:58:58.455432'),
(33, 'seat_booking_service', '0003_remove_seat_block_letter_remove_seat_is_booked_and_more', '2024-04-07 16:55:24.255259'),
(34, 'seat_booking_service', '0004_alter_seat_schedule_alter_seat_user', '2024-04-08 05:32:54.113743');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('max9qtjhv63atu1npj4hgh1j5l4i6cic', '.eJxVjMsOwiAQRf-FtSE8ygAu3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmip1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb81IGqplTCSincxpyITKE8qSyc8FLKkwSrvhZYTYBHaWA8gbILJuOTY-wPO8jbI:1rtnMK:drleihMC7GTOYHQFKspjjN9AvHeH2R5p04SHdzrw6b8', '2024-04-22 11:40:20.624353'),
('yyr00xfrtvtu9aj48actcylzslgw1hk8', '.eJxVjMsOwiAQRf-FtSE8ygAu3fsNZIBBqgaS0q6M_65NutDtPefcFwu4rTVsg5YwZ3Zmip1-t4jpQW0H-Y7t1nnqbV3myHeFH3Twa8_0vBzu30HFUb81IGqplTCSincxpyITKE8qSyc8FLKkwSrvhZYTYBHaWA8gbILJuOTY-wPO8jbI:1rtKR3:Jrd9dZDTgVZ-mht7GJbkAG2oHFQFTa_5gOKZeC12Yjk', '2024-04-21 04:47:17.661325');

-- --------------------------------------------------------

--
-- Table structure for table `seat_booking_service_seat`
--

DROP TABLE IF EXISTS `seat_booking_service_seat`;
CREATE TABLE IF NOT EXISTS `seat_booking_service_seat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `schedule_id` bigint NOT NULL,
  `seat_numbers` varchar(50) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `seat_booking_service_seat_schedule_id_1a2b60c2` (`schedule_id`),
  KEY `seat_booking_service_seat_user_id_3cf79892` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `seat_booking_service_seat`
--

INSERT INTO `seat_booking_service_seat` (`id`, `schedule_id`, `seat_numbers`, `user_id`) VALUES
(108, 15, 'A3,A4,A6,A7,A8', 4),
(107, 15, 'B1,B5,B9', 3),
(105, 14, 'A1,A5', 2),
(104, 13, 'B1,B2,B3', 2);

-- --------------------------------------------------------

--
-- Table structure for table `train_schedule_service_train`
--

DROP TABLE IF EXISTS `train_schedule_service_train`;
CREATE TABLE IF NOT EXISTS `train_schedule_service_train` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `train_name` varchar(100) NOT NULL,
  `route` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `train_schedule_service_train`
--

INSERT INTO `train_schedule_service_train` (`id`, `train_name`, `route`) VALUES
(9, 'Train 1', 'COLOMBO - JAFFNA');

-- --------------------------------------------------------

--
-- Table structure for table `train_schedule_service_trainschedule`
--

DROP TABLE IF EXISTS `train_schedule_service_trainschedule`;
CREATE TABLE IF NOT EXISTS `train_schedule_service_trainschedule` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `departure_time` varchar(100) NOT NULL,
  `train_id` bigint NOT NULL,
  `schedule_date` date NOT NULL,
  `destination` varchar(50) NOT NULL,
  `start_location` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `train_schedule_service_trainschedule_train_id_8b23d0aa` (`train_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `train_schedule_service_trainschedule`
--

INSERT INTO `train_schedule_service_trainschedule` (`id`, `departure_time`, `train_id`, `schedule_date`, `destination`, `start_location`) VALUES
(15, '10:00', 9, '2024-04-21', 'COLOMBO', 'GALLE'),
(16, '23:00', 9, '2024-04-10', 'COLOMBO', 'TRINCOMALE');

-- --------------------------------------------------------

--
-- Table structure for table `train_search_service_train`
--

DROP TABLE IF EXISTS `train_search_service_train`;
CREATE TABLE IF NOT EXISTS `train_search_service_train` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `start_station` varchar(100) NOT NULL,
  `destination_station` varchar(100) NOT NULL,
  `departure_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_management_railwayuser`
--

DROP TABLE IF EXISTS `user_management_railwayuser`;
CREATE TABLE IF NOT EXISTS `user_management_railwayuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `NIC` varchar(12) NOT NULL,
  `registered_date` date NOT NULL,
  `country` varchar(100) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `date_of_birth` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_management_railwayuser`
--

INSERT INTO `user_management_railwayuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `NIC`, `registered_date`, `country`, `mobile_number`, `date_of_birth`) VALUES
(1, 'pbkdf2_sha256$720000$CfZ4aqp4OjSDpT3gfWzwAA$ZfkqPviqhzuQobE3oImW+/C+lqYZQpnSXrdVSy0s8dA=', '2024-04-07 04:47:08.366721', 0, 'st', 'st', 'Hesha', 'heshan@gmail.com', 0, 1, '2024-04-06 06:19:59.931573', '1234567899', '2024-04-06', 'LK', '0147852369', '2024-04-11'),
(2, 'pbkdf2_sha256$720000$eXUc9dbgwQjKpfONWzzwtd$PJpijgO1La/TMU1rn0OjN1znIXGTDiXMZ41iXh3+8xs=', '2024-04-08 11:40:20.622359', 1, 'ggwp', 'gg', 'wp', 'ggwp@gmail.com', 0, 1, '2024-04-06 09:03:52.898058', '2211334455', '2024-04-06', 'AF', '0258147369', '2024-04-01'),
(3, 'pbkdf2_sha256$720000$5fYHj8N3kB4gj6gsjsylMr$Ni2324faAlSWen/oBJ/nrw/nKEZ+vI+X7Js/xMojZFY=', '2024-04-08 08:31:19.211302', 0, 'stk', 'stk', 'kts', 'stk@gmail.com', 0, 1, '2024-04-08 03:53:17.154813', '22331122553', '2024-04-08', 'AF', '052967055', '2024-03-08'),
(4, 'pbkdf2_sha256$720000$ebpx9tq8jtS8sS07MX1X2z$47cn4a+FItRt3K8IVR8UePEGfJIgIQLE68ed0OQoWVM=', '2024-04-08 07:03:14.281078', 0, 'animal', 'animal', 'pererea', 'animal@gmail.com', 0, 1, '2024-04-08 06:35:09.261835', '1144772255', '2024-04-08', 'AO', '0258369741', '2024-01-23');

-- --------------------------------------------------------

--
-- Table structure for table `user_management_railwayuser_groups`
--

DROP TABLE IF EXISTS `user_management_railwayuser_groups`;
CREATE TABLE IF NOT EXISTS `user_management_railwayuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `railwayuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_management_railwayu_railwayuser_id_group_id_f44b95d1_uniq` (`railwayuser_id`,`group_id`),
  KEY `user_management_railwayuser_groups_railwayuser_id_631ec80e` (`railwayuser_id`),
  KEY `user_management_railwayuser_groups_group_id_3547aba1` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_management_railwayuser_user_permissions`
--

DROP TABLE IF EXISTS `user_management_railwayuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `user_management_railwayuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `railwayuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_management_railwayu_railwayuser_id_permissio_7a37b77e_uniq` (`railwayuser_id`,`permission_id`),
  KEY `user_management_railwayuser_railwayuser_id_49ea503f` (`railwayuser_id`),
  KEY `user_management_railwayuser_permission_id_60e1da8d` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
