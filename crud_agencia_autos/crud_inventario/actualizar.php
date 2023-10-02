<?php
	
	// Hacer conexion con la base de datos
	include("conexion.php");

	//Hacer el llamado de la funcion connection
	$conect =connection();

	//Se declara la variable con el valor del id_inventario
	$id_inventario=(isset ($_GET['id_inventario']));

	//Se selecciona de la tabla inventario_de_vehiculo el id_inventario ingresado
	$search="SELECT * FROM inventario_de_vehiculo WHERE id_inventario='$id_inventario'";

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
		<link href="css/estilo_actualizar.css" rel="stylesheet">
		<!--Titulo de la pagina-->
		<title>Editar Inventario de Equipo de Carretera</title>
	</head>
	<body>
	
		<!--Clase que identifica la informacion inventario-->
		<div class="inventario-form">
			<h2>Actualizar inventario</h2>
			<!--Conexion con el archivo update.php para hacer la actualizacion de los datos-->
			<form action="update.php" method="POST">
				<input type="hidden" name="id_inventario" value="<?= (isset($row['id_inventario']))?>">
				<div class="grupo-form">
                	<label for="gato">gato:</label>
					<input type="text" name="gato" placeholder="Gato" value="<?= (isset($row['gato']))?>">
				</div>
				<div class="grupo-form">
                	<label for="cruceta">cruceta:</label>
					<input type="text" name="cruceta" placeholder="Cruceta" value="<?= (isset($row['cruceta']))?>">
				</div>
				<div class="grupo-form">
                	<label for="botiquin">botiquin:</label>
					<input type="text" name="botiquin" placeholder="Botiquin" value="<?= (isset($row['botiquin']))?>">
				</div>
				<div class="grupo-form">
                	<label for="radio">radio:</label>
					<input type="text" name="radio" placeholder="Radio" value="<?= (isset($row['radio']))?>">
				</div>
				<div class="grupo-form">
                	<label for="observaciones">Observaciones:</label>
					<input type="text" name="observaciones" placeholder="Observaciones" value="<?= (isset($row['observaciones']))?>">
				</div>
				<div class="grupo-form">
					<input type="submit" value="Actualizar">
				</div>
				<div class="grupo-form">
					<!--Boton para volver al menu-->
					<input type="button" class="menu-button" onclick="window.location.href='index.php';" value="Atras" />
				</div>
			</form>
		</div>	
	</body>
</html>
