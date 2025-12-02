#include <stdio.h>

int partOne(){
    char buff[255];
    int fuel=0;
    FILE *input;
    input=fopen("./input1.txt","r");
    fgets(buff,255, (FILE*)input);
    fclose(input);
    printf("%s",buff[1]);
    return 0;
}

int 

void partTwo(){
    
}

int main(){
    partOne();
    return 0;
}