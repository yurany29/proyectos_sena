<?php

// Hacer conexion con la base de datos
include("conexion.php"); 

//Hacer el llamado de la funcion connection
$conect = connection(); 

//Realiza la busqueda de los titulares en la base de datos
$search = "SELECT * FROM titular"; 

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
    <meta name="description" content="Este es un registro de un CRUD"/>
    <!--Palabras clave para la busqueda de la pagina-->
    <meta name="keywords" content="nombre, registro, usuarios"/>
    <!--Se define el autor de la pagina-->
    <meta name="author" content="Jhon Faver Alvarez">
    <meta name="copyright" content="Aprendices">
    <!--Permite añadir un icono a la pestaña-->
    <link rel="shortcut icon" href="">
    <!--Conexion con el estilo-->
    <link  href="css/estilocrear.css" rel="stylesheet">
    <!--Titulo de la pagina-->
    <title>CREAR NUEVO TITULAR</title>
</head>
<body>
    <!--Clase que identifica la informacion titular-->
    <div class="container">
        <h2>Crear Titular</h2>
        <!--Conexion con el archivo insertar.php para insertar los datos-->
        <form action="insertar.php" method="POST">
            <div class="form-group">
                <label for="cedula_titular">Cedula:</label>
                <input type="text" id="cedula_titular" name="cedula_titular" placeholder="Cedula Titular" required>
            </div>
            <div class="form-group">
                <label for="nombre_titular">Nombre:</label> 
                <input type="text" id="nombre_titular" name="nombre_titular" placeholder="Nombre Titular" required>
            </div>
            <div class="form-group">
                <label for="direccion_titular">Direccion:</label>    
                <input type="text" id="direccion_titular" name="direccion_titular" placeholder="Direccion Titular" required>
            </div>
            <div class="form-group">
                <label for="telefono_titular">Telefono:</label>    
                <input type="text" id="telefono_titular" name="telefono_titular" placeholder="Telefono Titular" required>
            </div>
            <div class="form-group"> 
                <label for="movil_titular">Movil:</label>   
                <input type="text" id="movil_titular" name="movil_titular" placeholder="Movil Titular" required>
            </div>
            <div class="form-group-btn">    
                <input type="submit"  value="Agregar" class="btn add-btn">
                <button type="button" class="btn cancel-btn" onclick="window.location.href='index.php';">Cancelar</button>
            </div>
        </form>
    </div>
</body>
</html>
