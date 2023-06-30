#include<stdio.h>
#include<string.h>
int main(){
    char title[]="Movies ";
    char intr[]="adventure";
    strcpy(title,intr);
    printf("look at this %s",title);
return 0;
}