<?php

// Hacer conexion con la base de datos
include("conexion.php");

//Hacer el llamado de la funcion connection
$conect = connection();

//Se declaran las variables con los datos ingresados
$id_inventario =$_POST['id_inventario'];
$gato = $_POST['gato'];
$cruceta = $_POST['cruceta'];
$botiquin = $_POST['botiquin'];
$radio = $_POST['radio'];
$observaciones = $_POST['observaciones'];


//Se actualizan los datos en la tabla inventario_de_vehiculo.
$search = "UPDATE inventario_de_vehiculo SET gato='$gato', cruceta='$cruceta', botiquin='$botiquin', radio='$radio', observaciones='$observaciones' WHERE id_inventario='$id_inventario'";

//Pone los valores en la base de datos
$peticion = mysqli_query($conect, $search);


//Si se cumple se devuelve al inicio 
if($peticion){
	Header("Location: index.php");

}else{

}

?> 