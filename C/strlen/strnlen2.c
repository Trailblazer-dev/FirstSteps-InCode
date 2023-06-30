#include<stdio.h>
#include<string.h>
int main (){
        /*Write a program in C that reads a string from the user and determines
         its length, but limits the maximum number of characters that can be read to */
    char Reg[14],T;
    //Am writing a program that prompt the user to enter his reg no;
    printf("Enter your Registration number\n");
    fgets(Reg,sizeof(Reg),stdin);
    if(strnlen(Reg, 12)){
        printf("I is your Reg number %s ?",Reg);
    }
    else {
    printf("Try again entering your Reg number\n");
    fgets(Reg,sizeof(Reg),stdin);
    if(strnlen(Reg,12)){
        printf("Is your Registration number %s ?\t",Reg);
    }
}
    printf("press Y if it is and N is it not\t",Reg);
    scanf("%c",&T);
    if(toupper(T)=='Y'){
            printf("Thank you %s ",Reg);
    }
    else
    printf("\nSorry try again later");
return 0;
}