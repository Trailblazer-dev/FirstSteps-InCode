#include<stdio.h>
#include<string.h>
int main (){
    char number[11];
    printf("Enter your mobile number please\n");
    fgets(number, sizeof(number), stdin);
    while(strlen(number)!=11){
        printf("Please enter your phone number in the right format\n");
        fgets(number,sizeof(number),stdin);
    }
    printf("successful thank-you");
    return 0;
    }