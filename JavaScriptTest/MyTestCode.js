import { math } from "./mathfs"; 
function calculateDaysBetweenDates(begin, end) {
    // Parse the input strings as Date objects
    const beginDate = new Date(begin);
    const endDate = new Date(end);
    
    // Calculate the time difference in milliseconds
    const timeDifference = endDate.getTime() - beginDate.getTime();
    
    // Convert milliseconds to days
    const daysBetween = Math.floor(timeDifference / (1000 * 3600 * 24));
    
    return daysBetween;
  }


  const beginDate = "2023-01-01";
  const endDate = "2023-06-30";
  const daysBetween = calculateDaysBetweenDates(beginDate, endDate);
  console.log(daysBetween);  // Output: 180

  console.log("strings to print");


function covertTemp(_varTemp) {
    // will convert Celcius to Farenheit
    return math.evaluate(parseFloat((_varTemp)*(9/5))+32)
}
  