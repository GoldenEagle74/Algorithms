# Временная сложность: O(rows * cols)
# Алгоритм для подсчета количества островов в сетке


def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
            return

        grid[row][col] = '0'  # Помечаем посещенный остров

        # Рекурсивно вызываем dfs для смежных клеток
        dfs(row - 1, col)  # Верхняя клетка
        dfs(row + 1, col)  # Нижняя клетка
        dfs(row, col - 1)  # Левая клетка
        dfs(row, col + 1)  # Правая клетка

    # Обходим каждую клетку в сетке
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':  # Если текущая клетка является частью острова
                count += 1
                dfs(i, j)  # Запускаем поиск в глубину (DFS) для текущего острова

    return count
