//The purpose of this file is test cat which stand for concatenates
#include<stdio.h>
#include<string.h>
int main (){
    char product[]="blueband";
    char flavour[]="prestige";
    strcat(product,flavour);
    printf("Do you prefer %s ?",product);
return 0;
}