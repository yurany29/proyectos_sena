<?php

function connection(){
	$sitio = "localhost";
	$vehiculo = "root";
	$placa = "";

	$data_base = "taller_de_vehiculos";

	$conectar = mysqli_connect($sitio, $vehiculo, $placa);

	mysqli_select_db($conectar, $data_base);

	return $conectar;
}
?>