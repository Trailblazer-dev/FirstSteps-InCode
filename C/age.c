#include <stdio.h>
int main(){
    int age;
    char unit3,unit1,unit2;
    printf("enter your age");
    scanf("%d",&age);
    printf("enter the grade for unit3\n");
    scanf("%c\n",&unit3);
    printf("enter grade for unit1 \n");
    scanf("%c\n",&unit1);
    printf("enter the grade for unit2 \n");
    scanf("%c\n",&unit2);
    printf("your age is :%d\n",age);
    printf("your grade is for unit1 =%c\n",unit1);
    printf("your grade is for unit2 =%c\n",unit2);
    printf("your grade is for unit3=%c",unit3);
    return 0;
}