#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Функция для нахождения минимального количества монет
int minCoins(vector<int>& coins, int amount) {
    sort(coins.rbegin(), coins.rend()); // Сортируем номиналы в порядке убывания
    int count = 0;

    for (int coin : coins) {
        if (amount >= coin) {
            count += amount / coin; // Берем максимально возможное количество данной монеты
            amount %= coin; // Оставшаяся сумма
        }
    }

    return (amount == 0) ? count : -1; // Если сумма набрана, возвращаем count, иначе -1 (невозможно набрать сумму)
}

int main() {
    vector<int> coins = {1, 5, 10, 25, 50}; // Доступные номиналы монет
    int amount;

    cout << "Введите сумму, которую нужно набрать: ";
    cin >> amount;

    int result = minCoins(coins, amount);
    if (result != -1) {
        cout << "Минимальное количество монет: " << result << endl;
    } else {
        cout << "Невозможно набрать данную сумму имеющимися монетами." << endl;
    }

    return 0;
}
