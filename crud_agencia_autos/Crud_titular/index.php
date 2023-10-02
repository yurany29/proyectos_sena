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
    <link  href="css/estiloindex.css" rel="stylesheet">
     <!--Titulo de la pagina-->
    <title>INFORMACION TITULAR</title>
</head>
<body>

    <!--Clase que identifica la tabla titular-->
    <div class="container">
        <!--Titulo de nivel 2 -->
        <h2>Titulares Registrados</h2>
        <!--Boton para crear titulares-->
        
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
                    <th>Acciones</th>       
                </tr>
            </thead>
            <tbody>
                <?php while ($row = mysqli_fetch_array($peticion)): ?>
                    <tr>
                        <!--Se agregan los datos ingresados en la tabla-->
                        <td><?= $row['cedula_titular'] ?></td>
                        <td><?= $row['nombre_titular'] ?></td>
                        <td><?= $row['direccion_titular'] ?></td>
                        <td><?= $row['telefono_titular'] ?></td>
                        <td><?= $row['movil_titular'] ?></td>
                    
                        <!--Boton de consulta-->
                        <td><a href="consulta.php?cedula_titular=<?= $row['cedula_titular'] ?>" class="btn consult-btn">Consulta Titular</a></td>
                    </tr>
                <?php endwhile;?>
            </tbody>
        </table>
        <input type="button" class="menu-button" onclick="window.location.href='../menu.php';" value="Menú"/>
        <a href="crear.php" class="btn create-btn">Crear Titular</a>
    </div>
</body>
</html>
