#include <stdio.h>

int main(){
    long long n,m,a;
    scanf("%lld %lld %lld", &n, &m, &a);
    printf("%lld",((m+a-1)/a)*((n+a-1)/a));
}
