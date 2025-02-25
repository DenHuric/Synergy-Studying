#include <iostream>
#include <vector>
#include <limits>

using namespace std;

long long maxProductDP(vector<int>& nums, int k) {
    int n = nums.size();
    if (k > n) return 0; // Если k больше размера массива, решения нет

    // DP таблица: dp[i][j] - максимальное произведение, взяв j элементов из первых i
    vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, LLONG_MIN));

    // Базовый случай: произведение 0 элементов всегда 1
    for (int i = 0; i <= n; i++) {
        dp[i][0] = 1;
    }

    // Заполняем таблицу динамического программирования
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= min(i, k); j++) {
            // Берем максимум из двух вариантов:
            dp[i][j] = dp[i-1][j]; // Не берем текущий элемент
            if (dp[i-1][j-1] != LLONG_MIN) {
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] * nums[i-1]); // Берем текущий элемент
            }
        }
    }

    return dp[n][k];
}

int main() {
    int n, k;
    cout << "Введите количество элементов в массиве: ";
    cin >> n;

    vector<int> nums(n);
    cout << "Введите элементы массива: ";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    cout << "Введите количество элементов в подпоследовательности (k): ";
    cin >> k;

    long long result = maxProductDP(nums, k);
    cout << "Максимальное произведение подпоследовательности из " << k << " элементов: " << result << endl;

    return 0;
}
