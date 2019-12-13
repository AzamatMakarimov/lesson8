from collections import Counter, deque


string = input('введите слово = ')
count = Counter(string)
count = deque(sorted(count.items(), key=lambda x: x[1]))
while len(count) > 1:
    sum1 = count[0][1] + count[1][1]
    new_node = {0: count.popleft()[0], 1: count.popleft()[0]}
    for i, one_count in enumerate(count):
        if sum1 > one_count[1]:
            continue
        else:
            count.insert(i, (new_node, sum1))
            break
    else:
        count.append((new_node, sum1))
count = count[0][0]
code_table = {}


def huffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        huffman_code(tree[0], path=f'{path}0')
        huffman_code(tree[1], path=f'{path}1')
huffman_code(count)
for t in string:
    print(code_table[t], end=' ')
