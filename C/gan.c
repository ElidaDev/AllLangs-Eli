#include <stdio.h>

int main(){
    int secretNumber = 7;
    int guess;
    int guesses = 5;
    int loop = 1;
    while(loop == 1){
        printf("Enter a number between 1 and 10: ");
        scanf("%d", &guess);
        if (guess == secretNumber){printf("You guessed the number! %d\n", secretNumber); loop = 0;}
        else if (guess < secretNumber){printf("You guessed lower than the number! %d\n", guess);}
        else{printf("You guessed higher than the number! %d\n", guess);}
    }
    return 0;
}