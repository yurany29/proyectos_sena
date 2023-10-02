<?php
include("../conexion.php");

$connect = connection();

$codigo = $_GET["codigo_tecnico"];

$consulta = "SELECT * FROM tecnicos WHERE codigo_tecnico='$codigo'";
$solicitud = mysqli_query($connect, $consulta);
$row = mysqli_fetch_array($solicitud);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilos/estiloeditar.css">
    <title>Editar Técnico</title>
</head>
<body>
    <div class="container">
        <h2>Editar Técnico</h2>
        <form action="update.php" method="POST">
            <input type="hidden" name="codigo_tecnico" value="<?= $row['codigo_tecnico'] ?>">
            <div class="form-group">
                <label for="cedula">Cédula:</label>
                <input type="text" name="cedula_tecnico" id="cedula" placeholder="Cédula" value="<?= $row['cedula_tecnico'] ?>">
            </div>
            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input type="text" name="nombre_tecnico" id="nombre" placeholder="Nombre" value="<?= $row['nombre_tecnico'] ?>">
            </div>
            <div class="form-group">
                <label for="direccion">Dirección:</label>
                <input type="text" name="direccion_tecnico" id="direccion" placeholder="Dirección" value="<?= $row['direccion_tecnico'] ?>">
            </div>
            <div class="form-group">
                <label for="telefono">Teléfono:</label>
                <input type="text" name="telefono_tecnico" id="telefono" placeholder="Teléfono" value="<?= $row['telefono_tecnico'] ?>">
            </div>
            <div class="form-group">
                <form name="MiForm" id="MiForm" method="post" action="update.php" enctype="multipart/form-data">
                    <h4 class="text-center">Seleccione imagen a cargar</h4>
                    <div class="formgroup">
                        
                        <div class="col-sm-8">
                            <input type="file" class="form-control" id="image" name="image" multiple>
                        </div>
                        
                    </div>
                </form>
            <div class="form-group">
                <input type="submit" value="Actualizar">
            </div>
            <div class="form-group">
                <input type="button" class="menu-button" onclick="window.location.href='consulta.php?codigo_tecnico=<?= $row['codigo_tecnico'] ?>';" value="Atrás">
            </div>
        </form>
    </div>
</body>
</html>
