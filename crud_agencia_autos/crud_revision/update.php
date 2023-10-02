<?php
include("conexion.php");
$conectar = connection();

$numero_revision = $_POST['numero_revision'];
$descripcion_revision = $_POST['descripcion_revision'];
$tecnico_encargado = $_POST['tecnico_encargado'];
$tiempo_de_revision = $_POST['tiempo_de_revision'];
$valor_de_revision = $_POST['valor_de_revision'];

$bd_sql = "UPDATE revision SET descripcion_revision='$descripcion_revision', tecnico_encargado='$tecnico_encargado', tiempo_de_revision='$tiempo_de_revision', valor_de_revision='$valor_de_revision' WHERE numero_revision='$numero_revision'";
$consultar = mysqli_query($conectar, $bd_sql);

if($consultar){
	Header("Location: index.php");
}else{

}
?>