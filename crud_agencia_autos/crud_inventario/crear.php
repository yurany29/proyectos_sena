<?php

// Hacer conexion con la base de datos
include("conexion.php"); 

//Hacer el llamado de la funcion connection
$conect = connection(); 

//Realiza la busqueda de los inventarios del vehiculo en la base de datos
$search = "SELECT * FROM inventario_de_vehiculo"; 

// Realizar la solicitud a la base de datos
$peticion = mysqli_query($conect, $search); 
?>

<!--Estructura HTML-->
<!DOCTYPE html>
<!--Pagina en idioma ingles-->
<html lang="en">
<head>
    <!--Permite utilizar caracteres especiales-->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Permite ajustarse-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--Descripcion asignada a la pagina-->
    <meta name="description" content="Este es el registro de un inventario"/>
    <!--Palabras clave para la busqueda de la pagina-->
    <meta name="keywords" content="nombre, registro, inventario"/>
    <!--Se define el autor de la pagina-->
    <meta name="author" content="Jhon Faver Alvarez">
    <meta name="copyright" content="Aprendices">
    <!--Permite añadir un icono a la pestaña-->
    <link rel="shortcut icon" href="">
    <!--Conexion con el estilo-->
    <link  href="css/estilo_crear.css" rel="stylesheet">
    <!--Titulo de la pagina-->
    <title>CREAR NUEVO INVENTARIO DE EQUIPO DE CARRETERA</title>
</head>
<body>
    <!--Clase que identifica la informacion inventario-->
    <div class="container">
        <h2>Crear Inventario</h2>
        <!--Conexion con el archivo insertar.php para insertar los datos-->
        <form action="insertar.php" method="POST">
            <div class="form-group">
                <label for="gato">gato:</label>
                <input type="text" name="gato" placeholder="Gato">
            </div>
            <div class="form-group">
                <label for="cruceta">cruceta:</label>
                <input type="text" name="cruceta" placeholder="Cruceta">
            </div>
            <div class="form-group">
                <label for="botiquin">botiquin:</label>
                <input type="text" name="botiquin" placeholder="Botiquin">
            </div>
            <div class="form-group">
                <label for="radio">radio</label>
                <input type="text" name="radio" placeholder="Radio">
            </div>
            <div class="form-group">
                <label for="observaciones">observaciones</label>
                <input type="text" name="observaciones" placeholder="Observaciones">
            </div>
            <div class="form-group">
                <input type="submit" value="Agregar" class="btn add-btn">
                <button type="button" class="btn cancel-btn" onclick="window.location.href='index.php';">Cancelar</button>
            <div>
        </form>
    </div>
</body>
</html>