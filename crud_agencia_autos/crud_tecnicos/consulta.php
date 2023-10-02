<?php
include("../conexion.php");

$connect = connection();

$codigo = $_GET["codigo_tecnico"];

$consulta = "SELECT * FROM tecnicos WHERE codigo_tecnico='$codigo'";
$solicitud = mysqli_query($connect, $consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilos/estiloconsulta.css">
    <title>CONSULTA TECNICO</title>
</head>
<body>
    <div class="container">
        <h2>Consulta de Técnico</h2>
        <table>
            <thead>
                <tr>
                    <th>Código</th>
                    <th>Cédula</th>
                    <th>Nombre</th>
                    <th>Dirección</th>
                    <th>Teléfono</th>
                    <th>Imagen tecnico</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php while ($row = mysqli_fetch_array($solicitud)): ?>
                    <tr>
                        <td><?= $row['codigo_tecnico'] ?></td>
                        <td><?= $row['cedula_tecnico'] ?></td>
                        <td><?= $row['nombre_tecnico'] ?></td>
                        <td><?= $row['direccion_tecnico'] ?></td>
                        <td><?= $row['telefono_tecnico'] ?></td>
                        <td><div class="panel panel-primary">
                        <div class="panel-body">
                            <img src='vista.php?codigo_tecnico=<?= $row['codigo_tecnico'] ?>' alt='Img blob desde MySQL' width="300"/>
                        </div>
                        </div></td>
                        <td>
                            <a href="actualizar.php?codigo_tecnico=<?= $row['codigo_tecnico'] ?>" class="btn edit-btn">Editar</a>
                            <a href="delete.php?codigo_tecnico=<?= $row['codigo_tecnico'] ?>" class="btn delete-btn">Eliminar</a>
                        </td>
                    </tr>
                <?php endwhile; ?>
            </tbody>
        </table>
        <br>
        <input type="button" class="menu-button" onclick="window.location.href='index.php';" value="Atras" />
    </div>
</body>
</html>
