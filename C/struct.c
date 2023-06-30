#include<stdio.h>
	struct Mystructure{
		int num;
		char letter;
	};
	int main (){
		struct Mystructure s1;
		s1.num=100;
		s1.letter='a';
		printf("%d\n%c",s1.num,s1.letter);
return 0;
}

