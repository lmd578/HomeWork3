# 3
# def my_func(x, y):
#     if y == 0:
#         return 1
#     return x * my_func(x, y + 1)
#
#
# print(my_func(2, -1))


# 6
# def int_func(text):
#     result = ''
#     for word in text.slit():
#         result += word[0].upper() + word[1:]
#
#     return result

# def int_func(text):
#     result = ''
#     for word in text.slit():
#         result += word.capitalize()
#
#     return result


def int_func(text):
    return text.title()


def int_func(*args):
    word = input('Введите слово: ')
    print(word.title())
    return


print(int_func())
