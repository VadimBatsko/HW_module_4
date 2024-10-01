from pathlib import Path

'''Перше завдання'''
def total_salary(path):
    sum_sallary = 0
    # Перевіряєм імя файлу
    try:
        # Перевірка чи це папка
        if Path(path).is_dir():
            return 'Ви обрали папку'
        # Відкриваєм файл і читаєм по рядку
        with open(path, 'r', encoding="utf-8") as test:
            one_line = test.readlines()

            # Перевіряєм чи файл пустий
            if not any(i.strip() for i in one_line):
                return "Файл пустий"
            # Ітеруємо по рядках і додаєм кожен другий елемент до sum_sallary як число
            for i in one_line:
                # Розділяєм у список
                split_text = i.strip().split(',')
                # Обробка помилок
                try:
                    sum_sallary += int(split_text[1])
                except IndexError:
                    return "Число за індеском відсутнє"
                except ValueError:
                    return "ЗП не є числом"
    except FileNotFoundError:
        return 'Файл не знайдено'
    return sum_sallary, sum_sallary // len(one_line)

