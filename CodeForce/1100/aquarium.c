#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

bool check(long long* a, int n, long long h, long long x) {
    long long water = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] < h) {
            water += h - a[i];
            if (water > x) return false;
        }
    }
    return water <= x;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        long long x;
        scanf("%d%lld", &n, &x);

        long long a[10000000];
        long long max_height = 0;

        for (int i = 0; i < n; i++) {
            scanf("%lld", &a[i]);
            if (a[i] > max_height) {
                max_height = a[i];
            }
        }

        long long low = 1;
        long long high = max_height + x;

        while (low < high) {
            long long mid = low + (high - low + 1) / 2;
            if (check(a, n, mid, x)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }

        printf("%lld\n", low);
    }

    return 0;
}
