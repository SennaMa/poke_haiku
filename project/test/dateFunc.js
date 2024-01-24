var currDate = new Date(2024,0,3).getTime();
var startDate = new Date(2024,0,1).getTime();
var listOfDates = [];

function fillDates (currDate, startDate, listOfDates) {
    var i = 2;
    listOfDates.sort();

    // we can store everything as time 
    // then convert to string

    while (!listOfDates.includes(currDate)) {
        runningDate = listOfDates.at(-1);
        if (!runningDate) {
            listOfDates.push(startDate);
        } else {
            
            if (runningDate <= currDate) {
                var nextDate = new Date(runningDate)
                nextDate.setDate(nextDate.getDate()+1);
    
                console.log('[runningDate < CurrDate] is' + nextDate)
                listOfDates.push(nextDate.setHours(0,0,0,0));
                console.log(listOfDates)
                i+=1;
            } else {
                var nextDate = new Date(currDate)
                nextDate.setDate(nextDate.getDate());
                listOfDates.push(nextDate.setHours(0,0,0,0));
            }
        }
    }
}

// check 
for (const element of listOfDates) {
    console.log(new Date(element));
}
