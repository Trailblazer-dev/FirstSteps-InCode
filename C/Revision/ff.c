//FUNCTION WITH RETURN TYPE AND NO PARAMETER
#include<stdio.h>
int add(){
    int x,z=10,y=3;
    x=z+y;
    return x;
}
int main(){
    //assigning return value to variable rs
    int rs=add();//function calling
    printf("add =%d",rs);
}