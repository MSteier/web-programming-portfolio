/* Student: Michael Steier 
   Date: 1-23-2023
   Description: Chapter 3 Exercise 3.1
*/
"use strict";

// alow user to repeat calculaction
let again = prompt("Enter values (y/n)?: ");

do {
    if (again != "y") {
        document.write("<h3>No values were entered</h3>");
        break;
    }
    
    // get investment amount - loop until user enters a number
    let investment = 0;
    do {
        while (investment <= 0) {
            investment = parseFloat(prompt("Enter investment amount as xxxxx.xx", 10000));
            if (investment <= 0) {
                alert(" The Investment amount must be greater than zero");
            }
        }
    }
    while (isNaN(investment));
    

    // get interest rate - loop until user enters a number
    let rate = 0;
    do {
        rate = parseFloat(prompt("Enter interest rate as xx.x", 7.5));
        while (rate <= 0 || rate >= 15) {
            alert("The rate must be greater than zero and less than 15");
            rate = parseFloat(prompt("Enter interest rate as xx.x", 7.5));
        }
    }
            
        while (isNaN(rate));
  
        // get number of years - loop until user enters a number
        let years = 0;
        do {
            years = parseInt(prompt("Enter number of years", 5));
            while (years <= 0) {
                if (years <= 0) {
                    alert("The entry for years must be greater than zero.");
                    years = parseFloat(prompt("Enter interest rate as xx.x", 7.5));
                }
                
            }
        }
        while (isNaN(years));
    
    

        // calulate future value
    let futureValue = investment;
    document.write(`<h1>The Future Value Calculator<h1>`);
        for (let i = 1; i <= years; i++) {
            futureValue = futureValue + (futureValue * rate / 100);
           
            //calculate interest for each yearyear
            let annualInterest = 0;
            annualInterest = (futureValue * rate) * ( i / 100);
            
            // display future value for each year
           
            document.write(`<h4><p>Investment amount = ${investment.toFixed(2)} Interest rate =  ${rate} 
                            Years = ${years}</p></h4>`);
            
            document.write(`<p>Year ${i} interest= ${annualInterest.toFixed(2)} 
                            Value = ${futureValue.toFixed(2)}</p>`);
    }
    
        // display results
    
        document.write(`<h1> The Future Value Calculator </h1>`);
        document.write(`<p><label>Investment amount:</label> ${investment}</p>`);
        document.write(`<p><label>Interest rate:</label> ${rate}</p>`);
        document.write(`<p><label>Years:</label> ${years}</p>`);
        document.write(`<p><label>Future Value:</label> ${futureValue.toFixed(2)}</p>`);
    
       
        again = prompt("enter more values (y/n)?:  ");
        // end do-while

        if (again != "y") {
            break;
        }
    } while (again == "y");

