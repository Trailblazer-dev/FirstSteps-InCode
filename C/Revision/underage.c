#include<stdio.h>
int main(){
    int age;
    printf("Enter your age\n");
    scanf("%d",&age);
    if (age<18)
    {
        printf("You are under 18\n");
    }
    else
printf("You are above 18");
return 0;
}