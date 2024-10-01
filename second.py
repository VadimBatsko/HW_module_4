from pathlib import Path


'''Друге завдання'''
def get_cats_info(path):
    cats_dicts = []
    # Робимо перевірку на папку
    if Path(path).is_dir():
            return 'Ви обрали папку'
    # Перевіряєм чи правильне ім'я файлу 
    try:
        # Відкриваєм файл і читаєм по рядку
        with open(path, 'r', encoding="utf-8") as test:
            one_line = test.readlines()

            # Перевіряєм чи файл пустий
            if not any(i.strip() for i in one_line):
                return "Файл пустий"
            # Проходимо по рядках
            for i in one_line:
                # Розділяєм на список щоб мати доступ
                split_text = i.strip().split(',')
                # Перевіряєм чи є всі параметри і якщо кіт дворовий то вік невідомий.Після перевірки додаємо до ліста
                if len(split_text) == 3:
                    cats_dicts.append({"id":split_text[0], "name":split_text[1], "age":split_text[2]})
                elif len(split_text) == 2:
                    cats_dicts.append({"id":split_text[0], "name":split_text[1], "age":"Невідомо"})
            return cats_dicts
    except FileNotFoundError:
        return "Неправильне ім'я файлу"
    