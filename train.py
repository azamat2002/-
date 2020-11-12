"""
    1. Создать функцию, которая выводит на экран цифру, введенную пользоватлем в консоли.

    2. Написать программу, которая принимает 5 значений, введенных пользователем из консоли, сохранит их в список,
    затем передаст значения в фукцию, которая выводит на экран сумму значений списка.

    3. Написать программу, которая:
    - выводит следующее меню на экран
        1. Ввести значения а и b
        2. Умножить значения а и b
        3. Делить а на b
        4. Выход
    - реализует каждую опцию как фукцию
    - реализует все ошибки и исключения.
"""


# 1
def number():
    num = int(input('>>> '))
    print(num)


number()


# 2
def num_sum(array):
    total = 0

    for i in array:
        total += i

    print(total)


list_num = []
for i in range(5):
    inputs = int(input('>>> '))
    list_num.append(inputs)
    print(list_num)


num_sum(list_num)


# 3
def user_input():
    A = int(input('a: '))
    B = int(input('b: '))

    return A, B


def multiplication(A, B):
    return A * B


def divided(A, B):
    return A / B


def quit_pr():
    return True


a = 0
b = 0

while True:

    print('1. Значения а и b')
    print('2. Умножить  а и b')
    print('3. Делить а на b')
    print('4. Выход')

    try:
        user_choice = int(input('>>> '))

        if user_choice != 4:
            if user_choice == 1:
                a, b = user_input()
                print('a: {0}, b: {1}'.format(a, b))
            if user_choice == 2:
                m = multiplication(a, b)
                print('a * b =', m)
            if user_choice == 3:
                m = divided(a, b)
                print('a * b =', m)
            else:
                print('Допущена ошибка.')
        else:
            q = quit_pr()
            if q is True:
                print('Выход из программы...')
                break
    except:
        print('Допущена ошибка.')
