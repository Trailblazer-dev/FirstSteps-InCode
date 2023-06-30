#include <stdio.h>
int main (){
    int k,j;
    printf("enter the value of k:");
    scanf("%d",&k);
    printf("eneter value of j:");
    scanf("%d",&j);
    if (k>j){
        printf("k is greater than j\n");
    }
    if(j>k){
        printf("j is greater than k\n");
    }
    printf("end of program");
    return 0;
}