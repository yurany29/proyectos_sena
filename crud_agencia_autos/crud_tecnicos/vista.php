<?php
if(!empty($_GET['codigo_tecnico'])){
	//Credenciales de conexion 
	$Local = 'localhost';
	$Usuario = 'root';
	$Contra = '';
	$Nombrebd = 'taller_de_vehiculos';

	//Crear conexion mysql
	$db = new mysqli($Local, $Usuario, $Contra, $Nombrebd);

	//revisar conexion
	if($db->connect_error){
		die("Connection failed: " . $db->connect_error);
	}

	//Extraer imagen de la BD mediante get
	$result = $db->query("SELECT * FROM tecnicos WHERE codigo_tecnico = {$_GET['codigo_tecnico']}");

	if($result->num_rows > 0){
		$imgDatos = $result->fetch_assoc();

		//Mostrar Imagen 
		header("Content-type: image/jpeg");
		echo $imgDatos['imagen_tecnico'];
	}else{
		echo 'Imagen no existe...';
	}
}
?>