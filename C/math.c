#include <stdio.h>

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
        default:
            break;
    }
    return value;
}
void main(){
    printf("%d\n", add(1,2));
    printf("%s\n", evenorodd(1));
    printf("%.16f\n", calculator(2.0,3.0,'a'));
}