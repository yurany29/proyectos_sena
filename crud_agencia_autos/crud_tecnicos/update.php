<?php
include("conexion.php");
$connect = connection();

$codigo = $_POST['codigo_tecnico']; 
$cedula = $_POST['cedula_tecnico'];
$nombre = $_POST['nombre_tecnico'];
$direccion = $_POST['direccion_tecnico'];
$telefono = $_POST['telefono_tecnico'];
$imagen_tecnico = $_POST['imagen_tecnico'];

$actualizar = "UPDATE tecnicos SET cedula_tecnico='$cedula', nombre_tecnico='$nombre', direccion_tecnico='$direccion', telefono_tecnico='$telefono', imagen_tecnico='$imagen_tecnico' WHERE codigo_tecnico='$codigo'";
$solicitud = mysqli_query($connect, $actualizar);

if ($solicitud){
    header("Location: index.php"); // Redirecciona a la página principal después de la actualización exitosa
    exit(); // Importante para detener la ejecución después de redirigir
} else {
    echo "Error al actualizar los datos: " . mysqli_error($connect); // Imprime el error si la actualización falla
}

mysqli_close($connect);
?>