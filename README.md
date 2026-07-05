# Web Programming Portfolio

Selected coursework from the **Web Programming Certificate Program at Southeast Technical College** (CIS 195 Internet Programming Essentials and CIS 196), demonstrating front-end development with HTML, CSS, vanilla JavaScript, and PHP.

This is not a comprehensive sampling of my abilities — I'm continuously learning new technologies and adding to my skill set.

## Repository Structure

```
portfolio-site/   PHP portfolio website (home, resume, coursework pages, contact form)
projects/         Standalone front-end projects, each in its own folder
```

## Portfolio Site

A small multi-page PHP site with shared navigation, a resume page, and a contact form with client-side validation. To run it locally:

```
cd portfolio-site
php -S localhost:8000
```

Then open http://localhost:8000 in a browser.

## Projects

Each project is self-contained — open its `index.html` (or the page noted below) in a browser.

| Project | Description | Skills Demonstrated |
|---|---|---|
| [`venomous-snakes-website`](projects/venomous-snakes-website/) | Multi-page site about venomous snakes of the world. Hotspots on a world map (Southern California, Eastern Arizona, central Africa, eastern India) link to pages for the western diamondback, Sonoran coral snake, Gaboon viper, and Russell's viper. Start at `default.html`. | HTML image maps / hotspots, multi-page layout |
| [`happy-hound-responsive-site`](projects/happy-hound-responsive-site/) | Dog-care site that adapts cleanly to all screen sizes. | Media queries, responsive design |
| [`komatsu-family-website`](projects/komatsu-family-website/) | Family website where clicking each member's face in a group photo navigates to their page. Start at `html/tb_komatsu.html`. | CSS/HTML graphic design, image hotspots |
| [`customer-survey-form`](projects/customer-survey-form/) | Customer satisfaction survey that validates user input and flags valid/invalid entries. Start at `rb_survey.html`. | Web forms, client-side validation, regular expressions |
| [`slide-show`](projects/slide-show/) | Image slideshow with preloaded images, captions, and pause/resume controls. Start at `MS_index.html`. | DOM manipulation, timers, image preloading |
| [`registration-form`](projects/registration-form/) | Registration form with validation and a confirmation page. Start at `MS_index.html`. | Web forms, JavaScript validation |
| [`guessing-game`](projects/guessing-game/) | Number guessing game (CIS 196 Assessment 1). | Control flow, user input handling |
| [`fibonacci-sequence`](projects/fibonacci-sequence/) | Fibonacci sequence generator. | Loops, algorithms |
| [`future-value-calculator`](projects/future-value-calculator/) | Compound-interest future value calculator. | Form input, arithmetic, DOM updates |
| [`test-scores`](projects/test-scores/) | Test score statistics built with arrays. | Arrays, iteration |

## Technologies

- HTML5 & CSS3 (responsive design, media queries, image maps)
- Vanilla JavaScript (DOM manipulation, form validation, timers)
- PHP (multi-page site structure, form handling)
