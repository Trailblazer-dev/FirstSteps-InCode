#include<stdio.h>
int main(){
    int ran[5],x,sum,avg;
    for(x=0;x<5;++x){
        printf("Enter the number%d\n",x);
        scanf("%d",&ran[x]);}
        for(x=0;x<5;++x){
    sum+=ran[x];
    avg=sum/5;}
printf("the sum%d",sum);
printf("\naverage is%d",avg);
    return 0;
}