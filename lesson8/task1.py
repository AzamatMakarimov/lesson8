"""
я не понимаю зачем и как использовать хеширование в данной задаче
"""
f1 = input('строка = ')


def quantity(x):
    i = 0
    v = 0
    kol = 0
    for _ in range(len(x) ** 2):
        t = x[i: 1 + i + v]
        if t != x and t != '':
            print(t)
            kol += 1
        i += 1
        if i == len(x):
            i = 0
            v += 1
    print(kol, 'подстрок в строке')
quantity(f1)
