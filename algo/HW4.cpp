#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Структура для хранения информации о занятии
struct Activity {
    int start, end;
};

// Функция для выбора максимального количества занятий
int maxActivities(vector<Activity>& activities) {
    // Сортируем занятия по времени окончания
    sort(activities.begin(), activities.end(), [](const Activity& a, const Activity& b) {
        return a.end < b.end;
    });

    int count = 0, last_end_time = 0;
    vector<Activity> selected; // Вектор для хранения выбранных занятий

    // Перебираем занятия в порядке возрастания времени окончания
    for (const auto& activity : activities) {
        if (activity.start >= last_end_time) { // Если занятие не пересекается с предыдущим
            selected.push_back(activity);
            last_end_time = activity.end;
            count++;
        }
    }

    // Вывод выбранных занятий
    cout << "Максимальное количество занятий: " << count << endl;
    cout << "Выбранные занятия (начало, конец): ";
    for (const auto& act : selected) {
        cout << "(" << act.start << ", " << act.end << ") ";
    }
    cout << endl;

    return count;
}

int main() {
    int n;
    cout << "Введите количество занятий: ";
    cin >> n;

    vector<Activity> activities(n);
    cout << "Введите время начала и окончания занятий (через пробел):" << endl;
    for (int i = 0; i < n; i++) {
        cin >> activities[i].start >> activities[i].end;
    }

    maxActivities(activities);

    return 0;
}
