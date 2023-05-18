# Сложность алгоритма O(n), где n - количество дней 
# Мы инициализируем переменную res для хранения максимальной прибыли, которая изначально равна 0.
# Затем мы проходим по массиву цен с помощью цикла for, начиная с первого элемента и до предпоследнего элемента.
# Внутри цикла мы проверяем, если цена на следующий день (prices[i + 1]) больше цены на текущий день (prices[i]).
# Если это условие выполняется, значит можно совершить операцию покупки и продажи акций в этот день, и мы прибавляем разницу цен к общей прибыли res.
# После прохождения по всем элементам массива, мы возвращаем максимальную прибыль res.

def maxProfit(prices) -> int:
    # Инициализация переменной для хранения максимальной прибыли
    res = 0

    # Проход по массиву цен (за исключением последнего элемента)
    for i in range(len(prices) - 1):
        # Проверка, если цена на следующий день выше цены на текущий день
        if prices[i + 1] - prices[i] > 0:
            # Прибавление разницы цен к общей прибыли
            res += (prices[i + 1] - prices[i])

    # Возврат максимальной прибыли
    return res