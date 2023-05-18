# Сложность алгоритма: временная сложность O(n), где n - количество домов.
# Функция rob решает задачу для случая, когда дома расположены в кругу. Она вызывает функцию rob_linear дважды: один раз, исключая первый элемент, и один раз, исключая последний элемент. Затем она возвращает максимальное значение из этих двух случаев, так как решение должно быть независимым от порядка домов.
# Функция rob_linear решает задачу для случая, когда дома расположены линейно. Она использует динамическое программирование для нахождения максимальной суммы при рассмотрении каждого дома. Для каждого дома, она обновляет предыдущий максимум (prev_max) и текущий максимум (curr_max). Текущий максимум вычисляется как максимум из суммы предыдущего максимума и текущего дома или предыдущего дома.
# В итоге, функция rob_linear возвращает максимальную сумму, которую можно украсть без привлечения полиции.
# Функция rob использует rob_linear для двух случаев (исключая первый и последний элемент) и возвращает максимум из них.


def rob(nums) -> int:
    n = len(nums)
    
    if n == 1:
        return nums[0]  # Если в списке только один элемент, то возвращаем его значение
    
    # Вызываем функцию rob_linear для случая, когда мы не рассматриваем первый элемент
    # и функцию rob_linear для случая, когда мы не рассматриваем последний элемент.
    # Возвращаем максимальное значение из этих двух случаев.
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


def rob_linear(nums):
    n = len(nums)
    
    # Инициализируем две переменные для хранения максимальной суммы при рассмотрении
    # предыдущего и текущего домов.
    prev_max = curr_max = 0
    
    # Обходим все дома по очереди.
    for num in nums:
        # Сохраняем значение текущего максимума, затем обновляем текущий максимум,
        # используя предыдущий максимум и текущий дом.
        prev_max, curr_max = curr_max, max(prev_max + num, curr_max)
    
    # Возвращаем максимальную сумму.
    return curr_max

print(rob([1, 2, 3, 4, 5]))