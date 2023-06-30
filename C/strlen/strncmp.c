//strncmp compare a specific no of the string the syntax is strncmp(s1,s2,10)
#include<stdio.h>
#include<string.h>
int main(){
    char n[10]="Goodmorning girl";
    char nd[10]="Goodmorning boy";
    if(strncmp(n,nd,14)==0){
        printf("they are equal");
    }
    else{
    printf("there are different");
    }
printf("\n%s",nd);
return 0;
}