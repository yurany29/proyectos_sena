<?php
	
	// Hacer conexion con la base de datos
	include("conexion.php");

	//Hacer el llamado de la funcion connection
	$conect =connection();

	//Se declara la variable con el valor de la cedula titular
	$cedula_titular=$_GET['cedula_titular'];

	//Se selecciona en la tabla titular la cedula_titular ingresada
	$search="SELECT * FROM titular WHERE cedula_titular='$cedula_titular'";

	//Pone los valores en la base de datos
	$peticion=mysqli_query($conect, $search);
	
	$row=mysqli_fetch_array($peticion);

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
		<!--Conexion con el estilo-->
		<link href="css/estiloeditar.css" rel="stylesheet">
		<!--Titulo de la pagina-->
		<title>Editar Titulares</title>
	</head>
	<body>
	<!--Boton para volver al menu-->
	
		<!--Clase que identifica la informacion titular-->
		<div class="container">
			<h2>Editar Titular</h2>
			<!--Conexion con el archivo update.php para hacer la actualizacion de los datos-->
			<form action="update.php" method="POST">
				<input type="hidden" name="cedula_titular" value="<?= $row['cedula_titular']?>">
				<div class="form-group">
					<label for="cedula_titular">Cedula:</label>
					<input type="text" name="nombre_titular" id="nombre_titular" placeholder="Nombre Titular" value="<?= $row['nombre_titular']?>">
				<div/>
				<div class="form-group">
					<label for="direccion_titular">Direccion:</label>
					<input type="text" name="direccion_titular"  id="direccion_titular" placeholder="Direccion Titular" value="<?= $row['direccion_titular']?>">
				<div/>
				<div class="form-group">
					<label for="telefono_titular">Telefono:</label>
					<input type="text" name="telefono_titular"  id="telefono_titular" placeholder="Telefono Titular" value="<?= $row['telefono_titular']?>">
				<div/>
				<div class="form-group">
					<label for="movil">Movil:</label>
					<input type="text" name="movil_titular" id="movil_titular" placeholder="Movil Titular" value="<?= $row['movil_titular']?>">
				<div/>
				<div class="form-group">
                	<input type="submit" value="Actualizar">
				</div>
				<div class="form-group">
					<input type="button" class="menu-button" onclick="window.location.href='consulta.php?cedula_titular=<?= $row['cedula_titular'] ?>';" value="Atrás">
				</div>
			</form>
		</div>	
	</body>
</html>
