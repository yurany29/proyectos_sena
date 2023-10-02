<?php

function connection(){ 
    $local = "localhost";
    $usuario = "root";
    $password = "";
    
    //Se declara la variable que tiene como valor la base de datos.
    $base_de_datos = "taller_de_vehiculos";

    //Se realiza la conexion con la base de datos
    $conect = mysqli_connect($local, $usuario, $password);
    mysqli_select_db($conect, $base_de_datos);
    return $conect;
}
