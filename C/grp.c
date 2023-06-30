#include <stdio.h>
int main (){
    int a,b,c,d,e,f;
    char g,h;
    float k,j,i;
    printf("value of (signed)int: a=\n");
    scanf("%d",&a);
    printf("value of unsigned int: b=\n");
    scanf("%u",&b);
    printf("value of short (signed)int: c=\n");
    scanf("%hd",&c);
    printf("value of unsigned short int: d=\n");
    scanf("%hu",&d);
    printf("value of long (signed)int: e\n");
    scanf("%ld",&e);
    printf("value of long unsigned int: f=\n");
    scanf("%lu",&f);
    /*variables for char*/
    printf("value of (signed)char: g=\n");
    scanf("%g",&g);
    printf("value of unsigned char: h=\n");
    scanf("%c",&h);
    /*variables for float*/
    printf("value of float:k=\n");
    scanf("%f",&k);
    printf("value of double: j=\n");
    scanf("%lf",&j);
    printf("value of long double : i=\n");
    scanf("%Lf",&i);
   printf("The sum %d+%u+%hd+%hu+%ld+%lu=%d\n",a,b,c,d,e,f,a+b+c+d+e+f);
   if((a+b+c+d+e+f)>40){
    printf("the grade is =%c\n",g);
   }
   else{
    printf("You haven't achieved=%c\n",h);
   }
   printf("The multiplication of %f*%lf*Lf=%f\n",k,j,i,k*j*i);
    return 0;
}