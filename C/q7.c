#include<stdio.h>
int main(){
    int n,sum=0,a=1;
    float avg;
    printf("Enter how many number you want:\n");
    scanf("%d",&n);
    printf("Enter number one by one\n");
    do{
        scanf("%d",&n);
        sum=sum+n;
        a++;
    }
    while (a<16);
avg=sum/n;
printf("\nsum of %dnumber=%d",n,sum);
printf("\nAverage of the%d numbers=%f",n,avg);
return 0;

}