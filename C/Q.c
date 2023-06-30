//a program which convert a person name into abbrievation
#include <stdio.h>
int main(){
    char fn[10],mn[10],ln[10];
    printf("Enter your first name \n");
    fgets(fn,sizeof(fn),stdin);
    printf("Enter your second name\n");
    fgets(mn,sizeof(mn),stdin);
    printf("Enter your last name\n");
    fgets(ln,sizeof(ln),stdin);
printf("Hello %c.%c.%c",fn[0],mn[0],ln[0]);
return 0;
}