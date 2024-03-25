#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main (){
    int fd[2];
    //The 2 parameters are 0(read) and 1(write)
    //We shall used pipes which return 0 when successful and -1 otherwise
    if(pipe(fd) == -1){
        printf("Error occurred with openning pipe\n");
        return 1;
    }
    int id = fork();
    if(id ==0){
        close(fd[0]);
        int x;
        printf("Input a number \n");
        scanf("%d",&x);
        if(write(fd[1],&x,sizeof(int))==-1){
            printf("Error occurred with writing to pipe\n");
            return 2;
        }
        close(fd[1]);
    }
    else{
        close(fd[1]);
        int y;
        if(read(fd[0],&y,sizeof(int))==-1){
            printf("Error occurred with reading from pipe\n");
            return 3;
        }
        close(fd[1]);
        printf("We got from the child process %d\n",y);
    }
    return 0;
}