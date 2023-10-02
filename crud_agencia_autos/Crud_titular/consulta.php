<?php 

// Hacer conexion con la base de datos
include("conexion.php");

//Hacer el llamado de la funcion connection
$conect = connection();
$cedula = $_GET["cedula_titular"];

//Se selecciona la tabla titular
$search = "SELECT * FROM titular WHERE cedula_titular='$cedula'";

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
	<meta name="description" content="Consulta datos de base usuarios">
	<!--Palabras clave para la busqueda de la pagina-->
	<meta name="keywords" content="html, css, bases de datos, php"/>
	<!--Se define el autor de la pagina-->
	<meta name="author" content="Aprendices" />
	<meta name="copyright" content="Aprendices" />
	<!--Conexion con el estilo-->
	<link href="css/estiloconsultar.css" rel="stylesheet">
	<!--Titulo de la pagina-->
	<title>CONSULTA TITULARES</title>
</head>
<body>
	<!--Clase que identifica la tabla titular-->
	<div class="container">
		<!--Titulo de nivel 2 -->
		<h2>Consulta de Titulares Registrados</h2>
		<!--Estructura de la tabla-->
		<table>
			<thead>
				<tr>
					<!--Campos de la tabla-->
					<th>Cedula Titular</th>
					<th>Nombre Titular</th>
					<th>Direccion Titular</th>
					<th>Telefono Titular</th>
					<th>Movil Titular</th>
					<th></th>
					
				</tr>
			</thead>
			<tbody>
				<?php while ($row = mysqli_fetch_array($peticion)): ?>
					<tr>
						<!--Se muestran los datos ingresados en la tabla-->
						<td><?= $row['cedula_titular'] ?></td>
						<td><?= $row['nombre_titular'] ?></td>
						<td><?= $row['direccion_titular'] ?></td>
						<td><?= $row['telefono_titular'] ?></td>
						<td><?= $row['movil_titular'] ?></td> 
						<!--Boton de actualizar-->
						<td><a href="actualizar.php?cedula_titular=<?= $row['cedula_titular'] ?>"class="btn edit-btn">Editar Titular</a>
						<!--Boton de eliminar-->
						<a href="delete.php?cedula_titular=<?= $row['cedula_titular'] ?>"class="btn delete-btn">Eliminar Titular</a></td>
					</tr>
				<?php endwhile; ?>
			</tbody>
		</table>
		<br>
					<!--Boton para volver al menu-->
		<input type="button" class="menu-button" onclick="window.location.href='index.php';" value="Menu"/>

	</div>
	
</body>
</html>
