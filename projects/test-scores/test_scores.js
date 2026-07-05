// Student: Michael Steier
// Date:01/26/2023
// Description: Exercise 3.2 Enhance Test Scores application

"use strict";

let scores = [];
let highScore = 0;
let score = 0;

// use do-while loop to get the scores from the user

document.write(`<h1>The Test Scores App</h1>`);
do {
    score = parseInt(
        prompt("Enter a test score, or enter -1 to end scores", -1));

    if (score >= 0 && score <= 100) {
        scores[scores.length] = score;
    }
    else if (score != -1) {
        alert("Score must by a valid number from 0 through 100");
    }
}

while (score != -1);

if (scores.length > 0) {
    // use a for-in loop to add each score to total, and display score
    let total = 0;
    for (let i in scores) {
        total = total + scores[i];
        document.write(`<p>Score ${parseInt(i) + 1}: ${scores[i]}</p>`);
    }
        let highScore = scores[0];
        for (let index = 1; index < scores.length; index++) {
        if(scores[index] > highScore) {
        highScore = scores[index];
        }        
    }
    alert(`The high score is ${highScore}`);
    document.write(` The sum of all scores is: ${total}`);
    document.write(`<p>The highest score is ${highScore} </p>`);

            //calculate and display the average
            const average = parseInt(total / scores.length);
            document.write(`<p>Average score is ${average}</p>`);    
}
        
        // calculate and display the high score
            /*
            let highest = scores[0];
            for (let index = 1; index < scores.length; index++) {
            if (scores[index] > highest) {
                highest = scores[index];
            }  
        }    
            */
//document.write(`<p>The highest score is ${highest} </p>`);
