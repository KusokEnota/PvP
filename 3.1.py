"""Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
отрицательных чисел и чисел больше 100 тысяч."""

num = -1
num_max = 100000


def input_num(input_num_var, num_max_var):
    while input_num_var is None or input_num_var < 0 or input_num_var > num_max_var:
        try:
            input_num_var = int(input("Введите неотрицательное число и меньше " + str(num_max_var) + " - "))
        except ValueError:
            input_num_var = None
    return input_num_var


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


if is_prime(input_num(num, num_max)):
    print("Простое")
else:
    print("Число не является простым")
