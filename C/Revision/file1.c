#include<stdio.h>
void trial();
int main(){
    FILE *tears;
    tears=fopen("test.txt","w");
    fprintf(tears,"Am quite happy am almost done studying c\n");
    fclose(tears);
trial();
return 0;
}
void trial(){
    FILE *joy;
    joy =fopen("test.txt","a");
    fprintf(joy,"It feels so good to end sth ");
    fclose(joy);
}