#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(){
    char  name[10];
    printf("Enter your second name\n");
    fgets(name,sizeof(name),stdin);
    printf("%s",toupper(name));
    printf("Hello %s", name);
return 0;
}
