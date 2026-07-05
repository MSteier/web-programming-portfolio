/* Student: Michael Steier
   Date:    03/31/2023
   Dexcription: Exercise 7-2 Slide Show Application
*/

const $ = selector => document.querySelector(selector);
    
const imageCache = [];
let imageCounter = 0;
let timer = null;
let image = null;


let pauseButton = $("#pause");
let startButton =  $("#start")

// image and caption 

const mainImage = $("#main_image");   
const caption = $("#caption");        

const runSlideShow = () => {
    imageCounter = (imageCounter + 1) % imageCache.length;
    image = imageCache[imageCounter];
    mainImage.src = image.src;
    mainImage.alt = image.alt;
    caption.textContent = image.alt;
};
         
document.addEventListener("DOMContentLoaded", () => {
    const links = $("#image_list").querySelectorAll("a");
    
// Preload image
    
    for ( let link of links ) {
            image = new Image();
            image.src = link.href;
            image.alt = link.title;
        
         imageCache[imageCache.length] = image;
    }

    // Event listeners for the start image (displays for 2 seconds) and pause buttons
    startButton.addEventListener("click", () => {
        runSlideShow();
        timer = setInterval(runSlideShow, 2000);
        startButton.disabled = true;
        pauseButton.disabled = false;
    });
   
    pauseButton.addEventListener("click", () => {
        clearInterval(timer);
        startButton.disabled = false;
        pauseButton.disabled = true;
    });
});
