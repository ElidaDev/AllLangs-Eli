#include <stdio.h>
#include <strings.h>

typedef struct {
    char name[12];
    int id;
    float gpa;
} student;


int main(){
    student student1 = {"Spongebob", 1, 1.5};
    student student2 = {"Patrick", 2, 2.5};
    student student3 = {"Albert", 3, 4.0};
    student student4 = {"Squidward", 4, 0.5};

    student students[] = {student1,student2,student3,student4};

    int size = sizeof(students)/sizeof(students[0]); 
    for(int i = 0; i < size; i++){
        printf("\nName: %-12s | ID: %-3d |GPA: %-1.2f", students[i].name,students[i].id,students[i].gpa);
    }
    return 0;
}