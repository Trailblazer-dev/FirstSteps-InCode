#include<stdio.h>
#include<string.h>
int main (){
    char sim[30];
    printf("Enter the cellular service provider you have ever used\n");
    fgets(sim,sizeof(sim),stdin);
    printf("The total length of the details you provided above is %d\n",strlen(sim));
    printf("The size of the array was %d\n", sizeof(sim));
    printf("Your have entered %s",sim);
return 0;
}