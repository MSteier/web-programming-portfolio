/*Student: Michael Steier
  Date:2/5/2023
  Description: calculates a fibbonacci sequence based on the number of 
               steps entered by the user
*/
document.write(`<h1>The Fibonacci Sequence</h1>`);
// Prompt user for steps in sequence

const steps = parseInt(prompt(`Please enter the number of steps you want in the sequence: `))

// check for invalid entries

if (isNaN(steps) || steps <= 0) {
  alert(`Entry must be a positive nummeric value`);
  document.write(`<h4>Invalid entry! </h4> <p>Reload your Browser to try again.</p>`);
}
else {

  // Create array and set it to the number of steps entered by the user
  const numbers = [steps];
 
  // sequence must begin with a 0 and 1
  numbers[1] = 1;
  numbers[0] = 0;
  
    
  //for loop to determine fibbonacci value starts at 2 because indices 0 and 1 already have values. 

  for (let index = 2; index < steps; index++) {
    numbers[index] = numbers[index - 1] + numbers[index - 2];
  }
  // display results
  document.write(`<h2>${numbers}</h2>`);
}