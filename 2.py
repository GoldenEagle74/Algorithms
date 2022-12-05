# Сложность Q(n)

# Пускаем изначальное число в цикл пока оно не станет равно 1
# Если число нечетное, то n равно n // 2 + 1. А к общему счету матчей n пополам
# Если число четное, то n //= 2 и счет матчей += n//2


def numberOfMatches(n):
	cnt = 0
	while n > 1:
		if n % 2:
			n = n // 2 + 1
			cnt += n - 1
		else:
			n //= 2
			cnt += n
	return cnt

print(numberOfMatches(int(input())))
