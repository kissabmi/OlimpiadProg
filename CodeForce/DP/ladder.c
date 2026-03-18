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

    dp[1] = a[1];

    for (int i = 2; i <= n; i++) {
        dp[i] = a[i] + max(dp[i-1], dp[i-2]); //просто смотрим что нам выгоднее из двух и то используем
    }

    printf("%d", dp[n]); //наш ответ - конец лестницы (т.е максимальная сумма)

    return 0;
}

/* 2 СЛУЧАЙ РЕШЕНИЯ

//массив заполнили маленькими числами т.к ищем максимум.
for (int i = 0; i <= n; i++) dp[i] = -999999;

dp[0] = 0;

for (int i = 0; i < n; i++) {
    //предлагаем свой результат следующей ступеньке (шаг на 1)
    if (dp[i] + a[i+1] > dp[i+1]) {
        dp[i+1] = dp[i] + a[i+1];
    }

    //предлагаем свой результат через одну ступеньку (шаг на 2)
    if (i + 2 <= n && dp[i] + a[i+2] > dp[i+2]) {
        dp[i+2] = dp[i] + a[i+2];
    }
}
//ответ так же лежит в dp[n]

*/

/* 3 СЛУЧАЙ РЕШЕНИЯ

int solve(int i, int n, int a[], int dp[]) {
    //базовый случай: дошли до начала
    if (i == 0) {
        return 0;
    }

    //уже считали - возвращаем из кэша
    if (dp[i] != -1) {
        return dp[i];
    }

    //рекурсивно вычисляем максимум из двух вариантов
    int oneStep = solve(i - 1, n, a, dp) + a[i];
    int twoSteps = (i >= 2) ? solve(i - 2, n, a, dp) + a[i] : -999999;

    dp[i] = max(oneStep, twoSteps);
    return dp[i];
}

int main_recursion() {
    int n;
    scanf("%d", &n);

    int a[101];
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }

    //массив dp заполняем -1 (означает "ещё не посчитано")
    int dp[101];
    for (int i = 0; i <= n; i++) {
        dp[i] = -1;
    }

    int result = solve(n, n, a, dp);
    printf("%d", result);

    return 0;
}

*/
