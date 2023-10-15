-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Oct 15, 2023 at 12:38 AM
-- Server version: 10.5.16-MariaDB
-- PHP Version: 8.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Potatofacts`
--

-- --------------------------------------------------------

--
-- Table structure for table `facts`
--

CREATE TABLE `facts` (
  `factid` smallint(6) DEFAULT NULL,
  `facttext` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facts`
--

INSERT INTO `facts` (`factid`, `facttext`) VALUES
(1, 'The first permanent potato patches in North America were established in 1719 near Londonderry, New Hampshire, USA.\r\n'),
(2, 'Today potatoes are grown in all 50 states of the USA and in about 125 countries throughout the world. \r\n'),
(3, 'People have been growing potatoes for at least 7,000 years!\r\n'),
(4, 'In 1995, potatoes became the first vegetable to be grown in space!\r\n'),
(5, 'The sweet potato belongs in the same family as morning glories while the white potato belongs to the same group as tomatoes, tobacco, chile pepper, eggplant and the petunia.\r\n'),
(6, 'The potato is about 80% water and 20% solids.\r\n'),
(7, 'An 8 ounce baked or boiled potato has only about 100 calories.\r\n'),
(9, 'In 1974, an Englishman named Eric Jenkins grew 370 pounds of potatoes from one plant.\r\n'),
(10, 'Thomas Jefferson gets the credit for introducing “french fries” to America when he served them at a White House dinner.\r\n'),
(11, 'According to the Guinness Book of World Records, the largest potato grown was 7 pounds 1 ounce by J. East (1953) and J. Busby (1982) of Great Britain. \r\n'),
(12, 'The worlds largest potato chip crisp was produced by the Pringles Company in Jackson, TN, in 1990. It measures 23 feet x 14.5 feet. \r\n'),
(13, 'In October 1995, the potato became the first vegetable to be grown in space. NASA and the University of Wisconsin, Madison, created the technology with the goal of feeding astronauts on long space voyages, and eventually, feeding future space colonies. \r\n'),
(14, 'Potato blossoms used to be a big hit in royal fashion. Potatoes first became fashionable when Marie Antoinette paraded through the French countryside wearing potato blossoms in her hair. \r\n'),
(15, 'The Incas of Peru were the first to cultivate potatoes around 8000 BC to 5000 BC. \r\n'),
(16, 'In 1536 Spanish Conquistadors discovered just how delicious potatoes were and carried them back to Europe. \r\n'),
(17, 'In 1589 Sir Walter Raleigh introduced potatoes to Ireland.  Early growers discovered that they could provide food for ten people off of just one acre of land, much better than wheat or oats. \r\n'),
(18, 'Potatoes came to the colonies in 1621 when the Governor of Bermuda, Nathaniel Butler sent two large cedar chests containing potatoes to Jamestown. \r\n'),
(19, 'Potatoes were popularized in France in the 18th century.  King Louis XIV and Antoine Parmentier hosted a dinner that featured only dishes with potato.  Benjamin Franklin was in attendance at the 1767 dinner.  Twenty different dishes were served! \r\n'),
(20, 'In Shakespeares time the potato was known simply as the apple of love. \r\n'),
(21, 'Vincent Van Gough painted four still-life paintings featuring potatoes. \r\n'),
(22, 'Thank Thomas Jefferson next time you have french fries.  He served them in the White House! \r\n'),
(23, 'Potatoes didnt arrive in Idaho until 1836. \r\n'),
(24, 'The Irish potato famine occurred in the 1840s, caused by the oomycete, Phytophthora infestans, meaning plant destroyer.  Before the disease struck, Irish families ate nearly ten pounds of potato a day.  Almost one million people died from starvation or disease during that time period. \r\n'),
(25, 'Potatoes first appeared in Montana in 1841. The first crop was grown in the Bitteroot Valley at St. Marys Mission by Father DeSmet. \r\n'),
(26, 'A complaining railroad magnate earned a chastisement for complaints from chef George Crum, resulting in “Saratoga Crunch Chips,” known to us as potato chips in 1853. A delicious punishment! \r\n'),
(27, 'During the gold rush, potatoes were highly valued.  At a time when gold was more plentiful than nutrition sources, you might say that potatoes were worth their weight in gold! \r\n'),
(28, 'In 1860, the first Montana commercial crop was grown in Virginia City at the mining camps.  This was especially significant because this was miners only source of vitamin C! \r\n'),
(29, 'Russet Burbank has been around since 1872! \r\n'),
(30, 'In 1903, Parker Brothers had a game called The Potato Race. \r\n'),
(31, 'In Germany there is a monument to the potato with the inscription To God and Francis Drake, who brought to Europe for the everlasting benefit of the poor-the Potato.\r\n'),
(32, 'The word potato comes from the Spanish word patata.\r\n'),
(33, 'Potato is the 4th most important crop worldwide, But 1st in our book!\r\n'),
(34, 'The Irish Potato famine gave rise to the field of Plant Pathology!\r\n'),
(35, '35% of the potato crop is turned into french fries, 28% is used for fresh, and 13% goes to chips!\r\n'),
(36, 'The Potato Museum in Washington DC contains 2000 potato artifacts.\r\n'),
(37, 'A potato has more potassium than a banana!\r\n'),
(38, '2008 was the U.N. International Year of the Potato.\r\n'),
(39, 'August 13 is National Potato Day, dont forget to celebrate!\r\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



























