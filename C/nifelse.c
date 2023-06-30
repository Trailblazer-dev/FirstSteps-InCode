#include <stdio.h>
int main(){
    int teamA,teamB;
    printf("enter the goals for teamA=");
    scanf("%d",&teamA);
    printf("enter the goals for teamB=");
    scanf("%d",&teamB);
    if (teamA!=teamB){
        printf("teamA point is not equal to teamB\n");
if (teamA>teamB)
{printf("teamA has many point than teamB\n");
}
        else{
           printf("teamB has many point than teamA\n");
        }
    }
        else{
            printf("teamA and  teamB have equal points");
        }
    return 0;
}