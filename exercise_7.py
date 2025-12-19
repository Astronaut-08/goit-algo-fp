'''Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел,
які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел,
які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі
симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені
за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином (аналітична таблиця).

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці.'''

import random
import matplotlib.pyplot as plt

def monte_carlo_cube(cube_1: list, cube_2: list, experiments: int) -> list[list]:
    '''Приймає кубики і рахує ймовірність їх комбінацій'''
    min_combo = cube_1[0] + cube_2[0]
    max_combo = cube_1[-1] + cube_2[-1]
    temp_result = {i: 0 for i in range(min_combo, max_combo+1)}

    for _ in range(experiments):
        combo = random.choice(cube_1) + random.choice(cube_2)
        temp_result[combo] += 1

    unpack = []
    for key, value in temp_result.items():
        result = [str(key), f'{(value*100)/experiments:.02f}% ({value}/{experiments})']
        unpack.append(result)
    
    return unpack

table = monte_carlo_cube([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 10_000)

fig, ax = plt.subplots()
ax.axis('off')

ax.table(
    cellText=table,
    colLabels=["Сума", "Ймовірність"],
    loc='upper right'
)

plt.show()
