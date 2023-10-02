<?php
include("conexion.php");
$conectar = connection();
$numero = $_GET["numero_revision"];

$bd_sql = "SELECT * FROM revision WHERE numero_revision='$numero'";
$consultar = mysqli_query($conectar, $bd_sql);
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
    <link href="css/estilo_consulta.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>CONSULTA DE LA REVISION</title>  <!--Titulo de la pagina-->
</head>

<body>
	<div class="container">
		<h2>Consulta de revisiones realizadas</h2>
		<table>
			<thead>
				<tr>
					<th>Numero revision</th>
					<th>Fecha revision</th>
					<th>Descripcion revision</th>
					<th>tecnico encargado</th>
					<th>Tiempo de revision</th>
					<th>Valor de revision</th>
					<th>Acciones</th>
				</tr>
				<br>
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
						<td>
							<div class="btn-container">
								<a href="actualizar.php?numero_revision=<?= $row['numero_revision'] ?>" class="btn edit-btn">Editar</a>

								<a href="delete.php?numero_revision=<?= $row['numero_revision'] ?>" class="btn delete-btn">Eliminar</a>
							</div>
						</td>
					</tr>
				<?php endwhile; ?>
			</tbody>
		</table>
		<br>
		<input type="button" class="menu-button" onclick="window.location.href='index.php';" value="Atras"/>
	</div>
</body>
</html>