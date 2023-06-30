#include<stdio.h>
int main(){
    int age;
    char unit1,unit2,unit3;
    printf("Enter your age\n");
    scanf("%d",&age);
    printf("Enter grade for unit1\n");
    scanf(" %c",&unit1);
    printf("Enter grade for unit2\n");
    scanf(" %c",&unit2);
    printf("Enter your grade for unit3\n");
    scanf(" %c",&unit3);
    printf("Your age is %d",age);
    printf("Your grade for unit 1 is %c\n",unit1);
    printf("Your grade for unit 2 is %c\n",unit2);
    printf("Your grade for unit 3 is %c\n",unit3);
    return 0;
}