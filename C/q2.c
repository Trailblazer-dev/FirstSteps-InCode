#include <stdio.h>
int main(){
    int numberofItems;
    float cost;
    printf("no of items bought");
    scanf("%d",&numberofItems);
    printf("cost of the items");
scanf("%f",&cost);
    if (cost<1000&&numberofItems>=3)
    {
     printf("special offer");}
     else if(cost>=1000) {
        printf("discount");
     }  /* code */
    
    else{
        printf("no special offer/discount");
    }
    return 0;
}