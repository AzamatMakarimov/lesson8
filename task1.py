import hashlib,sys


f1 = input('строка = ')


def quantity(x):
    i = 0
    v = 0
    words = []
    for _ in range(len(x) ** 2):
        t = x[i: 1 + i + v]
        if t != x and t != '':
            d = bytearray(t.encode('utf-8'))
            words.append((t, hashlib.sha1(d).hexdigest()))
        i += 1
        if i == len(x):
            i = 0
            v += 1
    words = set(words)
    print(round(len(words)), 'подстрок в строке:')
    for i in words:
        print(f'{i[0]} - {i[1]}')
quantity(f1)
