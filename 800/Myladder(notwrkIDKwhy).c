#include <stdio.h>
#include <stdlib.h>

struct shag
{
    int n;
    int *a;
    int c;

};

void step(int *a, int n,int *c, int  *sum){
    if (*c == n-1){
        *sum += a[n-1];
        *c += 1;
    }
    else if (a[*c]>=0){
        *sum += a[*c];
        *c += 1;
    }
    else if (a[*c]<0){
        if (a[*(c)+1]<0){
            //printf("\nalo %d %d\n", a[*c], a[*(c)+1]);
            if (a[*c]>=a[*(c)+1]){
                *sum += a[*c];
                *c += 1;
            }
            else {
                *sum += a[*(c)+1];
                *c += 2;
            }
        }
        else{
            *sum += a[*(c)+1];
            *c +=2;
        }
    }
}

int main(){
    struct shag shagg;

    FILE *in = fopen("ladder.in", "r");
    FILE *out =fopen("ladder.out", "w");

    fscanf(in, "%d",&shagg.n);
    shagg.a = (int*)malloc(shagg.n*sizeof(int));


    for (int i = 0;i<shagg.n;i++){
        fscanf(in, "%d",&shagg.a[i]);
    }

    int c = 0 , sum = 0;
    //printf("%d %d\n",c,sum);

    // for (int i = 0;i<4;i++){
    //     step(shagg.a,shagg.n,&c,&sum);
    //     printf("%d %d\n",c,sum);
    // }

    while (c<shagg.n){
        step(shagg.a,shagg.n,&c,&sum);
        //printf("%d %d\n",c,sum);
    }

    fprintf(out, "%d",sum);

    fclose(in);
    fclose(out);
}
