<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="estilos/estilotecnicocrear.css">
    <title>Crear Usuario</title>
</head>
<body>
    <div class="container">
        <h2>Crear Usuario</h2>
        <form action="insertar.php" method="POST">
            <div class="form-group">
                <label for="cedula_tecnico">Cédula:</label>
                <input type="text" id="cedula_tecnico" name="cedula_tecnico" placeholder="Cédula" required>
            </div>
            <div class="form-group">
                <label for="nombre_tecnico">Nombre:</label>
                <input type="text" id="nombre_tecnico" name="nombre_tecnico" placeholder="Nombre" required>
            </div>
            <div class="form-group">
                <label for="direccion_tecnico">Dirección:</label>
                <input type="text" id="direccion_tecnico" name="direccion_tecnico" placeholder="Dirección" required>
            </div>
            <div class="form-group">
                <label for="telefono_tecnico">Teléfono:</label>
                <input type="text" id="telefono_tecnico" name="telefono_tecnico" placeholder="Teléfono" required>
            </div>
            <div class="form-group">
                <form name="MiForm" id="MiForm" method="post" action="insertar.php" enctype="multipart/form-data">
                    <h4 class="text-center">Seleccione imagen a cargar</h4>
                    <div class="formgroup">
                        
                        <div class="col-sm-8">
                            <input type="file" name="imagen_tecnico" id="imagen_tecnico">
                        </div>
                        
                    </div>
                </form>
            <div class="form-group">
                <input type="submit" name=submit value="Agregar" class="btn add-btn">
                <button type="button" class="btn cancel-btn" onclick="window.location.href='index.php';">Cancelar</button>
            </div>
          

        </form>
    </div>
</body>
</html>
