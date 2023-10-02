<?php

function connection(){
    $local = "localhost";
    $usuario = "root";
    $password = "";
    
    $base_de_datos = "taller_de_vehiculos";

    $conector = mysqli_connect($local, $usuario, $password);
    mysqli_select_db($conector, $base_de_datos);
    return $conector;
}
