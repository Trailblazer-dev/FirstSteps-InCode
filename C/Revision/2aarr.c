#include<stdio.h>
int main(){
    int ran[4][5],x,j,sum,avg;
    for(x=1;x<4;x++){
        for(j=1;j<5;j++){
           printf("enter value [%d][%d]:",x,j);
           scanf("%d",ran[x][j]);
        }
    }
    for(x=1;x<4;x++){
        for(j=1;j<5;j++){
            printf("%d",ran[x][j]);
            sum+=ran[x][j];
            avg=sum/20;
        }
    }
    printf("sum:%d\n",sum);
    printf("the average:%d",avg);
    return 0;
}