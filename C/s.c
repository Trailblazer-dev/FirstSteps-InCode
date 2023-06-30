#include<stdio.h>
#include<string.h>
int main() {
    char comp[20];
    printf("Enter the name of computer you use\n");
    scanf("%s",&comp);
    printf("the length of your computer name is %ld",strlen(comp));
return 0;
}