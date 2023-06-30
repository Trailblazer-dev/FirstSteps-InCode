#include<stdio.h>
int a[2][2],b[2][2],a2[2][2],b2[2][2];
int array(){
int i,j;
printf("enter the element for the first matrices\n");
for(i=0;i<2;i++){
  for(j=0;j<2;j++){
   scanf("%d",&a[i][j]);
}
}
printf("enter the element for second matrice\n");
for(i=0;i<2;i++){
   for(j=0;j<2;j++){
   scanf("%d",&b[i][j]);
}
}
}
int main(){
int i,j;
//square two  matrices
array();
for(i=0;i<2;i++){
   for(j=0;j<2;j++){
    a2[i][j]=a[i][j]*a[i][j];
}
}
for(i=0;i<2;i++){
   for(j=0;j<2;j++){
    printf("the square of a is %d \n",a2[i][j]);
}
}
for(i=0;i<2;i++){
    for(j=0;j<2;j++){
    b2[i][j]=b[i][j]*b[i][i];
}
}
for(i=0;i<2;i++){
   for(j=0;j<2;j++){
    printf("the square of b is %d \n",b2[i][j]);
}
}
return 0;
}
