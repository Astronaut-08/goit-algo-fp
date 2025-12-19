'''Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та
алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною
калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника,
де ключ — назва страви, а значення — це словник з вартістю та калорійністю.'''

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

'''Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи
співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming,
яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.'''

def greedy_algorithm(budget: int, products: dict[str: dict[str: int]]) -> list:
    '''Приймає в себе бюдет і список продуктів з калорійністю, повертає список продуктів'''
    greedy_list = list()

    greedy_sort_items = dict(
        sorted(
            products.items(), 
            key=lambda x: x[1]['calories'] / x[1]['cost'], # співвідношення
            reverse=True
        )
    )

    for item in greedy_sort_items:
        if budget > greedy_sort_items[item].get('cost'):
            greedy_list.append(item)
            budget -= greedy_sort_items[item].get('cost')
        else:
            break

    return greedy_list

def dynamic_programing(budget: int, products: dict[str: dict[str: int]]) -> list:
    '''Приймає в себе бюдет і список продуктів з калорійністю, повертає список продуктів'''
    items = list(products.items())
    cou = len(items)

    table = [[0] * (budget + 1) for _ in range(cou + 1)] # 2D таблиця

    for i in range(1, cou + 1):
        item, stats = items[i - 1]
        
        for j in range(budget + 1):
            table[i][j] = table[i-1][j]

            if j >= stats['cost']:
                table[i][j] = max(
                    table[i][j], table[i-1][j-stats['cost']] + stats['calories']
                )

    dynamic_list = list()
    for i in range(cou, 0, -1): # розпаковка з останнього рядка
        if table[i][budget] != table[i-1][budget]:
            item, stats = items[i - 1]
            dynamic_list.append(item)
            budget -= stats['cost']

    return dynamic_list

print(greedy_algorithm(120, items))
print(dynamic_programing(120, items))
