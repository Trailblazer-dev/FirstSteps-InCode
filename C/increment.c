#include<stdio.h>
int main(){
   int a=3,b=2,c;
    c=++a;
    printf("line 1 a=%d\n",c);
    c=a++;
    printf(";ine 2 a= %d\n",c);
    c=++b;
    printf("line 3 b=%d\n",c);
    c=b++;
    printf("line 4 b= %d\n",c);
    c=++a;
    printf("line 5 a=%d",c);
    return 0;
}