<?php
    error_reporting(0); //repota errores
    session_start(); // inicia sesion en php
    $con = new mysqli("localhost", "root", "", "cliente"); //se inicializa variable y se busca el servidor nombre de la base de datos
    if ($con->connect_errno) //si los datos no se encuentran
    {
            echo "Fallo al conectar a MySQL: (" . $con-> connect_errno .")" . $con->connect_error; //Imprimir el error
            exit(); //salir
    }
    @mysqli_query($con, "SET NAMES 'utf8'"); //Realiza un recorrido y permite poner caracteres especiales
    if ($_POST['usuario'] == null || $_POST['contrasena'] == null) //if sencillo, si el dato ingresado por la variable post esta vacio
    {
        echo '<span>Por favor complete todos los campos.</span>'; //imprime
    }       //en los condicionales no va punto y coma 
    else
    {
        $user = $_POST['usuario']; //asignarle el valor de post a la avariable user
        $contrasena = $_POST["contrasena"]; //asignarle el valor de post a contraseña
        $consulta = mysqli_query($con, "SELECT * FROM login WHERE usuario = '$user' and contrasena='$contrasena'"); //en la variable hace un recorrido por la base de datos, selecciona todos los campos de la tabla login, donde usuario  sea igual al usuario y contrasena igual a la contraseña ingresada

        if(mysqli_fetch_array($consulta)>0){ //array: lista. si en la busqueda encuentra algo mayor a cero

            $_SESSION["usuario"] = $user;
            echo '<script>location.href = "../index.html"</script>';//cuando ya este autenticado que lo pase a la pagina principal
        }
        else
        {
            echo '<span>El usuario y/o clave son incorrectas, vualva a intentarlo.</span>';//si lo anterior no se cumple imprimir
            echo '<script>location.href = "login.html"</script>'; //lo redirecciona nuevamente a la pagina del login
        }
    }
?>