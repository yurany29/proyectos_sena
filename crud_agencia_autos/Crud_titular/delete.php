<?php

// Hacer conexion con la base de datos
include("conexion.php");

//Hacer el llamado de la funcion connection
$conect = connection();

//Se declara la variable con el valor de la cedula titular
$cedula_titular=$_GET["cedula_titular"];

//Se selecciona en la tabla titular la cedula_titular ingresada para eliminarla.
$search="DELETE FROM titular WHERE cedula_titular='$cedula_titular'";
$peticion = mysqli_query($conect, $search);

//Si se cumple se devuelve al inicio 
if($peticion){
	Header("Location: index.php");
}else{

}

?> 