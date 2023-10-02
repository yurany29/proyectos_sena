<?php
include("conexion.php"); //llama la coneccion
$conectar = connection(); //llama la funcion

$placa = $_POST['placa']; //trae los valores del archivo index
$marca = $_POST['marca']; //trae los valores del archivo index
$modelo = $_POST['modelo']; //trae los valores del archivo index
$color = $_POST['color']; //trae los valores del archivo index
$kms = $_POST['kms']; //trae los valores del archivo index
$no_motor = $_POST['no_motor']; //trae los valores del archivo index
$no_chasis = $_POST['no_chasis']; //trae los valores del archivo index

$bd_sql = "INSERT INTO vehiculo VALUES('$placa','$marca','$modelo','$color','$kms','$no_motor','$no_chasis')"; //inserta las variables en la tabla

$consultar = mysqli_query($conectar, $bd_sql); //pone los valores en la BD

if($consultar){
	header("Location: index.php"); //si se cumple se devuelve al inicio
	exit;
}else{

}
?>