//omg my first zadacha(task idk) that correct at first try!111

#include <stdio.h>

int maxx(int* arr, int n ){
    int maxx = 0;
    for (int i = 0;i<n;i++){
        if (arr[i]>maxx){
            maxx = arr[i];
        }
    }
    return maxx;
}

int main(){
    int n;
    scanf("%d", &n);
    int work[n];
    for (size_t i = 0; i < n; i++)
    {
        scanf("%d", &work[i]);
        //printf("%d", work[i]);
    }

    int relax[n];
    int c = 0;

    for (size_t i = 0; i < n; i++)
    {
        relax[i] = 0;
    }

    for (size_t i = 0; i < n; i++)
    {
        if (work[i]==1){
            relax[c]++;
        }
        else {
            c++;
        }
            //printf("c: %d ", c);
            //printf("i: %ld ", i);
    }

    if ((relax[0]!=0) && (relax[c]!=0)){
        relax[c] = relax[0]+relax[c];
        relax[0] = 0;
    }

    printf("%d", maxx(relax,n));

    // for (size_t i = 0; i < n; i++)
    // {
    //     printf("%d ", relax[i]);
    // }
}
