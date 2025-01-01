#include <stdio.h>
#include <strings.h>
//Very important if you want to be efficient imo...
/*
Type          | Bytes | %formating |(Precision/min-max)              | Unsigned precision/min-max
float         | 4     | %f         | 32 bit (6-7 digits)             |
Double        | 8     | %lf        | 64 bit (15-16 digits)           |
bool          | 1     | %d         |                                 |
char          | 1     | %d/%c      | -128 to 127                     | 0 to 255
short         | 2     | %d         | -32,768 to 32,767               | 0 to 65,535
int           | 4     | %d         | -2,147,483,648 to 2,147,483,647 | 0 to 4,294,967,295 (%u)   
long long     | 8     | %lld       | -9 quint to +9 quint            | 0 to 18 quintillion (%llu)



Formatting 

%.(#of decimal places)
%1
%- (Left align)
*/
struct Player
{
    char name[12];
    int score;
};

typedef char string[];

int main(){
    printf("Hello World!");
    //How to write a comment

    /*
    Multi
    Line
    Comment
    */

    // // Variables
    // int x; //Declaration
    // int y = 2; //Declaration/Initialization same line
    // char z = 'a';
    // char name[25];
    // double a = 1.5; // 
    // float b = 2.0;
    // char c[] = "This is an array of characters!";
    // long long d = 28638527;
    // double prices[10] = {1,2,3,4,5,6,7,8,9.5,10};
    // // %c = char, %d = ints, %f = floats, %s for arrays of chars
    // printf("X = %d, z = %c, y = %d",x,z,y); // learned
    // printf("Please input x: ");
    // scanf("%d", &x);
    // printf("What's your name: ");
    // fgets(name, 25, stdin);
    // name[strlen(name)-1] = '\0'; // gets rid of newline character

    // printf("You're name %s is pretty cool!", name);

    // for (int i = 0; i < sizeof(prices)/sizeof(prices[0]); i++){
    //     printf("%lf\n", prices[i]);
    // }
    // int numbers[2][3];
    // numbers[0][2] = 1; 
    // char cars[][15] = {"Porsche", "Bugatti", "SRT", "Challenger"};
    // strcpy(cars[0],"Corola");
    // printf("%d\n", (sizeof(cars)/sizeof(cars[0])));
    // for(int i = 0; i < (sizeof(cars)/sizeof(cars[0])); i++){
    //     printf("%s\n", cars[i]);
    // }

    // char x[15] = "Water";
    // char y[15] = "soda";
    // char temp[15];

    // strcpy(temp, x);
    // strcpy(x, y);
    // strcpy(y,temp);
    // printf("\nX: %s\nY: %s",x,y);

    //Structs

    string name = "This is a string!";
    printf("%s", name);
    
    
    // struct Player player1;
    // struct Player player2;
    // strcpy(player1.name,"ME!");
    // player1.score = 401;
    // strcpy(player2.name,"NotMe...");
    // player2.score = 1;
    // printf("\n\n%-12s:%-4d\n%-12s:%-4d",player1.name,player1.score,player2.name,player2.score);
    return 0;
}