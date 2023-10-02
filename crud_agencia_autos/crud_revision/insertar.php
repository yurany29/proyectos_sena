<?php
include("conexion.php"); //llama la coneccion
$conectar = connection(); //llama la funcion

$numero_revision = null; //pide un id nulo
$fecha_revision = $_POST['fecha_revision']; //trae los valores del archivo index
$descripcion_revision = $_POST['descripcion_revision']; //trae los valores del archivo index
$tecnico_encargado = $_POST['tecnico_encargado']; //trae los valores del archivo index
$tiempo_de_revision = $_POST['tiempo_de_revision']; //trae los valores del archivo index
$valor_de_revision = $_POST['valor_de_revision']; //trae los valores del archivo index

$bd_sql = "INSERT INTO revision VALUES('$numero_revision ','$fecha_revision','$descripcion_revision','$tecnico_encargado','$tiempo_de_revision','$valor_de_revision')"; //inserta las variables en la tabla

$consultar = mysqli_query($conectar, $bd_sql); //pone los valores en la BD

if($consultar){
	header("Location: index.php"); //si se cumple se devuelve al inicio
	exit;
}else{

}
?>