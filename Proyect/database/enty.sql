-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-10-2023 a las 06:52:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `enty`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `Identificación` varchar(6) NOT NULL,
  `Nombre` varchar(150) NOT NULL,
  `Apellidos` varchar(150) NOT NULL,
  `Fecha_inicio` varchar(15) NOT NULL,
  `Hora_entrada` varchar(15) NOT NULL,
  `Hora_salida` varchar(15) NOT NULL,
  `Sueldo` varchar(7) NOT NULL,
  `Edad` varchar(3) NOT NULL,
  `Recidencia` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`Identificación`, `Nombre`, `Apellidos`, `Fecha_inicio`, `Hora_entrada`, `Hora_salida`, `Sueldo`, `Edad`, `Recidencia`) VALUES
('6011', 'Hennrry Geovanny', 'Canahui Gomez', '1/12/2023', '7:00 A.M', '8:30 A.M', '6000', '18', 'Puerto Barrios, 22 calle'),
('6703', '2', '2', '2/2/2', '2 P.M', '2 P.M', '2', '2', '2'),
('7486', '7', '7', '7/7/7', '7 P.M', '7 P.M', '7', '7', '7'),
('9042', '1', '1', '1/1/1', '1 A.M', '1 A.M', '1', '1', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `ID` varchar(6) NOT NULL,
  `fecha_entrada` varchar(15) NOT NULL,
  `Hora_Salida` varchar(15) NOT NULL,
  `Hora_entrada` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registros`
--

INSERT INTO `registros` (`ID`, `fecha_entrada`, `Hora_Salida`, `Hora_entrada`) VALUES
('9042', '123', '456', '789'),
('9042', '987', '654', '321'),
('6703', '111', '222', '333'),
('6011', '22/10/2023', '', '09:07 PM'),
('6011', '22/10/2023', '', '09:16 PM'),
('7486', '22/10/2023', '', '09:58 PM');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`Identificación`),
  ADD KEY `Identificación` (`Identificación`);

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD KEY `ID` (`ID`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `registros`
--
ALTER TABLE `registros`
  ADD CONSTRAINT `registros_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `empleados` (`Identificación`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
