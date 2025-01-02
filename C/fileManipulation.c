#include <stdio.h>
#include <string.h>

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

int findInFile(char filePath[], char data[]){
    FILE *pF = fopen(filePath,"r");
    char buffer[255];
    unsigned int line = 0;
    int found = 0;

    while(fgets(buffer, 255, pF) != NULL){
        line++;
        if (strstr(buffer,data)){
            printf("\nLine number: %u\nThe value has been found: %s\n",line, buffer);
            found = 1;
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
   
    //findInFile(filePath,"Ta");
    //printLine(filePath,250);
    //removeFile(filePath);
    //addToFile(filePath, "You have been tacoed \n",5000);




    return 0;
}