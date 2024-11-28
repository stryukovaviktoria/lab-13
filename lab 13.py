import csv
import json


# Створення CSV файлу з даними
def create_csv_file(file_name):
    data = [
        ["Назва журналу", "Ціна", "Тираж"],
        ["Журнал 1", 150, 10000],
        ["Журнал 2", 200, 15000],
        ["Журнал 3", 120, 8000]
    ]

    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Файл '{file_name}' успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні CSV файлу: {e}")


# Конвертація CSV у JSON
def csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        with open(json_file, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Файл '{csv_file}' успішно конвертовано у '{json_file}'.")
    except FileNotFoundError:
        print(f"Файл '{csv_file}' не знайдено.")
    except Exception as e:
        print(f"Помилка при конвертації файлів: {e}")


if __name__ == "__main__":
    csv_file = "magazines.csv"
    json_file = "magazines.json"

    # Створення CSV файлу
    create_csv_file(csv_file)

    # Конвертація CSV у JSON
    csv_to_json(csv_file, json_file)

import csv
import json

# Конвертація JSON у CSV і додавання нових рядків


def json_to_csv(json_file, csv_file):
    try:
        # Читання даних з JSON файлу
        with open(json_file, mode="r", encoding="utf-8") as file:
            data = json.load(file)

        # Запис даних у CSV файл та додавання нових рядків
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["назва", "ціна", "тираж"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

            # Додавання нових рядків
            new_data = [
                {"назва": "Журнал 4", "ціна": 180, "тираж": 12000},
                {"назва": "Журнал 5", "ціна": 250, "тираж": 17000}
            ]
            writer.writerows(new_data)

        print(f"Файл '{json_file}' успішно конвертовано у '{csv_file}' та додано нові рядки.")
    except FileNotFoundError:
        print(f"Файл '{json_file}' не знайдено.")
    except Exception as e:
        print(f"Помилка при конвертації файлів: {e}")


if __name__ == "__main__":
    json_file = "magazines.json"
    csv_file = "updated_magazines.csv"

    # Конвертація JSON у CSV з додаванням нових рядків
    json_to_csv(json_file, csv_file)
