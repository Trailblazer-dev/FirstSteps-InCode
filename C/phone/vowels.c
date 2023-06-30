//using switch
#include<stdio.h>
int  main(){
char c;
printf("Enter alphabet\n");
scanf("%c",&c);
switch(c){
case'a':
printf("it is vowel:%c",c);
break;
case'e':
printf("is a vowel :%c",c);
break;
case'o':
printf("is a vowel:%c",c);
break;
case'u':
printf("is a vowel:%c",c);
break;
default:
printf("is a consonont:%c",c);}
return 0;
}
