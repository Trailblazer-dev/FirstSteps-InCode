#include<stdio.h>
int main(){
    FILE *key;
    key=fopen("test.txt","r");
    char t[100];
    //The first parameter specifies where to store the file content
//The second parameter specifies the maximum size of data to read, 
//The third parameter requires a file pointer that is used to read the file .
    while(fgets(t,100,key)){
    printf("%s",t);
    }
    fclose(key);
}
//we use while loop to read all line in the file since fgets only displays first line