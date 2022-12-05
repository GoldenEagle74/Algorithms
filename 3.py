# Сложность Q(n)


def numJewelsInStones(jewels,stones): return len([x for x in stones if x in jewels])

print(numJewelsInStones('aA','aAAbbbb'))