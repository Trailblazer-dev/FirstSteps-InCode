#include<stdio.h>
int main(){
int number[10],i=0,sum=0,y,x=0;
float average;
printf("Now taking then numbers from the keyboard\n\n\n");
printf("Please enter number\n");
while(i<10){
  scanf("%d\n",&y);
  number[i]=y;
  sum+=y;
  i+=1;
}
average=sum/i;
printf("average for i:%f",average);
while(x<10){
   printf("%d",number[x]);
   sum+=number[x];
   x+=1;
}
printf("\nsum:%d",sum);
average= sum/x;
printf("\naverage for x =%f",average);
return 0;
}
