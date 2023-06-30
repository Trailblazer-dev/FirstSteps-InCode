//is similar to strchr the only difference is that it searches for a string instead of char
#include<stdio.h>
#include<string.h>
int main(){
    char kali[70]="life is hard but you have to unjust to handle it";
    printf("let check this out %s",strstr(kali,"is"));
return 0;
}