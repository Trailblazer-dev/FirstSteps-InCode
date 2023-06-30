#include<stdio.h>
int product(int a,int b){
    int c=a*b;
    if(c>15){
        printf("a=%d,b=%d,product=%d\n",a,b,c);
    return 1;
    }
    else
        return 0;
   
}
int main(){
    int x,y;
    printf("ENTER two integer x&y\n");
    scanf("%d%d",&x,&y);
    if(product(x,y)==1){
        printf("equal to one");
    }
    return 0;
}