#include <stdio.h>
#include <math.h>

int add(int x, int y){
    return x+y;
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
        case '^': //Sqrt
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



void main(){
    printf("%d\n", add(1,2));
    printf("%s\n", evenorodd(1));
    printf("%.16f\n", calculator(2.0,3.0,'a'));
    printf("%.16f\n", calculator(4,0,'^')); 
    printf("%s\n", isPrime(1));
    printf("%s\n", isPrime(3));
    printf("%s\n", isPrime(4));
}