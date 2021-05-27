example = {
    'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15 / 2, False],
    'fire': ['hot', 46, ['cha', 'ching'], 81.13],
    'earth': ['solid', 100, (13, 31, 1), 90.01, {'b': 'c'}]
}

elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def try_element(example, elements):
    for i in elements:
        try:
            sums = 0
            for z in example[i]:
                try:
                    sums += z
                except TypeError:
                    continue
            print(f'{i} - {sums}')
        except KeyError:
            print(f'{i} ключа в словаре не существует')

try_element(example, elements)
