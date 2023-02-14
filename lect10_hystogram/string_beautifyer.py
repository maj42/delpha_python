# possible_replaces = input("Give number of replacements: ")
# string_example = input("Give string: ")

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
        # Иначе проверка на новый лучший результат
        else:
            if iter_best_string_length > best_string_length:
                best_string_length = iter_best_string_length

print(best_string_length)
