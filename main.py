import numpy as np
from scipy.optimize import fsolve

def solve_y(x, z, y0=None):

    # y = (x^2 - y) / (z - x) + log(y - x)

    if z == x:
        raise ValueError("Деление на ноль: z не может быть равно x.")
    
    if y0 is None:
        y0 = x + 1.0
        
    if y0 <= x:
        raise ValueError("Начальное приближение y0 должно быть строго больше x (ОДЗ логарифма).")

    def equation(y):
        # Защита от выхода за ОДЗ логарифма (y > x)
        diff = y - x
        sdiff = np.where(diff > 0, diff, 1.0) # 1.0 как безопасный фантом для логарифма
        
        result = y - (x**2 - y) / (z - x) - np.log(sdiff)
    
        return np.where(diff > 0, result, np.inf)

    y_solution, infodict, errflag, mesg = fsolve(equation, y0, full_output=True)

    # errflag=1 означает успешную сходимость
    if errflag != 1 or abs(equation(y_solution)[0]) > 1e-5:
        raise ValueError(f"Решение не найдено. Возможно, при данных x и z вещественных корней нет. {mesg.strip()}")

    return y_solution[0]