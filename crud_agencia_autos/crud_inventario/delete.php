<?php

// Hacer conexion con la base de datos
include("conexion.php");

//Hacer el llamado de la funcion connection
$conect = connection();

//Se declara la variable con el valor del id_inventario
$id_inventario=$_GET["id_inventario"];

//Se selecciona en la tabla inventario_de_vehiculo el id_inventario ingresado para eliminarlo.
$search="DELETE FROM inventario_de_vehiculo WHERE id_inventario='$id_inventario'";
$peticion = mysqli_query($conect, $search);

//Si se cumple se devuelve al inicio 
if($peticion){
	Header("Location: index.php");
}else{

}

?> 