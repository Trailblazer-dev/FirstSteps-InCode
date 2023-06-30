#include <stdio.h>
int main(){
    int t;
    printf("enter your points");
    scanf("%d",&t);
    if(t>=500){
        printf("Royal customer\n");
        t=t+10;
    }
    else{
        printf("Loyal customer\n");
    ++t;
    }
    printf("your total point is %d",t);
    return 0;
}