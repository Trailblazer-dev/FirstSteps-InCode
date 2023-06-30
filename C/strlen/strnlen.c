#include<stdio.h>
#include<string.h>
int main (){
    char team[12];
    printf("Which football team do support\n");
    fgets(team,sizeof(team),stdin);
    printf("The length of string when it maxlen is 10 : %d\n",strnlen(team, 5));
    printf("The length of string when it maxlen is 20: %d\n",strnlen(team, 20));
return 0;
}
//strnlen is useful where the input strings are limited check strnlen2.