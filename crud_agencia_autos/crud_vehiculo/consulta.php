<?php
include("conexion.php");
$conectar = connection();

$placa = $_GET["placa"];
$bd_sql = "SELECT * FROM vehiculo WHERE placa='$placa'";
$consultar = mysqli_query($conectar, $bd_sql);
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
    <link href="css/styleconsulta.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>CONSULTA VEHICULO</title>  <!--Titulo de la pagina-->
</head>

<body>
	<div class="container">
		<h2>Consulta de vehiculos Registrados</h2>
		<table>
			<thead>
				<tr>
					<th>Placa</th>
					<th>Marca</th>
					<th>Modelo</th>
					<th>Color</th>
					<th>Kms</th>
					<th>No.motor</th>
					<th>No.chasis</th>
					<th></th>
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
						<td>
							<a href="actualizar.php?placa=<?= $row['placa'] ?>" class="btn edit-btn">Editar</a>
							<a href="delete.php?placa=<?= $row['placa'] ?>" class="btn delete-btn" >Eliminar</a>
						</td>
					</tr>
				<?php endwhile; ?>
			</tbody>
		</table>
		<br>
		<input type="button" class="menu-button"  onclick="window.location.href='index.php';" value="Menu"/>

	</div>
</body>
</html>