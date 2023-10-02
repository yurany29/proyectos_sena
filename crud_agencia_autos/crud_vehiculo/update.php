<?php
include("conexion.php");
$conectar = connection();



$placa = $_POST['placa'];
$marca = $_POST['marca'];
$modelo = $_POST['modelo'];
$color = $_POST['color'];
$kms = $_POST['kms'];
$no_motor = $_POST['no_motor'];
$no_chasis = $_POST['no_chasis'];


$bd_sql = "UPDATE vehiculo SET marca='$marca',  modelo='$modelo', color='$color', kms='$kms',  no_motor='$no_motor',  no_chasis='$no_chasis' WHERE placa='$placa'";
$consultar = mysqli_query($conectar, $bd_sql);

if($consultar){
	Header("Location: index.php");
}else{

}
?>

<!-- CUIDADITO SULIBAN -->
<!-- jejejejje-->