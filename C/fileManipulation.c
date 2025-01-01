#include <stdio.h>
#include <string.h>

FILE *fptr;
int main(){
    fptr = fopen("test.txt", "r+");
    if (fptr != NULL){
        char buffer[100];
        char newData[100];
        while(fgets(buffer, sizeof(buffer), fptr) != NULL){
            for (int i = 0; i < sizeof(buffer); i++){
                strncat(newData,buffer, 5);
                strcat(newData, "New");     
                printf("%s\n", newData);
                newData[0] = '\0';
            }
        }
    }
    else{
        printf("File Not Found");
        return 1;
    }
    fclose(fptr); 
    return 0;//WIP
}