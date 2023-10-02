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
    <link href="css/style_index.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>CREANDO EL CRUD CONCESIONARIO</title>  <!--Titulo de la pagina-->
</head>


<body>
	<div class="tabla-vehiculo">
		<h2>Vehiculos registrados</h2>
		<table>
			<thead>
				<tr>
					<th>Placa</th>
					<th>Marca</th>
					<th>Modelo</th>
					<th>Color</th>
					<th>Kilómetros</th>
					<th>No. motor</th>
					<th>No. chasis</th>
					<th>Consulta</th>
					
				</tr>
			</thead>
			<tbody>
				<?php while ($row = mysqli_fetch_array($consultar)): ?>
					<tr>
						<td><?= $row['placa'] ?></td>
						<td><?= $row['marca'] ?></td>
						<td><?= $row['modelo'] ?></td>
						<td><?= $row['color'] ?></td>
						<td><?= $row['kms'] ?></td>
						<td><?= $row['no_motor'] ?></td>
						<td><?= $row['no_chasis'] ?></td>
						<td><a href="consulta.php?placa=<?= $row['placa'] ?>" class="btn consult-btn">Consulta</a></td>
						
					</tr>
				<?php endwhile; ?>
			</tbody>
		</table>
		<a href="../menu.php" class="menu-button">Volver al Menú</a>
		<a href="registro.php" class="btn create-btn">Registrar vehículo</a>
    </div>
</body>
</html>