from collections import defaultdict
from functools import reduce
import datetime

# Підготовка даних (список словників)
sports_data = [
    {"date": "2026-10-01", "player": "s1mple", "sport": "CS2", "score": 25, "tournament": "Major"},
    {"date": "2026-10-02", "player": "Yatoro", "sport": "Dota 2", "score": 18, "tournament": "The International"},
    {"date": "2026-10-03", "player": "b1t", "sport": "CS2", "score": 22, "tournament": "FACEIT Pro League"},
    {"date": "2026-10-04", "player": "Dendi", "sport": "Dota 2", "score": 12, "tournament": "The International"},
]

# === Функції для базових операцій (CRUD) ===

def add_result(data, result):
    """Додає новий спортивний результат."""
    data.append(result)
    print("Результат додано успішно.")

def remove_result(data, index):
    """Видаляє результат за індексом."""
    if 0 <= index < len(data):
        del data[index]
        print("Результат видалено успішно.")
    else:
        print("Невірний індекс.")

def update_result(data, index, key, value):
    """Оновлює інформацію про результат."""
    if 0 <= index < len(data):
        data[index][key] = value
        print("Інформацію оновлено успішно.")
    else:
        print("Невірний індекс.")

# === Функції аналізу та фільтрації ===

def find_by_player(data, player):
    """Знаходить всі результати конкретного гравця (використовує filter)."""
    return list(filter(lambda x: x["player"] == player, data))

def calculate_total_score(data):
    """Обчислює загальну суму всіх очок (використовує reduce)."""
    return reduce(lambda acc, res: acc + res["score"], data, 0)

def group_by_sport(data):
    """Групує результати за дисципліною (використовує defaultdict)."""
    categories = defaultdict(list)
    for res in data:
        categories[res["sport"]].append(res)
    return dict(categories)

def sort_by_date(data):
    """Сортує результати за датою."""
    return sorted(data, key=lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%d"))

def get_top_3_results(data):
    """Повертає Топ-3 найкращих результатів (використовує сортування та ЗРІЗИ)."""
    sorted_data = sorted(data, key=lambda x: x["score"], reverse=True)
    return sorted_data[:3]  # Зріз списку

def show_unique_stats(data):
    """Демонструє роботу з МНОЖИНАМИ (set) та функцією map()."""
    # Отримуємо списки через map
    tournaments = set(map(lambda x: x["tournament"], data))
    sports = set(map(lambda x: x["sport"], data))
    
    print(f"Унікальні турніри: {tournaments}")
    print(f"Унікальні дисципліни: {sports}")
    print(f"Об'єднання множин: {tournaments | sports}") # Операція об'єднання

# === Інтерактивне меню ===

def print_menu():
    print("\n==== Меню аналізу кіберспортивних результатів ====")
    print("1. Показати всі результати")
    print("2. Додати новий результат")
    print("3. Видалити результат")
    print("4. Оновити інформацію")
    print("5. Знайти результати за нікнеймом гравця")
    print("6. Загальна сума набраних очок")
    print("7. Групувати за дисципліною")
    print("8. Сортувати за датою")
    print("9. Показати Топ-3 найкращих результатів")
    print("10. Унікальна статистика турнірів")
    print("0. Вийти")

def main():
    global sports_data
    while True:
        print_menu()
        choice = input("Оберіть опцію: ")
        
        if choice == "1":
            for i, res in enumerate(sports_data):
                print(f"{i}: {res}")
                
        elif choice == "2":
            date = input("Введіть дату (YYYY-MM-DD): ")
            player = input("Введіть нікнейм гравця: ")
            sport = input("Введіть дисципліну: ")
            score = int(input("Введіть кількість очок (кілів): "))
            tournament = input("Введіть назву турніру: ")
            new_result = {"date": date, "player": player, "sport": sport, "score": score, "tournament": tournament}
            add_result(sports_data, new_result)
            
        elif choice == "3":
            index = int(input("Введіть індекс для видалення: "))
            remove_result(sports_data, index)
            
        elif choice == "4":
            index = int(input("Введіть індекс для оновлення: "))
            key = input("Введіть ключ (date/player/sport/score/tournament): ")
            if key == "score":
                value = int(input("Введіть нове значення очок: "))
            else:
                value = input("Введіть нове значення: ")
            update_result(sports_data, index, key, value)
            
        elif choice == "5":
            player = input("Введіть нікнейм для пошуку: ")
            results = find_by_player(sports_data, player)
            for res in results:
                print(res)
                
        elif choice == "6":
            total = calculate_total_score(sports_data)
            print(f"Загальна сума всіх очок: {total}")
            
        elif choice == "7":
            grouped = group_by_sport(sports_data)
            for sport, results in grouped.items():
                print(f"\n{sport}:")
                for res in results:
                    print(f"  {res}")
                    
        elif choice == "8":
            sorted_res = sort_by_date(sports_data)
            for res in sorted_res:
                print(res)
                
        elif choice == "9":
            top_3 = get_top_3_results(sports_data)
            print("\nТоп-3 результати:")
            for res in top_3:
                print(res)
                
        elif choice == "10":
            show_unique_stats(sports_data)
            
        elif choice == "0":
            print("Дякуємо за використання програми!")
            break
            
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
