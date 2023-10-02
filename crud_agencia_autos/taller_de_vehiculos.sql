-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-09-2023 a las 03:04:21
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `taller_de_vehiculos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_de_vehiculo`
--

CREATE TABLE `inventario_de_vehiculo` (
  `id_inventario` int(11) NOT NULL,
  `gato` varchar(3) NOT NULL,
  `cruceta` varchar(3) NOT NULL,
  `botiquin` varchar(3) NOT NULL,
  `radio` varchar(3) NOT NULL,
  `observaciones` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventario_de_vehiculo`
--

INSERT INTO `inventario_de_vehiculo` (`id_inventario`, `gato`, `cruceta`, `botiquin`, `radio`, `observaciones`) VALUES
(1, '1', '1', 'si', 'no', 'si'),
(3, '1', '1', '1', '1', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `revision`
--

CREATE TABLE `revision` (
  `numero_revision` int(11) NOT NULL,
  `fecha_revision` date NOT NULL,
  `descripcion_revision` varchar(100) NOT NULL,
  `tecnico_encargado` varchar(25) NOT NULL,
  `tiempo_de_revision` varchar(20) NOT NULL,
  `valor_de_revision` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `revision`
--

INSERT INTO `revision` (`numero_revision`, `fecha_revision`, `descripcion_revision`, `tecnico_encargado`, `tiempo_de_revision`, `valor_de_revision`) VALUES
(1, '2023-02-12', 'se le cayo la llanta', 'Juan Jose ', '3 horas', '6000'),
(2, '0000-00-00', 'Sapo', 'Faver', '12 horas', '6000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tecnicos`
--

CREATE TABLE `tecnicos` (
  `codigo_tecnico` int(11) NOT NULL,
  `cedula_tecnico` int(12) NOT NULL,
  `nombre_tecnico` varchar(25) NOT NULL,
  `direccion_tecnico` varchar(50) NOT NULL,
  `telefono_tecnico` varchar(14) NOT NULL,
  `imagen_tecnico` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tecnicos`
--

INSERT INTO `tecnicos` (`codigo_tecnico`, `cedula_tecnico`, `nombre_tecnico`, `direccion_tecnico`, `telefono_tecnico`, `imagen_tecnico`) VALUES
(5, 123456, 'este', 'eso mismos', '789', 0x6761746f322e6a7067),
(6, 111, '1', '1', '1', 0x576861747341707020496d61676520323032332d30392d31342061742031302e34342e333020414d2e6a706567),
(7, 3, '3', '3', '3', 0x6465736361726761202832292e6a7067);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `titular`
--

CREATE TABLE `titular` (
  `cedula_titular` int(12) NOT NULL,
  `nombre_titular` varchar(25) NOT NULL,
  `direccion_titular` varchar(50) NOT NULL,
  `telefono_titular` varchar(14) NOT NULL,
  `movil_titular` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `titular`
--

INSERT INTO `titular` (`cedula_titular`, `nombre_titular`, `direccion_titular`, `telefono_titular`, `movil_titular`) VALUES
(1, '1', '1', '1', '1'),
(2, '2', '2', '2', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo`
--

CREATE TABLE `vehiculo` (
  `placa` varchar(8) NOT NULL,
  `marca` varchar(25) NOT NULL,
  `modelo` varchar(20) NOT NULL,
  `color` varchar(10) NOT NULL,
  `kms` varchar(9) NOT NULL,
  `no_motor` varchar(10) NOT NULL,
  `no_chasis` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculo`
--

INSERT INTO `vehiculo` (`placa`, `marca`, `modelo`, `color`, `kms`, `no_motor`, `no_chasis`) VALUES
('ASD123', 'Tesla', '2022', 'Negro', '0', '2121j', '21211'),
('ASD320', 'SPARK GT', '2021', 'Blanco', '2km', '4569885', '888452'),
('MKL321', 'Mazda', '2020', 'Rojo', '0', '321213', '312313');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `inventario_de_vehiculo`
--
ALTER TABLE `inventario_de_vehiculo`
  ADD PRIMARY KEY (`id_inventario`);

--
-- Indices de la tabla `revision`
--
ALTER TABLE `revision`
  ADD PRIMARY KEY (`numero_revision`);

--
-- Indices de la tabla `tecnicos`
--
ALTER TABLE `tecnicos`
  ADD PRIMARY KEY (`codigo_tecnico`);

--
-- Indices de la tabla `titular`
--
ALTER TABLE `titular`
  ADD PRIMARY KEY (`cedula_titular`);

--
-- Indices de la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD PRIMARY KEY (`placa`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `inventario_de_vehiculo`
--
ALTER TABLE `inventario_de_vehiculo`
  MODIFY `id_inventario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `revision`
--
ALTER TABLE `revision`
  MODIFY `numero_revision` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tecnicos`
--
ALTER TABLE `tecnicos`
  MODIFY `codigo_tecnico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
