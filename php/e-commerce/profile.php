<?php 
session_start();

if(isset($_GET['action']) && ($_GET['action'] == 'logout')) {
    session_destroy();
    header("Location: login.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
</head>
<body>

    <div class="container my-5">
        <?= $_SESSION['username'] ?> | <a href="?action=logout">Logout</a>
    </div>

</body>
</html>