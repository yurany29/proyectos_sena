<?php
	include("conexion.php");
	$conectar = connection();

	$numero_revision = $_GET['numero_revision'];

	$bd_sql = "SELECT * FROM revision WHERE numero_revision='$numero_revision'";
	$consultar = mysqli_query($conectar, $bd_sql);

	$row = mysqli_fetch_array($consultar);
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
    <link href="css/estilo_actualizar_revision.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>REVISION DE LOS VEHICULOS</title>  <!--Titulo de la pagina-->
</head>
<body>
	<div class="container">
		<h2>Editar revisiones</h2>
		<form action="update.php" method="POST">
			<input type="hidden" name="numero_revision" value="<?= $row['numero_revision'] ?>">
			<div class="form-group">
				<label for="fecha_revision">Fecha de revision: </label>
				<input type="text" name="fecha_revision" id="fecha_revision" placeholder="Fecha de revision" value="<?= $row['fecha_revision'] ?>">
			</div>
			<div class="form-group">
				<label for="descripcion_revision">Descripcion revision: </label>
				<input type="text" name="descripcion_revision" id="descripcion_revision" placeholder="Descripcion de la revision" value="<?= $row['descripcion_revision'] ?>">
			</div>
			<div class="form-group">
				<label for="tecnico_encargado">Tecnico encargado: </label>
				<input type="text" name="tecnico_encargado" id="tecnico_encargado" placeholder="Tecnico encargado" value="<?= $row['tecnico_encargado'] ?>">
			</div>
			<div class="form-group">
				<label for="tiempo_de_revision">Tiempo de revision: </label>
				<input type="text" name="tiempo_de_revision" id="tiempo_de_revision" placeholder="Tiempo de revision" value="<?= $row['tiempo_de_revision'] ?>">
			</div>
			<div class="form-group">
				<label for="valor_de_revision">Valor de revision: </label>
				<input type="text" name="valor_de_revision" id="valor_de_revision" placeholder="Valor de revision" value="<?= $row['valor_de_revision'] ?>">
			</div>
			<div class="form-group">
				<input type="submit" value="Actualizar">
			</div>
			<div class="form-group">
                <input type="button" class="menu-button" onclick="window.location.href='consulta.php?numero_revision=<?= $row['numero_revision'] ?>';" value="Atrás">
            </div>
		</form>
	</div>
</body>
</html>