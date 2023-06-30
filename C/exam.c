#include<stdio.h>
int main(){
    int values[5][6],i,j;
    int sum;
    printf("Enter the values for the element\n");
    for(i=0;i<5;i++){
        for(j=0;j<6;j++){
            scanf("%d",&values[i][j]);
        }
    }
    //sum
    for(i=0;i<5;i++){
        for(j=0;j<6;j++){
            sum +=values[i][j];
        }
    }
    //output
    for(i=0;i<5;i++){
        for(j=0;j<6;j++){
            printf("The sum is %d",values);
        }
    }
    return 0;
}