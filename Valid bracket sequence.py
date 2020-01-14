# Valid Parentheses. Given a string containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true

# Считываем последовательность скобок:
string = input()

if not string:  # Если строка не содержит символов,
    print('true')  # дальнейший анализ не требуется.
    exit()

# Если первый символ последовательности не является открывающей скобкой,
if string[0] not in '([{':
    print('false')  # последовательность некорректна.
    exit()
else:  # Если первый символ - открывающая скобка,
    # добавляем его в список string_check:
    string_check = [string[0]]

# Словарь соответствия типов открывающих и закрывающих скобок:
bracket_pairs = {'(': ')', '[': ']', '{': '}'}

for i in range(1, len(string)):  # Перебираем скобки, начиная с индекса 1.
    if string[i] not in '([{':  # Если очередная скобка не открывающая,
        # и не соответствует последней открытой скобке,
        if string[i] != bracket_pairs[string_check[-1]]:
            print('false')  # последовательность некорректна.
            exit()
        else:  # Если закрывающая скобка соответствует последней открывающей,
            string_check.pop()  # удаляем последний элемент из string_check.
    else:  # Если очередная скобка открывающая, добавляем ее в список string_check.
        string_check.append(string[i])

# Если после завершения цикла список содержит какие-то элементы,
# значит, число открывающих скобок не соответствовало числу закрывающих.
if string_check:
    print('false')
else:  # Если же список пуст, то последовательность правильная.
    print('true')
