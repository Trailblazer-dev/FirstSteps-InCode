#include<stdio.h>
#include<string.h>
int main(){
char s1[20]="beginners book";
char s2[20]="beginners.com";
if (strcmp(s1,s2)==0){
printf("string 1 and 2 are equal");
}
else{
printf("string 1 and 2 are diffeetent");
}
return 0;
}
