def get_replacements() -> int:
    while True:
        replaces = input("Give number of replacements: ")
        try:
            replaces = int(replaces)
        except ValueError:
            print("Give a number!")
            continue
        if replaces < 0 or replaces > 10 ** 9:
            print("Give a number between 0 and 10^9!")
        else:
            return replaces


def get_string() -> str:
    while True:
        string = input("Give string: ")
        if not string.isalpha():
            print("Letters only!")
        elif not string.islower():
            print("Lowercase only!")
        elif len(string) < 2:
            print("Too short!")
        elif len(string) > 2 * 10 ** 5:
            print("Too long!")
        else:
            return string


# Для проверки входных данных по условию:
# possible_replaces = get_replacements()
# string_example = get_string()

possible_replaces = 2
string_example = "abcaz"
# string_example = "helto"

# Итоговая красота строки при заданных параметрах, выводится в конце
best_string_length = 1

# Внешний итератор по индексу каждого символа
for sym in range(len(string_example)):
    # Текущий символ внешнего итератора, кол-во замен для каждой итерации и лучший текущий результат
    current_sym = string_example[sym]
    iter_replaces = possible_replaces
    iter_best_string_length = 1
    # Внутренний итератор по индексам всех элементов справа от текущего
    for i in range(sym + 1, len(string_example)):
        iter_sym = string_example[i]
        # Если совпадают - +к текущему результату
        if current_sym == iter_sym:
            iter_best_string_length += 1
        # Если не совпали и еще есть замены - +к текущему результату
        elif iter_replaces > 0:
            iter_best_string_length += 1
            iter_replaces -= 1
        # Иначе - выход из внутреннего цикла и проверка на новый лучший результат
        else:
            if iter_best_string_length > best_string_length:
                best_string_length = iter_best_string_length
            break

print(best_string_length)
