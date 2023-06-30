//alternative
#include<stdio.h>
int main(){
char c;
printf("enter alphabet\n");
scanf("%c",&c);
switch(c){
case'a':
case'e':
case'o':
case'u':
printf("is a vowel:%c",c);
break;
default:
printf("is a vowel:%c",c);
}
return 0;
}
