<?php

include("../conexion.php");
$connect = connection();

$codigo = $_GET["codigo_tecnico"];

$eliminar = "DELETE FROM tecnicos WHERE codigo_tecnico = '$codigo'";
$solicitud = mysqli_query($connect, $eliminar);

if ($solicitud){
    Header("Location: index.php");
}else{

}

?>  