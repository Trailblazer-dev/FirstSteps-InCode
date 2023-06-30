//these code is about how to use the string function strcmp
#include<stdio.h>
#include<string.h>
int main(){
    char day[10],month[10];
    printf("Enter the day of week followed by month which you are in \n");
    fgets(day,sizeof(day),stdin);
    fgets(month,sizeof(month),stdin);
    if(strcmp(day,month)==0){
        printf("the two are equal");
    }
    else
    printf("The two are different");
return 0;   
}