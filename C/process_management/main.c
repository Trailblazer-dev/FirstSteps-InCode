#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]) {
    int id = fork();
    //printf("Hello, world from : %d\n",id);
    if(id==0){
        printf("Hello, world from child\n");
    }
    else{
        printf("Hello, world from main\n");
    }
    return 0;
}
