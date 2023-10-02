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
    <meta name="description" content="Este es un registro de un CRUD"/>
    <!--Palabras clave para la busqueda de la pagina-->
    <meta name="keywords" content="inventario, registro, vehiculo"/>
    <!--Se define el autor de la pagina-->
    <meta name="author" content="Jhon Faver Alvarez">
    <meta name="copyright" content="Aprendices">
    <!--Permite añadir un icono a la pestaña-->
    <link rel="shortcut icon" href="">
    <!--Conexion con el estilo-->
    <link  href="css/estilo_index.css" rel="stylesheet">
     <!--Titulo de la pagina-->
    <title>INFORMACION DEL EQUIPO DE CARRETERA</title>
</head>
<body>

    <!--Clase que identifica la tabla inventario-->
    <div class="inventario-table">
        <!--Titulo de nivel 2 -->
        <h2>Inventarios Registrados</h2>
        <!--Estructura de la tabla-->
        <table>
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
            </thead>
            <tbody>
            <?php while ($row = mysqli_fetch_array($peticion)): ?>
                <tr>
                    <!--Se agregan los datos ingresados en la tabla-->
                    <td><?= $row['id_inventario'] ?></td>
                    <td><?= $row['gato'] ?></td>
                    <td><?= $row['cruceta'] ?></td>
                    <td><?= $row['botiquin'] ?></td>
                    <td><?= $row['radio'] ?></td>
                    <td><?= $row['observaciones'] ?></td>
                    <!--Boton de consulta-->
                    <td><a href="consulta.php?id_inventario=<?= $row['id_inventario'] ?>" class="btn inventario-table--consult">Consulta Inventario</a></td>
                </tr>
            <?php endwhile;?>
            </tbody>
        </table>
        <input type="button" class="menu-button" onclick="window.location.href='../menu.php';" value="Menú" />
        <a href="crear.php" class="btn create-btn">Crear Inventario</a>
    </div>
</body>
</html>
