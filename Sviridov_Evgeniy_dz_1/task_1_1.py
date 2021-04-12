def multiplication_table(a, b):
    """Функция вывода таблицы умножения AxB"""
    print(f'Start multiplication table {a} x {b}')
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            print(f'{i} x {j} = {i * j}')
    print(f'End multiplication table {a} x {b}')


multiplication_table(2, 2)
multiplication_table(5, 7)
multiplication_table(20, 10)
