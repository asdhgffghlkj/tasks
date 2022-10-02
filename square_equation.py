# Важно понимать, что основной смысл ближайших занятий по Python - это познакомиться (вспомнить) с его синтаксисом,
# вспомнить/узнать встроенные структуры данных, сложность их методов
#
# Основу для изучения Python у нас составить данный курс: stepik.org/course/512
# Для ознакомления с синтаксисом Python предлагаю данную статью (или найди свою): cs.mipt.ru/algo/lessons/lab2.html
#
# Задачка 1
# Реализовать функцию, принимающую на вход три коэффициента квадратного уравнения и возвращающая кортеж из двух корней
# def square_equation(a, b, c):
#     # your code here

# Например:
# square_equation( 1,  2,  1 ) == (   -1,   -1 )
# square_equation( 1, -2,  1 ) == (    1,    1 )
# square_equation( 0,  1,  1 ) == (   -1, None )
# square_equation( 0,  1, -1 ) == (    1, None )
# square_equation( 1,  2, -1 ) == ( None, None )
#


def square_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c != 0:
                return None, None
            else:
                return "ALL"
        s1 = -c / b
        return s1, None
    else:
        s1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        s2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return s1, s2


assert square_equation(1, 2, 1) == (-1, -1)
assert square_equation(1, -2, 1) == (1, 1)
assert square_equation(0, 1, 1) == (-1, None)
assert square_equation(0, 0, 1) == (None, None)
assert square_equation(0, 0, 0) == "ALL"
