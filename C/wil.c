#include<stdio.h>
int main(){
int s,sum,r=0;
printf("enter values of number");
for(s=0;s<10;++s){
scanf("%d",&r);
++r;
sum +=r;
}
printf("the sum is %d",sum);
return 0;
}
