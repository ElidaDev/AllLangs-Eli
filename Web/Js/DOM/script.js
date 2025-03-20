var winloseLBL = document.getElementById("winlose");
var winnerImg = document.querySelector(".winimg");
var bod = document.querySelector("body");
var pTag = document.querySelector("p");
var secret;

function isNumeric(num) {
    return !isNaN(parseFloat(num) && isFinite(num))
}

document.getElementById("start").onclick = function(){
    while (!isNumeric(range)) {
        var range = parseInt(prompt("Set boundaries zero to ...?"));
   }
   //computer will pick a number
   const ANS = Math.floor(Math.random() * range +1);
   console.log(ANS);

   //GAN
   while(guess!=ANS){
     var guess = "";
     while(!isNumeric(guess)){ 
        var guess = parseInt(prompt(`Guess a number between 0 and ${range}`));
     }
    if(guess==ANS){
        winloseLBL.innerHTML="Hurray you got it!"
        winnerImg.style.display="block"; //visibility
        bod.style.backgroundColor="green";
        pTag.style.backgroundColor="red";
   }
   else if (guess < ANS) {
        console.log("Guess higher!")
        bod.style.backgroundColor = "blue"
   }
   else {
        console.log("Guess lower!")
        bod.style.backgroundColor = "brown"
    }
    }
}