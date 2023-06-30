#include<stdio.h>
int main(){
    int i,j;
    int matrix[2][3]={{2, 3, 4}, {8, 6, 4}};
    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            printf("The matrix is %d\n",matrix[i][j]);
        }
    }
    printf("\nThe matrix is %d",matrix);
return 0;
}