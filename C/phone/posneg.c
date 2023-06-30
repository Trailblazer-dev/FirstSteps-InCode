//check given number is positive or negative or zero
#include<stdio.h>
int main(){
int num;
printf("enter any value");
scanf("%d",&num);
if(num>0){
printf("num is positive:%d",num);
}
if(num<0){
printf("number is negative :%d",num);
}
if(num==0){
printf("number is equal to zero:%d",num);
}
return 0;
}
