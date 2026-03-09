#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    int a,b,c,T;
    scanf("%d %d %d %d", &a, &b, &c, &T);
    if ((a==b) && (a==c)){
        printf("%d", (T/a)+1); //xz chto eto
        return 0;
    }

    int s1 = T/a+1,s2 = T/b+1,s3 = T/c+1; //sizes massivov

    int *m1 = (int*)calloc(s1, sizeof(int));
    int *m2 = (int*)calloc(s2, sizeof(int));
    int *m3 = (int*)calloc(s3, sizeof(int));

    int c1 = 0,c2 = 0,c3 = 0; //счетчики ну пон

    for (int i = 0; i < T; i++)
    {
        if ((i%a)==0 && c1 < s1){
            m1[c1] = i;
            c1++;
        }
        if (i%b==0 && c2 < s2){
            m2[c2] = i;
            c2++;
        }
        if (i%c==0 && c3 < s3){
            m3[c3] = i;
            c3++;
        }
    }

    // printf("\n");
    // for (int i = 0; i < c1; i++)
    // {
    //     printf("%d ", m1[i]);
    // }
    // printf("\n");
    // for (int i = 0; i < c2; i++)
    // {
    //     printf("%d ", m2[i]);
    // }
    // printf("\n");
    // for (int i = 0; i < c3; i++)
    // {
    //     printf("%d ", m3[i]);
    // }

    int times[100000];
    int time_cnt = 0;
    bool used[s1] = {0};

    // m1 ∩ m2
    for (int i = 0; i < c1; i++) {
        if (used[i]) continue;
        for (int j = 0; j < c2; j++) {
            if (m1[i] == m2[j]) {
                times[time_cnt++] = m1[i];
                used[i] = 1;
                break;
            }
        }
    }

    // m1 ∩ m3
    for (int i = 0; i < c1; i++) {
        if (used[i]) continue;
        for (int k = 0; k < c3; k++) {
            if (m1[i] == m3[k]) {
                times[time_cnt++] = m1[i];
                used[i] = 1;
                break;
            }
        }
    }

    // m2 ∩ m3
    for (int j = 0; j < c2; j++) {
        for (int k = 0; k < c3; k++) {
            if (m2[j] == m3[k]) {
                int already = 0;
                for (int t = 0; t < time_cnt; t++) {
                    if (times[t] == m2[j]) already = 1;
                }
                if (!already) time_cnt++;
                break;
            }
        }
    }

    printf("%d\n", time_cnt);

    return 0;
}

//сейчас решено на 33 балла вроде чет такое
