<?php

// Hacer conexion con la base de datos
include("conexion.php");

//Hacer el llamado de la funcion connection
$conect = connection();

//Se declaran las variables con los datos ingresados
$cedula_titular =$_POST['cedula_titular'];
$nombre_titular = $_POST['nombre_titular'];
$direccion_titular = $_POST['direccion_titular'];
$telefono_titular = $_POST['telefono_titular'];
$movil_titular = $_POST['movil_titular'];


//Se actualizan los datos en la tabla titular.
$search = "UPDATE titular SET nombre_titular='$nombre_titular', direccion_titular='$direccion_titular', telefono_titular='$telefono_titular', movil_titular='$movil_titular' WHERE cedula_titular='$cedula_titular'";

//Pone los valores en la base de datos
$peticion = mysqli_query($conect, $search);


//Si se cumple se devuelve al inicio 
if($peticion){
	Header("Location: index.php");

}else{

}

?> 