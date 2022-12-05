# Сложность Q(n)


def removeOuterParentheses(s):
    res = []
    cnt = 0
    for i in s:
        if i == ')': cnt -= 1
        if cnt >= 1: res.append(i)
        if i == '(': cnt += 1
    return ''.join(res)

print(removeOuterParentheses('(()())(())(()(()))'))