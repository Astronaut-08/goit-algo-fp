'''Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі,
використовуючи бінарну купу. Завдання включає створення графа, використання піраміди
для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини
до всіх інших.'''

from networkx import Graph
import heapq
# Створюємо наш граф
graph = Graph()
graph.add_edge(6, 2, weight=3)
graph.add_edge(6, 1, weight=2)
graph.add_edge(2, 1, weight=4)
graph.add_edge(2, 9, weight=1)
graph.add_edge(2, 3, weight=6)
graph.add_edge(3, 9, weight=5)
graph.add_edge(3, 7, weight=1)
graph.add_edge(6, 9, weight=1)
graph.add_edge(1, 7, weight=2)


def diikstra(gr: Graph, start_node):
    '''Обходимо наш граф в такому порядку в якому передана купа'''
    node_table = {val: float('inf') for val in gr} # Таблиця відстані до всіх нод в графі
    node_table[start_node] = 0 # Час початкової ноди = 0

    h = [(0, start_node)] # Використовуємо купу для вибору оптимальних верхиш, починаємо зі старту

    while h:
        dist, curent_node = heapq.heappop(h) # беремо ноду з найменшим шляхом з купи
        if dist > node_table[curent_node]:
            continue
        # витягуємо вершини та ребра всіх сусідів і перевіряємо шляхи
        for val, attr in gr[curent_node].items():
            weight = attr['weight']
            new_dist = dist + weight
            if new_dist < node_table[val]:
                node_table[val] = new_dist
                heapq.heappush(h, (new_dist, val)) # повертаємо ноду з накоротшим шляхом в купу
        
    return node_table

print(diikstra(graph, 1))
