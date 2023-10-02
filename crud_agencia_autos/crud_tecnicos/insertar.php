<?php
if(isset($_POST["submit"])){

    $codigo = NULL;
    $cedula = $_POST['cedula_tecnico'];
    $nombre = $_POST['nombre_tecnico'];
    $direccion = $_POST['direccion_tecnico'];
    $telefono = $_POST['telefono_tecnico'];
    
		$imagen_tecnico = $_POST['imagen_tecnico'];

        $Local = 'localhost';
		$Usuario = 'root';
		$Contra = '';
		$Nombrebd = 'taller_de_vehiculos';

        //Crear conexion con la base de datos
		$db = new mysqli($Local, $Usuario, $Contra, $Nombrebd);

        if($db->connect_error){
            die("Connection failed: " . $db->connect_error);
        }
        $insertar = $db->query("INSERT INTO tecnicos ( codigo_tecnico, cedula_tecnico, nombre_tecnico, direccion_tecnico, telefono_tecnico, imagen_tecnico) VALUES ('$codigo', '$cedula', '$nombre', '$direccion', '$telefono', '$imagen_tecnico')");
        if($insertar){
            echo "Archivo subido correctamente";
        }else{
            echo "Ha fallado la subida del archivo ";
        } 


    }else{
        echo "Seleccione una imagen ";
    }


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilos/estiloconsulta.css">
</head>
<body>
    <input type="button" class="menu-button" onclick="window.location.href='index.php';" value="Atras" />
</body>
</html>