<!-- Student: Mike Steier
* Date:06/01/2023
* Description: defines navigation bar for all pages in its own file.
-->

<nav class="navbar">
        <div class="brand-title">Mike's Portfolio</div>
        <a href="#" class="toggle-button">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </a>
        <div class="navbar-links">
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="Resume.php">Resume</a></li>
                <li><a href="internet_programming_II.php">Internet Programming II</a></li>
                <li><a href="internet_programming_essentials.php">Internet Programming Essentials</a></li>
                <li><a href="contact_form.php">Contact Form</a></li>
                <li><a href="https://github.com/MSteier/web-programming-portfolio">Work Examples</a></li>
            </ul>
        </div>
    </nav>
    <script>
        const toggleButton = document.getElementsByClassName('toggle-button')[0]
        const navbarLinks = document.getElementsByClassName('navbar-links')[0]

        toggleButton.addEventListener('click', () => {
        navbarLinks.classList.toggle('active');
});
    </script>
    <style>

    /* CSS for navbar added to the same file to reduce number of files in project folder */    

    .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    color: white;
}
.brand-title {
    font-size: 1.5rem;
    margin: .5rem;
}

.navbar-links ul {
    margin: 0;
    padding: 0;
    display: flex;
}

.navbar-links li {
    list-style: none;
}

.navbar-links li a {
    text-decoration: none;
    color: white;
    padding: 1rem;
    display: block;
}

.navbar-links li:hover {
    background-color: rgb(66, 66, 66);
}

.toggle-button {
    position: absolute;
    top: .75rem;
    right: 1rem;
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 30px;
    height: 21px;
}
</style>
    