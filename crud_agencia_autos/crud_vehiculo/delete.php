<?php

include("conexion.php");
$conectar = connection();

$placa = $_GET["placa"];

$bd_sql = "DELETE FROM vehiculo WHERE placa='$placa'";
$consultar = mysqli_query($conectar, $bd_sql);

if($consultar){
	Header("Location: index.php");
}else{

}
?>