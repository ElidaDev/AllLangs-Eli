#include <stdio.h>

int main(){
    printf("Hello World!");
    //How to write a comment

    /*
    Multi
    Line
    Comment
    */

    // Variables
    int x; //Declaration
    x = 1; //Initialization
    int y = 2; //Declaration/Initialization same line
    char z = 'a';
    double a = 1.5; // 
    float b = 2.0;
    char c[] = "This is an array of characters!";
    long long d = 28638527;
    // %c = char, %d = ints, %f = floats, %s for arrays of chars
    printf("X = %d, z = %c, y = %d",x,z,y); // learned

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

// He talks about all the operators, but i know them all from other programming languages atleast what he went over...

    scanf("%d", &x);
    printf("The value of x is %d!",x);
    return 0;
}