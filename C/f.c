#include<stdio.h>
int a[2][2],b[2][2],c[2][2];
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
//add the sum of matrices
array();
for(i=0;i<2;i++){
   for(j=0;j<2;j++){
    c[i][j]=a[i][j]+b[i][j];
}
}
for(i=0;i<2;i++){
    for(j=0;j<2;j++){
 printf("the sum is %d\n",c[i][j]);
}
}
return 0;
}
