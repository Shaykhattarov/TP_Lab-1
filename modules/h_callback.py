def success(login):
    status_code = 200
    return [status_code, login]


def failure(login, error_message):
    status_code = 404
    return [status_code, login, error_message]


def ask_password(login, password, success, failure):
    val_vowel = True
    val_consonant = True

    vowel_ru = ["a", "е", "i", "o", "u", "y"]
    count_vowel = 0

    #Проверка на количество гласных и на присутствие лишней согласной
    for char in password:
        if char in vowel_ru:
            count_vowel += 1

        if char not in vowel_ru and char not in login:
            val_consonant = False

    #Проверка на отсутсвие согласных в пароле
    for char in login:
        if char not in vowel_ru and char not in password:
            val_consonant = False

    if count_vowel != 3:
        val_vowel = False

    if not val_vowel and val_consonant:
        error = "Wrong number of vowels"
        return failure(login, error)
    elif val_vowel and not val_consonant:
        error = "Wrong consonants"
        return failure(login, error)
    elif not val_vowel and not val_consonant:
        error = "Everything is wrong"
        return failure(login, error)
    else:
        return success(login)


def main():
    login = input().lower()
    password = input().lower()
    response = ask_password(login, password, success, failure)
    if response[0] == 200:
        return "Привет, " + response[1] + "!"
    else:
        error_text = "Кто-то пытался притвориться пользователем " + response[1] + ", но в пароле допустил ошибку: " \
                     + response[2].upper()
        return error_text



