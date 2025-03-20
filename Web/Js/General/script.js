var secret = 4;
var guess = prompt("guess a number between 1-5");
while(guess!=secret){
    if(guess<secret){
        alert("guessed too low");
    } else if(guess>secret){
        alert("guessed too high");
    } else{
        alert("YOU WIN!");
        break;
    }
    var guess = prompt("guess a number between 1-5");
}