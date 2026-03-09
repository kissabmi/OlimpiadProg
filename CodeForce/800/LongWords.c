#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d",&n);
    for (size_t i = 0; i < n; i++)
    {
        char *str = malloc(1000);
        scanf("%s", str);
        int lenght = strlen(str);
        realloc(str, lenght+1);
        if (lenght>10){
            char first = str[0];
            char last = str[lenght-1];
            printf("\n%c%d%c", first,lenght-2,last);
        }
        else {
            printf("\n%s", str);
    }
}
}

