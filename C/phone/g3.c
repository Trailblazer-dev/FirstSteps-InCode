//Greater value in 3 number using if statement
#include<stdio.h>
int main(){
int a,b,c;
printf("Enter the value of a&b&c");
scanf("%d%d%d",&a,&b,&c);
if(a>b&&a>c){
printf("a is %d is greater",a);
}
if(b>a&&b>c){
printf("b is %d is greater ",b);
}
if(c>a&&c>b){
printf("c is %d is greater",c);
}
return 0;
}
