# Сложность Q(n)

# Возвращает список с помощью генератора списков в котором проверяется наличие элемента stones в jewels


def numJewelsInStones(jewels,stones): return len([x for x in stones if x in jewels])

print(numJewelsInStones('aA','aAAbbbb'))