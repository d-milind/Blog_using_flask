-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2020 at 05:34 PM
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
-- Database: `doanything`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(12) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'First Post', 'firstpost@gmail.com', '1234567890', 'First post - to check - is it working properly?', '2020-05-06 17:03:27'),
(2, 'second', 'second@gmail.com', '1212121212', 'asdadsas', NULL),
(3, 'third', 'third@gmail.com', '121232334', 'third', '2020-05-06 18:25:26'),
(4, 'forth', 'forth@gmail.com', '121232334', 'Want to talk to you for the flask application', '2020-05-07 01:19:13'),
(5, 'forth', 'forth@gmail.com', '121232334', 'asdasd', '2020-05-07 01:27:04'),
(6, 'forth', 'forth@gmail.com', '121232334', 'sxvc', '2020-05-07 01:34:18');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(30) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'Lets learn about stock market Infosys', 'This is first post Tagline Milind', 'first-post ', 'Stock (also capital stock) of a corporation, is all of the shares into which ownership of the corporation is divided.[1] In American English, the shares are collectively known as \"stock\".[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares.  ', 'first dsdf', '2020-05-08 13:46:11'),
(3, 'Engineering', 'Department:Engineering', 'engg-post', 'Books in this area deal with engineering: the discipline and profession of acquiring and applying technical, scientific, and mathematical knowledge in order to design and implement materials, structures, machines, devices, systems, and processes that safely realize a desired objective.', '', '2020-05-07 13:18:02'),
(4, 'America 2', 'Latin-American History', 'america-post', 'Latin America is a region of startling physical contrasts which stretches 7,000 miles southward from the Mexican-U.S. border to the tip of Tierra del Fuego on Cape Horn. It is a region of diverse geography which has influenced the development of unique Latin American nations. There are two dominant characteristics of the landscape: large mountain ranges and vast river systems. The mountain ranges form the backbone of the landmass, with peaks of about 22,000 feet. Due to their relative impassibility, they have hindered trade and communications in Mexico and the nations in Latin America. These mountain ranges have separated nations from each other as well as individual regions with nations. The three river systems (the Río de la Plata, the Amazon, and the Orinoco) lie in rural areas, and have also impeded the development of transportation and settlements. Modern technology however has helped to bridge these geological barriers and help create individual nations and strong trade markets. In the west, the majority of the populations are located inland rather than on the coast. None of the major cities are ports, and there are few harbors available. This is in sharp contrast the eastern coast where the majority of the cities are ports. ', '', '2020-05-08 11:48:16'),
(10, 'qwassdsdasdas', 'q', 'w', 'qw', 'w', '2020-05-08 14:17:50'),
(11, 'ABCD', 'ABCD', 'ABCD', 'ABCD', 'ABCD', '2020-05-08 14:03:39');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
