def add_pet_to_dictionary():
    pets = {}  # Пустой словарь для хранения информации о питомцах

    # Запрос информации о питомце
    pet_name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца (например, собака, кошка, питон): ")
    pet_age = int(input("Введите возраст питомца (целое число): "))
    owner_name = input("Введите имя владельца питомца: ")

    # Заполнение словаря информацией
    pets[pet_name] = {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name
    }

    return pets

# Функция для определения правильной формы слова "год" в зависимости от числа
def correct_age_ending(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

# Шаг 2: Вывод информации о питомце
def print_pet_info(pets):
    for pet_name, details in pets.items():
        age_ending = correct_age_ending(details["Возраст питомца"])
        print(f'Это {details["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {details["Возраст питомца"]} {age_ending}. Имя владельца: {details["Имя владельца"]}')

# Создание и вывод информации о питомце
pets = add_pet_to_dictionary()
print_pet_info(pets)
