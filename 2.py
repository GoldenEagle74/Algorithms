# Сложность Q(n)


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
