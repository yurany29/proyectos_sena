<?php

include("conexion.php");
$conectar = connection();

$numero_revision = $_GET["numero_revision"];

$bd_sql = "DELETE FROM revision WHERE numero_revision='$numero_revision'";
$consultar = mysqli_query($conectar, $bd_sql);

if($consultar){
	Header("Location: index.php");
}else{

}
?>