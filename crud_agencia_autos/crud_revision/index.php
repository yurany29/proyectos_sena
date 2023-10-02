<?php
	include("../conexion.php"); //coneccion con el archivo php
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
    <link href="css/estilo_index_revision.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>REGISTRAR LA REVISION</title>  <!--Titulo de la pagina-->
</head>


<body>

	<div class="container">
		<h2>Revisiones ingresadas</h2>
		<table>
			<thead>
				<tr>
					<th>Numero revision</th>
					<th>Fecha revision</th>
					<th>Descripcion revision</th>
					<th>Tecnico encargado</th>
					<th>Tiempo revision</th>
					<th>Valor revision</th>
					<th>Acciones</th>
				</tr>
			</thead>
			<tbody>
				<?php while ($row = mysqli_fetch_array($consultar)): ?>
					<tr>
						<td><?= $row['numero_revision'] ?></td>
						<td><?= $row['fecha_revision'] ?></td>
						<td><?= $row['descripcion_revision'] ?></td>
						<td><?= $row['tecnico_encargado'] ?></td>
						<td><?= $row['tiempo_de_revision'] ?></td>
						<td><?= $row['valor_de_revision'] ?></td>
						<td><a href="consulta.php?numero_revision=<?= $row['numero_revision'] ?>" class="btn consult-btn">Consulta</a></td>
					
					</tr>
				<?php endwhile; ?>
			</tbody>
		</table>
		<input type="button" class="menu-button" onclick="window.location.href='../menu.php';" value="Menú"/>
		<a href="revision.php" class="btn create-btn">Registrar revision</a>

	</div>
</body>
</html>