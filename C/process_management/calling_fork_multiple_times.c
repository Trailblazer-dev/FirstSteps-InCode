#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<errno.h>
int main (int argc, char *argv[]) {
    int id = fork();
    int id2 = fork();
    if(id ==0){
        if(id2 ==0){
            printf("We are process y\n");
        }
        else{
            printf("We are process x\n");
        }
    }
    else{
        if(id2 ==0){
            printf("we are process z\n");
        }
        else{
            printf("we are the parent process \n");
        }
    }
    
    while(wait(NULL)!=-1 || errno != ECHILD ){
        printf("Waited for the child process to finish\n");
        //it will appear 3 type since there are 3 children 
    }
    return 0;   
}