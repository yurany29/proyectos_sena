<?php
	include("conexion.php"); //coneccion con el archivo php
	$conectar = connection(); //Se alberga en la variable la funcion encontrada en el archivo php

	$busqueda = "SELECT * FROM revision"; //sel alberga en la variable la busqueda de los usuarios
	$consultar = mysqli_query($conectar, $busqueda); //Se alberga en la variable la base de datos
?>

<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8"> <!--Permite ingresar un set de caracteres-->
	<meta http-equiv="X-UA-Compatible" content="IE=edge"> <!--Permite que sea compatible con el navegador de internet explorer-->
	<meta name="viewport" content="width=device-width, initial-scale=1.0"> <!--Permite ajustarse al dispositivo-->
	<meta name="description" content="Este es un registro de CRUD"/> <!--Descripcion asisgnada a la pagina-->
    <meta name="keywords" content="registro, CRUD, base de datos, revision"/> <!--Palabras claves para mejorar la busqueda de la página-->
    <meta name="author" content="Yurany Henao"> <!--Nombre del autor de la pagina-->
    <link rel="shortcut icon" href=""> <!--Permite añadirle un icono a la pagina-->
    <link href="css/estiloregistrar.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>REGISTRAR LA REVISION</title>  <!--Titulo de la pagina-->
</head>


<body>
	<div class="container">
		<h2>Registrar revision</h2>
		<form action="insertar.php" method="POST">
			<div class="form-group">
				<label for="fecha_revision">Fecha revisión:</label>
				<input type="text" id="fecha_revision" name="fecha_revision" placeholder="Fecha AAAA/MM/DD" required>
			</div>
			<div class="form-group">
				<label for="descripcion_revision">Descripcion de la revisión:</label>
				<input type="text" id="descripcion_revision" name="descripcion_revision" placeholder="Descripcion de la revisión" required>
			</div>
			<div class="form-group">
				<label for="tecnico_encargado">Tecnico encargado:</label>
				<input type="text" id="tecnico_encargado" name="tecnico_encargado" placeholder="Tecnico encargado" required>
			</div>
			<div class="form-group">
				<label for="tiempo_de_revision">Tiempo de revisión:</label>
				<input type="text" id="tiempo_de_revision" name="tiempo_de_revision" placeholder="Tiempo de revisión" required>
			</div>
			<div class="form-group">
				<label for="valor_de_revision">Valor de revisión:</label>
				<input type="text" id="valor_de_revision" name="valor_de_revision" placeholder="Valor de revisión" required>
			</div> 
			<div class="form-group">
				<input type="submit" value="Agregar" class="btn add-btn">
				<button type="button" class="btn cancel-btn" onclick="window.location.href='index.php';">Cancelar</button>
			</div>
		</form>
	</div>
</body>
</html>