# Данные из базы (для примера)
correct_login = "user123"
correct_password = "pass456"

# Счётчик попыток
attempts = 0
max_attempts = 3

# Цикл while — повторяем, пока попытки не закончились
while attempts < max_attempts:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    if login == correct_login and password == correct_password:
        print("Авторизация успешна! Добро пожаловать!")
        break  # Выходим из цикла, так как вход выполнен
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Неверный логин или пароль. Осталось попыток: {remaining}")

# Если цикл завершился без break (все попытки исчерпаны)
else:
    print("Доступ заблокирован. Слишком много неудачных попыток.")