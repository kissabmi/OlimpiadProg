#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    freopen("ladder.in", "r", stdin);
    freopen("ladder.out", "w", stdout);

    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }

    int a[101];
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }

    int dp[101];

    dp[0] = 0;

    dp[1] = a[1] + dp[0];

    for (int i = 2; i <= n; i++) {
        dp[i] = a[i] + max(dp[i-1], dp[i-2]);
    }

    printf("%d", dp[n]);

    return 0;
}
