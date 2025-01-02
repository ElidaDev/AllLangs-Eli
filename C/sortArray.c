#include <stdio.h>

void sort(int array[], int size, char order[]){
    int temp;
    if (order == "ascending"){
        for(int i = 0; i< size-1; i++){
            for (int j = 0; j < size - i -1; j++){
                if(array[j]>array[j+1]){
                    temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }}
    else{
        for(int i = 0; i< size-1; i++){
            for (int j = 0; j < size - i -1; j++){
                if(array[j]<array[j+1]){
                    temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
}

void printArray(int array[], int size){
    for(int i = 0; i < size; i++){
        printf("%d, ", array[i]);
    }
}

int main(){
    int array[] = {9,2,3,6,7,3,2,7,8,9,12,745,325,24};
    int size = sizeof(array)/sizeof(array[0]);
    sort(array,size,"descending");
    printArray(array,size);
    printf("\n");
    sort(array,size,"ascending");
    printArray(array,size);
    return 0;
}