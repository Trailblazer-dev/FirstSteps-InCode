#include<stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc,char *argv[]){
	int fd1,fd2;
	char buffer[512];
//open the source file
	fd1 = open(argv[1],O_RDONLY);
//check whether the file has opened successfully
	if(fd1<0){
	printf("errno= %d \n", errno);
	perror("main Error opening source file");
	exit(0);
	}
	else{
	  printf("Successful opened the source file\n");
	
	}
	fd2 = open(argv[2],O_WRONLY|O_CREAT|O_EXCL,0644);
	if(fd2<0){
			printf("errno = %d\n",errno);
			perror("Error opening the destination file");
			exit(1);
		
	}
	else{
 	  printf("successful opened the destination file\n");
	}
	ssize_t bytes_read;
	ssize_t bytes_written ;

	while((bytes_read= read(fd1,buffer, sizeof( buffer)))>0){
//write the read data to the destination file
	bytes_written= write(fd2, buffer, bytes_read);
	if(bytes_written != bytes_read){
		perror("Error writing to the destination file");
		close(fd1);
		close(fd2);	
		return 1;
	}
	}
	close(fd1);
	close(fd2);
	return 0;
}


