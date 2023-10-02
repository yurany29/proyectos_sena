<?php
include("../conexion.php");
$connect = connection();
$search = "SELECT * FROM tecnicos";
$peticion = mysqli_query($connect, $search);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilos/estiloindex.css">
    <title>CRUD TECNICOS</title>
</head>
<body>
    <div class="container">
        <h2>Técnicos en el sistema</h2>
        <table>
            <thead>
                <tr>
                    <th>Código técnico</th>
                    <th>Cédula técnico</th>
                    <th>Nombre</th>
                    <th>Dirección</th>
                    <th>Teléfono</th>
                    <th>Imagen tecnico</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
            <?php while ($row = mysqli_fetch_array($peticion)): ?>
                <tr>
                    <td><?= $row['codigo_tecnico'] ?></td>
                    <td><?= $row['cedula_tecnico'] ?></td>
                    <td><?= $row['nombre_tecnico'] ?></td>
                    <td><?= $row['direccion_tecnico'] ?></td>
                    <td><?= $row['telefono_tecnico'] ?></td>
                    <td>
                        <div class="panel panel-primary">
                            <div class="panel-body">
                                <img src="imagenes/<?= $row['codigo_tecnico'] ?>.jpg" alt='Img blob desde MySQL' width="300"/>
                            </div>
	                    </div>
                    </td>
                    <td><a href="consulta.php?codigo_tecnico=<?= $row['codigo_tecnico'] ?>" class="btn consult-btn">Consulta</a></td>
                </tr>
            <?php endwhile; ?>
            </tbody>
        </table>
        <input type="button" class="menu-button" onclick="window.location.href='../menu.php';" value="Menú" />
        <a href="crear.php" class="btn create-btn">Crear Técnico</a>
    </div>
</body>
</html> 
