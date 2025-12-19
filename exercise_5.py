'''Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python,
яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB
(приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від
послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який
візуально відображає порядок обходу.

👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію'''

import exercise_4
from collections import deque

# Створюємо таблицю кольорів для наших нод
nodes = [exercise_4.Node(i) for i in exercise_4.heap] # рахуємо кількість нод

def get_node_color(nodes: list[exercise_4.Node], start_rgb: tuple, end_rgb: tuple) -> dict:
    '''Генерує кольори для нод і повертає їх у вигляді словника'''
    start_r, start_g, start_b = start_rgb
    end_r, end_g, end_b = end_rgb
    # вираховуємо крок зміни
    step_r = (end_r - start_r) / (len(nodes) - 1)
    step_g = (end_g - start_g) / (len(nodes) - 1)
    step_b = (end_b - start_b) / (len(nodes) - 1)
    # Присвоюємо вузлам
    table_node_color = dict()
    for idx in range(len(nodes)):
        idx_r = round(start_r + idx * step_r)
        idx_g = round(start_g + idx * step_g)
        idx_b = round(start_b + idx * step_b)
        table_node_color[idx] = f'#{idx_r:02X}{idx_g:02X}{idx_b:02X}'

    return table_node_color


table_node_color = get_node_color(nodes, (83, 75, 69), (255, 109, 0))


def my_dfs(root: exercise_4.Node):
    '''Обхід в глибину за допомогою циклу та стеку'''
    stack = [root]
    color_step = 0

    while stack:
        node = stack.pop()

        # Змінюємо колір, вважаємо відвіданим
        node.color = table_node_color[color_step]
        color_step += 1

        # візуалізуємо завжди від кореня
        exercise_4.draw_tree(root)

        if node.right: # спочатку права бо стек LIFO
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

def my_bfs(root: exercise_4.Node):
    '''Обхід в ширину за допомогою циклу та черги'''
    que = deque([root])
    color_step = 0

    while que:
        node = que.popleft()

        # Змінюємо колір, вважаємо відвіданим
        node.color = table_node_color[color_step]
        color_step += 1

        # візуалізуємо завжди від кореня
        exercise_4.draw_tree(root)

        if node.left: # спочатку ліва бо черга FIFO
            que.append(node.left)

        if node.right:
            que.append(node.right)


# my_dfs(exercise_4.root)
my_bfs(exercise_4.root)
