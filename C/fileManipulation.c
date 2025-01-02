#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char string[2];

int addToFile(char filePath[], char data[], short int times){
    FILE *pF = fopen(filePath,"a");
    if(pF == NULL){
        printf("File could not be found at the path: %s", filePath);
        return 1;
    }
    for(int i = 0; i < times; i++){
        fprintf(pF,data);
    }
    fclose(pF);
    return 0;
}

int findInFile(char filePath[], char data[], int reverse){ // if reverse = 1, this is a reverse search for anything except the data inputed
    FILE *pF = fopen(filePath,"r");
    char buffer[255];
    unsigned int line = 0;
    int found = 0;

    while(fgets(buffer, 255, pF) != NULL){
        line++;
        if(reverse != 1){
            if (strstr(buffer,data)){
                
                printf("\nLine number: %u\nThe value has been found: %s\n",line, buffer);
                found = 1;
            }
            }
        else{
            if ((strstr(buffer,data)) == 0){
                printf("\nLine number: %u\nThe value has been found: %s\n",line, buffer);
                found = 1;
            }
        }
    }
    fclose(pF);
    if (found == 0){
        printf("The data \"%s\" Couldn't be found in the file at \" %s\"",data,filePath);
        return 1;
    }
    else{
        return 0;
    }
    
}

int printLine(char filePath[], unsigned int line){   
    FILE *pF = fopen(filePath,"r");
    char buffer[255];
    int found = 0;
    unsigned int linec = 0;
    while(fgets(buffer, 255, pF) != NULL){
            linec++;
            if (linec == line ){
                printf("\nLine number: %u\n%s\n",line, buffer);
                found = 1;
            }
    }
    fclose(pF);
    if(found != 1){printf("Could not find line: #%u", line); return 1; }
    else{return 0;}
    
}

int removeFile(char filePath[]){
    if(remove(filePath) == 0){
        printf("File deleted...");
        return 0;
    }
    else{
        printf("File could not be located...");
        return 1;
    }
}
int main(){
    char filePath[] ="C:\\Users\\elija\\Desktop\\test.txt";
    srand(time(0));
    findInFile(filePath,"1",1);
    //printLine(filePath,250);
    //removeFile(filePath);
    // for(int i = 0; i < 1000; i++){
    //     addToFile(filePath,"1",1);
    //     for(int j = 0; j < 50; j++){
    //         char randomChar = (char)((rand() % 94) + 33);
    //         string[0] = randomChar;
    //         string[1] = '\0';
    //         addToFile(filePath,string ,1);
    //     }
    //     addToFile(filePath,"\n" ,1);
    // }



    return 0;
}