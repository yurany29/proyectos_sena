<?php
	include("conexion.php");
	$conectar = connection();

	$placa = $_GET['placa'];

	$bd_sql = "SELECT * FROM vehiculo WHERE placa='$placa'";
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
    <meta name="keywords" content="registro, CRUD, base de datos, vehiculos"/> <!--Palabras claves para mejorar la busqueda de la página-->
    <meta name="author" content="Yurany Henao"> <!--Nombre del autor de la pagina-->
    <link rel="shortcut icon" href=""> <!--Permite añadirle un icono a la pagina-->
    <link href="css/style_actualizar.css" rel="stylesheet"> <!--Se invoca el documento css-->
    <title>vehiculos</title>  <!--Titulo de la pagina-->
</head>
<body>
	<div class="container">
		<h2>Editar Vehiculos</h2>
		<form action="update.php" method="POST">
			<input type="hidden" name="placa" id="placa" value="<?= $row['placa']?>">
			<div class="form-group">
				<label for="marca">Marca:</label>
				<input type="text" name="marca" id="marca" placeholder="Marca" value="<?= $row['marca']?>">
			</div>
			<div class="form-group">
				<label for="modelo">Modelo:</label>	
				<input type="text" name="modelo" id="modelo" placeholder="Modelo" value="<?= $row['modelo']?>">
			</div>
			<div class="form-group">
				<label for="color">Color:</label>	
				<input type="text" name="color" id="color" placeholder="Color" value="<?= $row['color']?>">
			</div>
			<div class="form-group">
				<label for="kms">Kms</label>	
				<input type="text" name="kms" id="kms" placeholder="Kms" value="<?= $row['kms']?>">
			</div>
			<div class="form-group">
				<label for="no_motor">No_motor</label>	
				<input type="text" name="no_motor" id="no_motor" placeholder="No_motor" value="<?= $row['no_motor']?>">
			</div>
			<div class="form-group">
				<label for="no_chasis">No_chasis</label>	
				<input type="text" name="no_chasis" id="no_chasis" placeholder="No_chasis" value="<?= $row['no_chasis']?>">
			</div>
			
			<div class="form-group-btn">
                <input type="submit" value="Actualizar" class="actulizar">
            
                <input type="button" class="menu-button" onclick="window.location.href='consulta.php?placa=<?= $row['placa'] ?>';" value="Atrás">
            </div>
			
		</form>
	</div>

</body>
</html>