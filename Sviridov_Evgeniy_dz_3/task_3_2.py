def int_float(number):
    try:
        int(number)
        print('Целое число')
    except ValueError:
        try:
            float(number)
            print('Дробное число')
        except ValueError:
            print('Введите число')
        else:
            n1, n2 = number.split('.')
            if n1 == n2:
                return True
            else:
                return False


number = input('Введите число: ')
print(int_float(number))
