"""таблицу умножения от 2х2 до 9х10 как на школьной тетрадке"""


def tablu():
    res = ""
    for k in range(2, 10):
        for i in range(2, 11):
            res += f'{i} x {k} = {i * k}\t\t'
        res += "\n"
    return res


print(tablu())
