from collections import defaultdict

def maxNetIncome(edges, bob, amount):
    # Шаг 1: Построить дерево с помощью списка смежности
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    n = len(amount)

    # Шаг 2: Найти путь Боба к корню (узлу 0)
    def find_path_to_root(node, parent):
        path = []
        while node != -1:
            path.append(node)
            node = parent[node]
        return path

    # Массив для родителей, чтобы отслеживать путь Боба
    parent = [-1] * n
    def dfs_bob(node, par):
        parent[node] = par
        for neighbor in tree[node]:
            if neighbor != par:
                dfs_bob(neighbor, node)

    # Запускаем DFS для Боба от его начальной позиции
    dfs_bob(bob, -1)
    path_bob = find_path_to_root(bob, parent)

    # Шаг 3: Рассчитать максимальный доход для Алисы с помощью DFS
    max_income = float('-inf')

    def dfs_alice(node, par, depth):
        current_income = 0

        # Рассчитываем доход для Алисы на этом узле
        if depth < len(path_bob):
            bob_depth = path_bob[depth]
            # Если они доходят одновременно
            if bob_depth == node:
                current_income += amount[node] // 2
            else:
                current_income += amount[node]
        else:
            current_income += amount[node]

        is_leaf = True
        total_income = current_income  # Сохраняем доход на текущем узле
        for neighbor in tree[node]:
            if neighbor != par:
                is_leaf = False
                total_income += dfs_alice(neighbor, node, depth + 1)

        if is_leaf:
            return total_income
        return current_income

    dfs_alice(0, -1, 0)

    return max_income

# Пример использования:
edges1 = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob1 = 3
amount1 = [-2, 4, 2, -4, 6]
print(maxNetIncome(edges1, bob1, amount1))  # Ожидаемый вывод: 6

edges2 = [[0, 1]]
bob2 = 1
amount2 = [-7280, 2350]
print(maxNetIncome(edges2, bob2, amount2))  # Ожидаемый вывод: -7280
