#include<stdio.h>
#include<string.h>
int main(){
char d[20]="use an AI ?";
	printf("length of the str. when the maxlen is 30.%d",strnlen(d ,20));
	printf("length of the str. when the maxlen is 10.%d",strnlen(d ,10));
return 0;
}
