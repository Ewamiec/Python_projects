-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 14 Cze 2020, 16:42
-- Wersja serwera: 10.4.6-MariaDB
-- Wersja PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `tinkter_baza`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `links`
--

CREATE TABLE `links` (
  `Link_ID` int(11) DEFAULT NULL,
  `Link_name` varchar(30) COLLATE utf8_polish_ci DEFAULT NULL,
  `Description` varchar(100) COLLATE utf8_polish_ci DEFAULT NULL,
  `URL` varchar(100) COLLATE utf8_polish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `links`
--

INSERT INTO `links` (`Link_ID`, `Link_name`, `Description`, `URL`) VALUES
(1, 'Filmweb', 'Polski portal kinomaniaków', 'http://filmweb.pl'),
(2, 'mBank', 'Sprawdź, czy nie jesteś na debecie!', 'http://mbank.pl'),
(3, 'Facebook', 'Portal egotyków - bądź, kim chcesz!', 'http://facebook.com'),
(4, 'Spotify', 'Streaming muzyki wszelakiej', 'http://spotify.com'),
(5, 'YouTube', 'Wszystko i nic - on the record', 'http://youtube.com'),
(6, 'Messenger', 'Gdy chcesz ograniczyć FB tylko do wiadomości', 'http://messenger.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
