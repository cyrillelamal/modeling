import math
import statistics
import plotly.graph_objects as go

E = 5  # precision


x = [33, 40, 36, 60, 55, 80, 95, 70, 48, 53, 95, 75, 63, 112, 70]
y = [13.8, 13.8, 14, 22.5, 24, 28, 32, 20.9, 22, 21.5, 32, 35, 24, 37.9, 27.5]


# 1. график зависимости между переменными
print('1. график зависимости между переменными')
# Y = a + bx
# ERR(x) = S(i=1, n)(a+bx(i)+y(i))^2
# sum -> S
# ERR'a = 2na + 2bS(i=1, n)(x(i)) - S(i=1, n)(y(i)) = 2(na+bS(i=1, n)(x(i)) - S(i=1, n)(y(i)))
# ERR'b = 2S(i=1, n)(x(i)*(a+bS(i=1, n)(x(i)-S(i=1, n)(y(i))))

# number of values
n = len(x)
# sums
sx = sum(x)
sy = sum(y)
# sum of multiplications
xy = [x[i] * y[i] for i in range(n)]
sxy = sum(xy)
# sum of squares
x_sq = [x[i] * x[i] for i in range(n)]
sx_sq = sum(x_sq)

a = (sx_sq * sy - sx * sxy) / (sx_sq * n - sx * sx)
b = (sxy * n - sy * sx) / (sx_sq * n - sx * sx)

print('Оптимальные значения a и b:\n')
print(f'a = {a}')
print(f'b = {b}')
print(f"Уравнение регрессии: y'= {a} + {b}x")
line = [a+b*x[i] for i in range(n)]  # regression line

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='markers',
    name='Диаграмма рассеяния'
))
fig.add_trace(go.Scatter(
    x=x, y=line,
    mode='lines',
    name='Линия регрессии'
))
fig.update_layout(
    title='Уравнение регресси',
    xaxis_title="Общая площадь квартиры в кв. м.",
    yaxis_title="Рыночная стоимость квартиры в тыс. у.е.",
)
fig.show()


# 3. Средняя ошибка аппроцсимации
print('3. Средняя ошибка аппроцсимации')
A_ = 1/n * sum((
    abs((y[i] - line[i]) / y[i])
    for i in range(n)
)) * 100  # %
print(f'Средняя ошибка аппроксимации: {round(A_, E)}')


# 4. Коэффициент эластичности
print('4. Коэффициент эластичности')
ELASTIC = b * (sum(x) / n) / (sum(y) / n)
print(f'Коэффициент эластичности: {round(ELASTIC, E)}')


# 5. Оценка тесноты связи между переменными с помощью показателей корреляции и детерминации
print('5. Оценка тесноты связи между переменными с помощью показателей корреляции и детерминации')
sigma_x = math.sqrt(
    statistics.mean((x[i]*x[i] for i in range(n)))
    - statistics.mean(x)**2
)
sigma_y = math.sqrt(
    statistics.mean((y[i]*y[i] for i in range(n)))
    - statistics.mean(y)**2
)
r = (statistics.mean(x[i]*y[i] for i in range(n)) - statistics.mean(x) * statistics.mean(y))\
    / (sigma_x * sigma_y)
print(f'Коэффициент корреляции: {round(r, E)}')

r_sq = r * r
print(f'Коэффициент детерминации: {round(r_sq, E)}')

print('Гипотеза: коэффициент корреляции в генеральной совокупности равен нулю, '
      'и изучаемый фактор не оказывает существенного влияния на результативный признак')
k = n - 2
alpha = 0.05
T_cr = 2.16
print(f'Уровень значимости: {alpha}, число стпеней свободы: {k} -> t критическое = {T_cr}')
t_c = round(abs(r) / math.sqrt((1 - r_sq) / k), E)
print(f'Расчетное значение t-критерия: {t_c}')
if t_c > T_cr:
    print(f'Гипотеза отвергается: {t_c} > {T_cr}')
else:
    print(f'Гипотеза подтвержается: {t_c} < {T_cr}')


# 6. Оценка значимости коэффициентов корреляции и регрессии по критерию t-Стьюдента
print('6. Оценка значимости коэффициентов корреляции и регрессии по критерию t-Стьюдента')
# Student coefficient
m_b1 = math.sqrt(
    sum(((y[i] - line[i])**2 for i in range(n)))
    / (k * sigma_x**2 * n)
)
t_c2 = round(b / m_b1, E)
print(f'Расчетное значение t-критерия Стьюдента: {t_c2}')
if t_c2 > T_cr:
    print(f'Гипотеза отвергается: {t_c2} > {T_cr}')
else:
    print(f'Гипотеза подтвержается: {t_c2} < {T_cr}')


# 7. Статистическая надежность результатов регрессионного анализа с использованием критерия F-Фишера
print('7. Статистическая надежность результатов регрессионного анализа с использованием критерия F-Фишера')
# reliability
# Fischer's criteria
F = round(r_sq / (1 - r_sq) * k, E)
F_cr = 4.67
print(f'Уровень значимости: {alpha}, число стпеней свободы: {k} -> F критическое = {F_cr}')
print(f'Рассчетный критей F-Фишера: {F}')
if F > F_cr:
    print(f'Уравнение регрессии - статичтически значимо (надежно)')
else:
    print(f'Уравнение регрессии - не значимо (ненадежно)')


# 8. Прогнозное значение результативного признака
print('8. Прогнозное значение результативного признака')
# forecast value
X_p = round(statistics.mean(x) + 1.2, E)
print(f'Факторный признак: {X_p}')
Y_p = round(a + b * X_p, E)
print(f'Прогнозное значение результативного признака: {Y_p}')
