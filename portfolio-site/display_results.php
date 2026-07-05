<!-- Student: Mike Steier
     Date: 06/03/2023
     Description: When user clicks submit on the contact_form.php page this page is displayed 
     It's purpose is to show the user what they entered into the webform on the page prior. 
-->

<?php
include 'navigation.php';
?>

<?php
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$company = filter_input(INPUT_POST, 'company');
$name = filter_input(INPUT_POST, 'name');
$phone = filter_input(INPUT_POST, 'phone');
$comments = filter_input(INPUT_POST, 'comments');


?>
<!DOCTYPE html>
<html>
<head>
    <title>Your Contact Information</title>
    <link rel="stylesheet" type="text/css" href="main.css"/>
    <link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
    <main>
        <h1>Your Contact Information</h1>

        <label>Email Address:</label>
        <span><?php echo htmlspecialchars($email); ?></span><br>

        <label>Company:</label>
        <span><?php echo htmlspecialchars($company); ?></span><br>

        <label>Your Name::</label>
        <span><?php echo htmlspecialchars($name); ?></span><br>

        <label>Phone Number:</label>
        <span><?php echo htmlspecialchars($phone); ?></span><br>

        <label>Comments:</label>
        <span><?php echo htmlspecialchars($comments); ?></span><br>
      <!--  <input type="submit" value="Submit"> -->
    <br>
    </form>    
    </main>