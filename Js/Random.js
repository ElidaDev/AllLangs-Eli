//Edit what is in the "" to change what is in the random selection
var choice = [
    "Random1",
    "Random2",
    "Random3",
    "Random4",
    "Random5",
    "Random6",
    "Random7",
    "Random8",
    "Random9",
    "Random10"
    ]
  var c = 6
  function RollDice(roll) {
   return Math.floor(Math.random() * (roll - 1 + 1) + 1);
  }
  
  function makeid(length) { var result = ''; var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; var charactersLength = characters.length; for ( var i = 0; i < length; i++ ) { result += characters.charAt(Math.floor(Math.random() * charactersLength)); } return result; } 
  var choices = choice[Math.floor(Math.random()*choice.length)];
  var today = new Date();
  var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
  var dateTime = date+' '+time;
  var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
  var today = new Date(); 
  let num = Math.random();
  
  var b = (RollDice(c))
  var a = (RollDice(c))
  var d = (b+a)
  var rpsi = [
    "Rock",
    "Paper",
    "Scissors"
  ];
  
  var suits = [
    "of Diamonds",
    "of Clubs",
    "of Hearts",
    "of Spades"
    ]
  var suit = suits[Math.floor(Math.random()*suits.length)];  
  
  var cards = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "King",
    "Queen",
    "Jack"
    ]
  var card = cards[Math.floor(Math.random()*cards.length)];  
  
  var randomItem = rpsi[Math.floor(Math.random()*rpsi.length)];
  
  var colors = [
    "Red",
    "Orange",
    "yellow",
    "Green",
    "Purple",
    "Blue",
    "Cyan",
    "Aqua",
    "Pink"
    ]
   var randomcolor = colors[Math.floor(Math.random()*colors.length)];
  console.log (dateTime)
  console.log ("_____________________________________")
  console.log ("Dice Below")
  console.log ()
  console.log ("You rolled a "+a,"and a " +b)
  console.log ("Congrats! You rolled a total of ", (d))
  
  if (a!=b) {
    console.log ("You did not roll doubles")
  }
  else  {
    console.log ("You rolled doubles")
  }
  console.log ("_____________________________________")
  console.log ("Coinflip below")
  console.log ()
  if (num < 0.5) {
    console.log("HEADS");
  } else {
    console.log("TAILS");
  }
  console.log ("_____________________________________")
  console.log ("ROCK PAPER SCISSORS Below")
  console.log ()
  
  console.log (randomItem)
  console.log ("_____________________________________")
  console.log ("Card below")
  console.log ()
  console.log ("you drew a(n)" ,card , suit)
  console.log ("_____________________________________")
  console.log ("Randomcolor below")
  console.log ()
  console.log (randomcolor)
  console.log("_____________________________________")
  console.log ("Random string below")
  console.log ()
  console.log (makeid(10));
  console.log ("_____________________________________")
  console.log ()
  console.log ("Below is your random choice")
  console.log (choices)
  
  
  
