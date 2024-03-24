#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<sys/wait.h>
int main(int argc,char *argv[]){
    int id = fork();
    if(id ==0){
        sleep(1);
    }
    
    printf("The currentID is %d  and the parentID is %d\n",getpid(),getppid());
    int result = wait(NULL);
    if(result == -1){
        printf("No children to wait for\n");
        
    }
    else{
        printf("%d finished execution\n",result);
    }

    return 0;
}