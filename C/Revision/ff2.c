//FUNCTION WITH RETURN TYPE AND NO PARAMETER
#include<stdio.h>
int add(int z,int y){
    int x;
    x=z+y;
    return x;
}
int main(){
    //assigning return value to variable rs
    int rs=add(10,3);//function calling
    printf("add =%d",rs);
}