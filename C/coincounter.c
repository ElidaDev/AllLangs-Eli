#include <stdio.h>
#include <conio.h>
double sum(int nums[]){
    double total;
    total = (nums[0]*.01) + (nums[1]*.05) + (nums[2]*.1)+(nums[3]*.25);
    return total;
}
void summary(int coins[]){
            double count = sum(coins);
            printf("Pennies : %-4d : $%-2.2lf\n", coins[0], (double)coins[0]*.01);
            printf("Nickels : %-4d : $%-2.2lf\n", coins[1], (double)coins[1]*.05);
            printf("Dimes   : %-4d : $%-2.2lf\n", coins[2], (double)coins[2]*.1);
            printf("Quarters: %-4d : $%-2.2lf\n", coins[3], (double)coins[3]*.25);
            printf("Total amount of coins: %d\n", coins[0]+coins[1]+coins[2]+coins[3]);
            printf("$%.2f\n",count);
}
void main(){
    int c;
    double count = 0.0;
    int coins[] = {115,30,36,55}; //These are the numbers of coins in the jar Pennies,Nickels,Dimes,Quarters starting out
    double last;

    printf("Program started!\nPenny(1),Nickle(2),Dime(3),Quarter(4), Remove last(5)\n");
    printf("6,7,8,9 sets last coin to the corresponding coin 6(penny), 7(nickle)... etc\n0 shows the coins counted so far\n");
    while((c = getch()) !=EOF )
        if(c == 27){
            summary(coins);
            break;
        }
        else if (c == 48){        
            summary(coins);
        }
        else if (c == 49){ // Penny(1)
            coins[0] += 1;
            last = .01;
            printf("added a penny, running total: %3.2f\n", sum(coins) );
        }
        else if (c == 50){ // Nickle(2)
            coins[1] += 1;
            last = .05;
            printf("added a nickle, running total: %3.2f\n", sum(coins));
        }
        else if (c == 51){ // Dime(3)
            coins[2] += 1;
            last = .10;
            printf("added a dime, running total: %3.2f\n", sum(coins));
        }
        else if (c == 52){ //Quarter(4)
            coins[3] += 1;
            last = .25;
            printf("added a quarter, running total: %3.2f\n", sum(coins));
        }
        else if (c == 53){ //Remove last (5)
            printf("Removed %.2f", last); 
            printf(", running total: %.2f\n", sum(coins));
            if (last == .01) coins[0] -= 1;
            if (last == .05) coins[1] -= 1;
            if (last == .1) coins[2] -= 1;
            if (last == .25) coins[3] -= 1;
        }
        else if (c == 54){ last = .01; printf("Set last coin to Penny!\n");}
        else if (c == 55){ last = .05; printf("Set last coin to Nickle!\n");}
        else if (c == 56){ last = .10; printf("Set last coin to Dime!\n");}
        else if (c == 57){ last = .25; printf("Set last coin to Quarter!\n");}
}

