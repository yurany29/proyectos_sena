<?php
	include("conexion.php"); //coneccion con el archivo php
	$conectar = connection(); //Se alberga en la variable la funcion encontrada en el archivo php

	$busqueda = "SELECT * FROM vehiculo"; //sel alberga en la variable la busqueda de los usuarios
	$consultar = mysqli_query($conectar, $busqueda); //Se alberga en la variable la base de datos
?>


<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8"> <!--Permite ingresar un set de caracteres-->
	<meta http-equiv="X-UA-Compatible" content="IE=edge"> <!--Permite que sea compatible con el navegador de internet explorer-->
	<meta name="viewport" content="width=device-width, initial-scale=1.0"> <!--Permite ajustarse al dispositivo-->
	<meta name="description" content="Este es un registro de CRUD"/> <!--Descripcion asisgnada a la pagina-->
    <meta name="keywords" content="registro, CRUD, base de datos, vehiculo"/> <!--Palabras claves para mejorar la busqueda de la página-->
    <meta name="author" content="Yurany Henao"> <!--Nombre del autor de la pagina-->
    <link rel="shortcut icon" href=""> <!--Permite añadirle un icono a la pagina-->
    <link href="css/styleregistro.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>REGISTRO DE VEHICULOS</title>  <!--Titulo de la pagina-->
</head>


<body>
	<div class="vehiculo-form">
		<h2>Registrar Vehiculo</h2>
		<form action="insertar.php" method="POST">
			<div class="form-group">
				<label for="placa">Placa:</label>
				<input type="text" id="placa" name="placa" placeholder="Placa" required>
			</div>
			<div class="form-group">
				<label for="marca">Marca:</label>
				<input type="text" id="marca" name="marca" placeholder="Marca" required>
			</div>
			<div class="form-group">
				<label for="modelo">Modelo:</label>	
				<input type="text" id="modelo" name="modelo" placeholder="Modelo" required>
			</div>
			<div class="form-group">
				<label for="color">Color:</label>	
				<input type="text" id="color" name="color" placeholder="Color" required>
			</div>
			<div class="form-group">
				<label for="kms">Kms:</label>	
				<input type="text" id="kms" name="kms" placeholder="Kms" required>
			</div>
			<div class="form-group">
				<label for="no_motor">No_Motor:</label>	
				<input type="text" id="no_motor" name="no_motor" placeholder="No_motor" required>
			</div>
			<div class="form-group">
				<label for="no_chasis">No_Chasis:</label>	
				<input type="text" id="no_chasis" name="no_chasis" placeholder="No_chasis" required>
			</div>
			<div class="form-group-btn">
				<input type="submit" value="Agregar" class="btn add-btn">
				<button type="button" class="btn cancel-btn" onclick="window.location.href='index.php';">Cancelar</button>
			</div>
		</form>
		
		
	</div>
</body>
</html>
