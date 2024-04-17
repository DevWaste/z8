my_dict = {}
for i in range(10, -6, -1):  # Цикл от 10 до -5 включительно
    if i != 0:
        my_dict[i] = i ** i  # Возведение числа i в степень i
    else:
        my_dict[i] = 1  # Обработка случая для i = 0, так как 0 в степени 0 считается равным 1

# Печать результатов
for key, value in my_dict.items():
    print(f"{key}: {value}")
