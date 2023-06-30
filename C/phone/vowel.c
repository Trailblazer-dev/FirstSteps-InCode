//checking character is vowel or constant
#include<stdio.h>
int main(){
char c;
printf("enter character\n");
scanf("%c",&c);
if(c=='a'||c=='e'||c=='o'||c=='u')
{printf("The character is a vowel\n");
}
else 
printf("Character is constant" );
return 0;
}
