var rawDate = new Date();
var month = rawDate.getMonth() + 1; // adding one because getMonth() is zero-based
var day = rawDate.getDate();
var year = rawDate.getFullYear();

// below can be written as ternary statements
if (month < 10) {
    month = '0'+ month
}

if (day < 10) {
    day = '0' + day
}

var date = year + '-' + month + '-' + day;
console.log(date);

var dailyHaiku = [];
var dailySprite = [];

var parsedHaikus = window.__DATA__;

for (var i = 0; i < Object.values(parsedHaikus['dates']).length; i++) {
    if (parsedHaikus.dates[i] == date) {
        dailyHaiku.push(parsedHaikus.haiku[i])
        dailySprite.push(parsedHaikus.sprites[i])
    }
}

function fetchHaiku() {
    return dailyHaiku[0].split("\n\n")
}

function fetchSprite(position) {
    if (position === "front") {
        return dailySprite[0]
    } else {
        return dailySprite[0].replace("/animated/", "/animated/back/")
    }
}

function fetchDate() {
    return rawDate.toUTCString()
}