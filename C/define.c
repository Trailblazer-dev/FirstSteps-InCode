#define SALESTAX 0.05
#include<stdio.h>
int main(){
    float amount,total,taxes;
    printf("Enter the amount purchased:\n");
    scanf("%f",&amount);
    taxes=SALESTAX*amount;
    printf("The sales tax is %4.2f",taxes);
    printf("\n The total bill is %5.2f",total);
return 0;
}