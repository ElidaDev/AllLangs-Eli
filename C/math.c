#include <stdio.h>
#include <math.h>
#include <ctype.h>

const double PI = 3.14159;

double hypotenuse(double a, double b){
    double c;
    c = sqrt(pow(a,2)+pow(b,2));
    return c;
}

double circumference(double radius){
    double c;
    c = 2 * PI * radius;
    return c;
}

double area (unsigned short length, unsigned short width, char shape[10]){ // Length is also radius
    char selection;
    double a;

    if (shape == "circle"){selection = 'c';}
    else if(shape == "square" || shape == "rectangle"){selection = 's';} //Circle, Rectangle/square
    switch (selection){
        case 'c':
            a = PI * pow(length,2);
            break;
        case 's':
            a = length*width;
            break;
        default:
            printf("Invalid shape, Please try again... We support circle, square, and rectangle...");
            return 1;
    }
    return a;
}

const char* evenorodd(int x){
    if(x % 2 == 0) {return "Even";}
    else{return "Odd";}
}

double calculator(double x, double y, char operator){
    double value;
    switch (operator){
        case '+':
            value = x+y;
            break;
        case '-':
            value = x-y;
            break;
        case '/':
            value = x/y;
            break;
        case '*':
            value = x*y;
            break;
        case '^': //xto the power of y
            value = pow(x,y);
            break;
        case '%': //Sqrt
            value = sqrt(x);
            break;
        default:
            break;
    }
    return value;
}

const char* isPrime(int num){
    if (num <=1){
        return "Not Prime";
        }
    for (int i = 2; i <= sqrt(num); i++){
        if (num % i == 0){
            return "Not Prime";
            }
    
    }
    return "Prime!";
}

double converter(float temperature, char unit){
    
    if(toupper(unit) == 'F'){
        temperature = ((temperature - 32) * 5) / 9;
        return temperature;
    }
    else if(toupper(unit) == 'C'){
        temperature = (temperature * 9 / 5) +32;
        return temperature;
    }
    else{
        printf("Could not determine the unit (%c)! Please try again... (c/f)", unit);
        return 1;
    }
}


void main(){
    // printf("%s\n", evenorodd(1));
    // printf("%.16f\n", calculator(2.0,3.0,'a'));
    // printf("%.16f\n", calculator(4,2,'^')); 
    // printf("%s\n", isPrime(1));
    // printf("%s\n", isPrime(3));
    // printf("%s\n", isPrime(4));
    // printf("%lf\n", circumference(10));
    // printf("%.5lf\n", area(10,0,"circle"));
    // printf("%lf", hypotenuse(3,4));
    printf("%f", converter(32,'f'));
}