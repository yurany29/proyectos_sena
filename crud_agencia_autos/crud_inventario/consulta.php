<?php 

// Hacer conexion con la base de datos
include("conexion.php");

//Hacer el llamado de la funcion connection
$conect = connection();

$id = $_GET["id_inventario"];
//Se selecciona la tabla inventario_de_vehiculo
$search = "SELECT * FROM inventario_de_vehiculo WHERE id_inventario='$id'";

//Se hace la peticion a la base de datos
$peticion = mysqli_query($conect, $search);
?>

<!--Estructura HTML-->
<!DOCTYPE html>
<!--Pagina en idioma ingles-->
<html lang="en">
<head>
	<!--Permite utilizar caracteres especiales-->
	<meta charset="UTF-8">
	<!--Permite ajustarse-->
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!--Descripcion asignada a la pagina-->
	<meta name="description" content="Consulta base de datos de inventarios">
	<!--Palabras clave para la busqueda de la pagina-->
	<meta name="keywords" content="html, css, bases de datos, php, inventarios"/>
	<!--Se define el autor de la pagina-->
	<meta name="author" content="Aprendices" />
	<meta name="copyright" content="Aprendices" />
	<!--Conexion con el estilo-->
	<link href="css/estilo_consulta.css" rel="stylesheet">
	<!--Titulo de la pagina-->
	<title>CONSULTA INVENTARIO DE VEHICULO</title>
</head>
<body>
	<!--Clase que identifica la tabla inventario-->
	<div class="container">
		<!--Titulo de nivel 2 -->
		<h2>Consulta de Inventarios Registrados</h2>
		<!--Estructura de la tabla-->
		<table class="tabla-superior">
			<thead>
				<tr>
					<!--Campos de la tabla-->
					<th>ID Inventario</th>
					<th>Gato</th>
					<th>Cruceta</th>
					<th>Botiquin</th>
					<th>Radio</th>
					<th>Observaciones</th>
					<th>Acciones</th>
					
				</tr>
				<br>
					
			</thead>
			<tbody>
				<?php while ($row = mysqli_fetch_array($peticion)): ?>
					<tr>
						<!--Se muestran los datos ingresados en la tabla-->
						<td><?= $row['id_inventario'] ?></td>
						<td><?= $row['gato'] ?></td>
						<td><?= $row['cruceta'] ?></td>
						<td><?= $row['botiquin'] ?></td>
						<td><?= $row['radio'] ?></td> 
						<td><?= $row['observaciones'] ?></td>
						<!--Boton de actualizar-->
						<td><a href="actualizar.php?id_inventario=<?= $row['id_inventario'] ?>"class="btn inventario-table--edit">Editar Inventario</a>
						<!--Boton de eliminar-->
						
						<a href="delete.php?id_inventario=<?= $row['id_inventario'] ?>"class="btn inventario-table--delete">Eliminar Inventario</a></td>
					</tr>
				<?php endwhile; ?>
			</tbody>
		</table>
		<br>
		<input type="button" class="menu-button" onclick="window.location.href='index.php';" value="Atras" />
	</div>
	
</body>
</html>
