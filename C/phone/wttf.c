#include<stdio.h>
int main(){
int d,sum;
for(d=3;d<21;++d){
if(d==7){
continue;
}
printf("%d\n",d);
sum+=d;
}
printf("sum%d",sum);
return 0;
}
