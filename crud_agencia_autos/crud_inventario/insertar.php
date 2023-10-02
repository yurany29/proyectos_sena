<?php

// Hacer conexion con la base de datos
include("conexion.php"); 

//Hacer el llamado de la funcion connection
$conect = connection(); 

//Se declaran las variables con los datos ingresados
$id_inventario = null;
$gato = $_POST['gato'];
$cruceta = $_POST['cruceta'];
$botiquin = $_POST['botiquin'];
$radio = $_POST['radio'];
$observaciones = $_POST['observaciones'];


//Se insertan los datos en la tabla inventario_vehiculo.
$search = "INSERT INTO inventario_de_vehiculo VALUES('$id_inventario', '$gato', '$cruceta', '$botiquin', '$radio', '$observaciones')";

//Pone los valores en la base de datos
$peticion = mysqli_query($conect, $search);  


//Si se cumple se devuelve al inicio 
if($peticion){
	header("Location: index.php");
	exit;
}else{

}

?> 