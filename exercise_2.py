'''Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.'''

from turtle import Turtle, Screen

def pifagore_tree(cursor: Turtle, step: int, cou: int) -> None:
    '''Дерево піфагора, викликається рекурсивно'''
    if cou == 0:
        return # базовий випадк, просто зупиняємо рекурсію, більше нічого
    else:
        new_cursor = Turtle()
        # тут ми беремо позицію нашого початкового курсора
        new_cursor.speed(0)
        new_cursor.penup()
        new_cursor.setpos(cursor.pos())
        new_cursor.setheading(cursor.heading())
        new_cursor.pendown()
        # тут ми рахуємо новий крок, і проводимо всі рухи
        piece_step = step / 1.5
        cursor.forward(step)
        cursor.left(45)
        cursor.hideturtle()
        pifagore_tree(cursor, piece_step, cou - 1) # спочатку ми будуємо ліву сторону
        new_cursor.forward(step)
        new_cursor.right(45)
        new_cursor.hideturtle()
        pifagore_tree(new_cursor, piece_step, cou - 1) # потім будуємо праву 

screen = Screen()
screen.setup(width=1200, height=650)
t = Turtle()
t.speed(0)
t.left(90)

pifagore_tree(t, 120, 9)

screen.mainloop()