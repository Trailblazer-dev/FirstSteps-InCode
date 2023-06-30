#include<stdio.h>
int main(){
int d,sum;
do{
printf("%d\n",d);
++d;
sum+=d;}
while(d<12);
printf("sum%d",sum);
return 0;
}
