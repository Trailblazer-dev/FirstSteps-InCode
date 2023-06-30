#include<stdio.h>
#include<stdio.h>
int main (){
    char no[11];
    printf("Enter your phone number\n");
    fgets(no,sizeof(no),stdin);
    if(strlen(no)==10){
        printf("successful\n");
    }
    else{
        printf("invalid._____please insert your number and check before submitting \n");
    }
return 0;
}
//these program has an error such that if someone input excess integer it wouldn't detect.