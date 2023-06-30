#include <stdio.h>
int main (){
    int Mike,Bruce;
    char d='A',c='B';
    printf("marks for Mike=");
    scanf("%d",&Mike);
    printf("marks for Bruce=");
    scanf("%d",&Bruce);
    if (Mike>=80){
        printf("well Mike done you have %c\n",d);
    }
    else{
        printf("Well Mike done you have %c\n",c);
    }
    if(Bruce>=80){
        printf("well Bruce done you have %c\n",d);
        }
        else{
            printf("well Bruce done you have %c\n",c);
        }
printf("thanks for taking part in the competition");
return 0;
}