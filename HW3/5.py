# Временная сложность: O(rows * cols)
# Алгоритм для вычисления общего периметра острова в сетке
def islandPerimeter(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Обходим каждую клетку в сетке
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Если текущая клетка является частью острова
                perimeter += 4  # Добавляем 4 к периметру

                # Проверяем соседние клетки и уменьшаем периметр, если соседняя клетка также является частью острова
                if i > 0 and grid[i-1][j] == 1:  # Верхняя клетка
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:  # Левая клетка
                    perimeter -= 2

    return perimeter
