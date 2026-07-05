<!-- Student: Mike Steier
     Date: 06/03/2023
     Description: form so user can leave feedback for me
-->
<?php
include 'navigation.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="form_style.css">
    <title>Contact Me</title>
    
</head>
<body>
    <main>
    <fieldset>
    <legend>Your Contact Information</legend>
    <form action="display_results.php" method="post">
        <label>E-Mail:</label>
        <input type="text" name="email" value="" class="textbox">
        <br>
        <label>Company:</label>
        <input type="text" name="company" value="" class="textbox">

        <label>Your Name:</label>
        <input type="text" name="name" value="" class="textbox">
        <br>

        <label>Phone Number:</label>
        <input type="text" name="phone" value="" class="textbox">
        <br>
    <fieldset>
        <legend>Leave a comment</legend>
    <p>Comments:</p>
        <textarea name="comments" rows="4" cols="50"></textarea>
    </fieldset>
    <br>

    <input type="submit" value="Submit">
</body>
</main>
    
    <form action="display_results.php" method="post">
</html>