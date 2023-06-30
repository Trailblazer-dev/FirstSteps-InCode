#include <stdio.h>
int main(int argc, char const *argv[])
{
int a=4,b=4,c;
c= a+b;
printf("line 1=%d\n",c);
c=a*b;
printf("line 2=%d\n",c);
c=++a;
printf("line 3=%d\n",c);
c=b--;
printf("line 4=%d\n",c);
c=((++a)*(b--));
printf("line 5=%d\n",c);
return 0;
}
