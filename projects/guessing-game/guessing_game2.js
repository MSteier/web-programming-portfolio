/* Student: Michael Steier
   Date: 02/02/2023
   Description: The user tries to guess three pseudorandomly generated numbers
   within the range of 0 through 9. The user earns 10 points for each time the number 
   they entered matches any of the pseudorandomly generated numbers. when the user is finished
   guessing the results are displayed in the web browser.
*/

// pick random numbers

const numbers = [Math.floor(Math.random() * 10), Math.floor(Math.random() * 10), Math.floor(Math.random()
                * 10)];


/* 
Test values for demo purposes

const numbers = [];
numbers[0] = 7;
numbers[1] = 7;
numbers[2] = 0;
*/

let score = 0;
let total_score = 0;
let user_guess = 0;

// Print Title

document.write(`<h1><center>The Guessing Game</center></h1>`);
    
        // prompt the user for a guess

for (const number of numbers) {
    user_guess = parseInt(prompt(`Please enter a number between 0 and 9:`));
    if (user_guess == isNaN) {
        alert(`Please enter a nummeric value within the specified range.`);
        user_guess = parseInt(prompt(`Please enter a number between 0 and 9:`));
        }
    
    // check to see if users entry matches the current index
    if (user_guess == number) {
        alert(`You guessed ${user_guess}! You Win 10 points!`);
        total_score += 10;       
    }
    // check users input to make sure its valid
    else if (isNaN(user_guess) || user_guess < 0 || user_guess > 9) {
                alert(`Please enter a nummeric value within the specified range.`);
                user_guess = parseInt(prompt(`Please enter a number between 0 and 9:`));
            }
        
            // print results to page

            document.write(`<center><h3>Results:</center</h3>`);
            document.write(`<h3>You guessed: ${user_guess}</h3>`);
            document.write(`<h3>The computer picked: ${number}</h3>`);
            document.write(`<h3>Score: ${total_score}</h3>`);
            document.write(`<center><h3>TotalScore: ${total_score}</center></h3>`);

    }
    


 
    
   