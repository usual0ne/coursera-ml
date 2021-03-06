import pandas as pd
import numpy as np

# Загрузите данные из файла advertising.csv в объект pandas DataFrame.
adver_data = pd.read_csv('advertising.csv')

# Создайте массивы NumPy X из столбцов TV, Radio и Newspaper и y - из столбца Sales.
# # Используйте атрибут values объекта pandas DataFrame.
X = adver_data[['TV', 'Radio', 'Newspaper']].values
y = adver_data.Sales.values

# Отмасштабируйте столбцы матрицы X, вычтя из каждого значения среднее по соответствующему столбцу
# и поделив результат на стандартное отклонение.
# Для определенности, используйте методы mean и std векторов NumPy (реализация std в Pandas может отличаться).
# Обратите внимание, что в numpy вызов функции .mean() без параметров возвращает среднее по всем элементам массива,
# а не по столбцам, как в pandas.
# Чтобы произвести вычисление по столбцам, необходимо указать параметр axis.
means, stds = np.mean(X, axis=0), np.std(X, axis=0)
X = (X-means)/stds

# Добавьте к матрице X столбец из единиц, используя методы hstack, ones и reshape библиотеки NumPy.
# Вектор из единиц нужен для того, чтобы не обрабатывать отдельно коэффициент  𝑤0  линейной регрессии.
X = np.hstack((X, np.ones((200, 1))))

# Реализуйте функцию mserror - среднеквадратичную ошибку прогноза.
# Она принимает два аргумента - объекты Series y (значения целевого признака) и y_pred (предсказанные значения).
# Не используйте в этой функции циклы - тогда она будет вычислительно неэффективной.
def mserror(y, y_pred):
    return np.mean((y_pred - y)**2)

# Реализуйте функцию normal_equation, которая по заданным матрицам (массивам NumPy) X и y вычисляет вектор весов  𝑤
# согласно нормальному уравнению линейной регрессии.
def normal_equation(X, y):
    a = np.dot(X.T, X) # преобразуем левую часть
    b = np.dot(X.T, y) # преобразуем правую часть
    res = np.linalg.solve(a, b) # решаем систему
    return res

# Напишите функцию linear_prediction, которая принимает на вход матрицу X и вектор весов линейной модели w,
# а возвращает вектор прогнозов в виде линейной комбинации столбцов матрицы X с весами w.
def linear_prediction(X, w):
    return X.dot(w)

# Напишите функцию stochastic_gradient_step, реализующую шаг стохастического градиентного спуска для линейной регрессии.
# Функция должна принимать матрицу X, вектора y и w, число train_ind - индекс объекта обучающей выборки (строки матрицы X),
# по которому считается изменение весов, а также число  𝜂  (eta) - шаг градиентного спуска (по умолчанию eta=0.01).
# Результатом будет вектор обновленных весов. Наша реализация функции будет явно написана для данных с 3 признаками,
# но несложно модифицировать для любого числа признаков, можете это сделать.
def stochastic_gradient_step(X, y, w, train_ind, eta=0.01):
    N = X.shape[0]  # всего обьектов (нормировка)
    x = X[train_ind]  # текуший случайный k обьект
    y_pred = linear_prediction(x, w)  # предсказание для к случайного обьекта
    rs = (y_pred - y[train_ind])  # регрессионый остаток для k обьекта
    grad0 = 2.0 / N * x[0] * rs
    grad1 = 2.0 / N * x[1] * rs
    grad2 = 2.0 / N * x[2] * rs
    grad3 = 2.0 / N * x[3] * rs
    return w - eta * np.array([grad0, grad1, grad2, grad3])

# Напишите функцию stochastic_gradient_descent, реализующую стохастический градиентный спуск для линейной регрессии.
# Функция принимает на вход следующие аргументы:
#
# X - матрица, соответствующая обучающей выборке.
# y - вектор значений целевого признака.
# w_init - вектор начальных весов модели.
# eta - шаг градиентного спуска (по умолчанию 0.01).
# max_iter - максимальное число итераций градиентного спуска (по умолчанию 10000).
# max_weight_dist - максимальное евклидово расстояние между векторами весов на соседних итерациях градиентного спуска,
# при котором алгоритм прекращает работу (по умолчанию 1e-8).
# seed - число, используемое для воспроизводимости сгенерированных псевдослучайных чисел (по умолчанию 42).
# verbose - флаг печати информации (например, для отладки, по умолчанию False).
# На каждой итерации в вектор (список) должно записываться текущее значение среднеквадратичной ошибки.
# Функция должна возвращать вектор весов  𝑤 , а также вектор (список) ошибок.
def stochastic_gradient_descent(X, y, w_init, eta=1e-2, max_iter=1e4,
                                min_weight_dist=1e-8, seed=42, verbose=False):
    # Инициализируем расстояние между векторами весов на соседних
    # итерациях большим числом.
    weight_dist = np.inf
    # Инициализируем вектор весов
    w = w_init
    # Сюда будем записывать ошибки на каждой итерации
    errors = []
    # Счетчик итераций
    iter_num = 0
    # Будем порождать псевдослучайные числа
    # (номер объекта, который будет менять веса), а для воспроизводимости
    # этой последовательности псевдослучайных чисел используем seed.
    np.random.seed(seed)

    # Основной цикл
    while weight_dist > min_weight_dist and iter_num < max_iter:
        # порождаем псевдослучайный индекс объекта обучающей выборки
        random_ind = np.random.randint(X.shape[0])
        # вектор обновленных весов
        w = stochastic_gradient_step(X, y, w, random_ind, eta)
        # вектор ошибок всех итераций
        errors.append(mserror(y[random_ind], X[random_ind].dot(w)))
        iter_num += 1

    return w, errors
