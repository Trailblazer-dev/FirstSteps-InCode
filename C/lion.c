#include<stdio.h>
#define N 10
int main (){
int number,sum,count;
float average;
sum=0;
count=0;
printf("enter number ");
scanf("%d\n",&number);
while(count<N){
sum+=number;
count+=1;
}
printf("sum %d\n",sum);
average = sum/N;
printf("average :%f\n",average);
return 0;
}

