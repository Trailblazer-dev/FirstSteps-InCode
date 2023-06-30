/*Write program that prompts the user to enter values to an array which was declared as  VALUES[5][6] then passes the array
 as an argument to a function which computes and returns the average of array values*/
#include<stdio.h>
int i,j;
int main(int values[5][6]){
    printf("Enter values for the elements\n");
    for(i=0;i<5;i++){
        for(j=0;j<6;j++){
            scanf("%d",&values[i][j]);
        }
    }
}
int array(int arr[5][6]){
    sum,avg;
    for(i=0;i<5;i++){
        for(j=0;j<6;j++){
            sum+=arr[i][j];
        }
    }
    for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            avg=sum/
        }
    }
}