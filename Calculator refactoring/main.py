import math

result = float

def sum(num1, num2):
    result = num1 + num2
    return result
def sub(num1, num2):
    result = num1 - num2
    return result
def mult(num1, num2):
    result = num1 * num2
    return result
def div(num1, num2):
    result = num1 / num2
    return result
def degree(num1, num2):
    result = num1 ** num2
    return result
def root(num1):
    result = math.sqrt(num1)
    return result
def cos(num1):
    result = math.cos(num1)
    return result
def sin(num1):
    result = math.sin(num1)
    return result
def tg(num1, num2):
    result = math.sin(num1) / math.cos(num2)
    return result
def factorial(num1):
    result = math.factorial(num1)
    return result

while True:
    print('\nВведите тип операции: \n (+) - Cложение \n (-) - Вычитание \n (*) - Умножение \n (/) - Деление \n (!) - Факториал числа \n (^) - Возведение числа в степень \n (√) - Квадратный корень из числа \n (cos) - Cos числа \n (sin) - Sin числа \n (tg) - Tg числа')
    oper = str(input())
    if type(oper) == str:
        pass
        if oper == '+' or oper == '-' or oper == '*' or oper == '/' or oper == '^' or oper == '√' or oper == 'cos' or oper == 'sin' or oper == 'tg' or oper == '!':
            match oper:
                case "+":
                    while True:
                        try:
                            num1 = float(input("\nВведите первое слагаемое: "))
                        except ValueError:
                            print("\nВы ввели некорректно первое слагаемое! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели первое слагаемое: {num1}')
                            break
                        else:
                            print("\nСлагаемое введено некорректно!")

                    while True:
                            try:
                                num2 = float(input("\nВведите второе слагаемое: "))
                            except ValueError:
                                print("\nВы ввели некорректно второе слагаемое! Попробуйте снова.")
                                continue
                            if type(num2) == float:
                                print(f'Вы ввели второе слагаемое: {num2}')
                                break
                            else:
                                print("\nСлагаемое введено некорректно!")

                    result = sum(num1, num2)
                    print(f'\nОтвет данной суммы: {result}')

                case '-':
                    while True:
                        try:
                            num1 = float(input("\nВведите уменьшаемое: "))
                        except ValueError:
                            print("\nВы ввели некорректно уменьшаемое! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели уменьшаемое: {num1}')
                            break
                        else:
                            print("\nУменьшаемое введено некорректно!")

                    while True:
                        try:
                            num2 = float(input("\nВведите вычитаемое: "))
                        except ValueError:
                            print("\nВы ввели некорректно вычитаемое! Попробуйте снова.")
                            continue
                        if type(num2) == float:
                            print(f'Вы ввели вычитаемое: {num2}')
                            break
                        else:
                            print("\nВычитаемое введено некорректно!")

                    result = sub(num1, num2)
                    print(f'\nОтвет данной разности: {result}')


                case '*':
                    while True:
                        try:
                            num1 = float(input("\nВведите первый множитель: "))
                        except ValueError:
                            print("\nВы ввели некорректно множитель! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели первый множитель: {num1}')
                            break
                        else:
                            print("\nМножитель введён некорректно!")

                    while True:
                        try:
                            num2 = float(input("\nВведите второй множитель: "))
                        except ValueError:
                            print("\nВы ввели некорректно множитель! Попробуйте снова.")
                            continue
                        if type(num2) == float:
                            print(f'Вы ввели второй множитель: {num2}')
                            break
                        else:
                            print("\nМножитель введён некорректно!")

                    result = mult(num1, num2)
                    print(f'\nОтвет данного произведения: {result}')


                case '/':
                    while True:
                        try:
                            num1 = float(input("\nВведите числитель: "))
                        except ValueError:
                            print("\nВы ввели некорректно числитель! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели числитель: {num1}')
                            break
                        else:
                            print("\nЧислитель введён некорректно!")

                    while True:
                        try:
                            num2 = float(input("\nВведите знаменатель: "))
                        except ValueError:
                            print("\nВы ввели некорректно множитель! Попробуйте снова.")
                            continue
                        if type(num2) == float and num2 != 0:
                            print(f'Вы ввели знаменатель: {num2}')
                            break
                        else:
                            print("\nЧислитель или знаменатель введён некорректно! (На ноль делить нельзя) Попробуйте снова")

                    result = div(num1,num2)
                    print(f'\nОтвет данного выражения: {result}')

                case '^':
                    while True:
                        try:
                            num1 = float(input("\nВведите число, которое хотите возвести в степень: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова:")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели число: {num1}')
                            break
                        else:
                            print("\nЧисло введено некорректно!")

                    while True:
                        try:
                            num2 = float(input("\nВведите степень: "))
                        except ValueError:
                            print("\nВы ввели некорректно степень! Попробуйте снова.")
                            continue
                        if type(num2) == float:
                            print(f'Вы ввели степень: {num2}')
                            break
                        else:
                            print("\nЧисло или степень введены некорректно!")

                    result = degree(num1, num2)
                    print(f'\nВозведение числа {num1} в степень {num2} равно: {result}')


                case '√':
                    while True:
                        try:
                            num1 = float(input("\nВведите число, из которого хотите вычеслить квадратный корень: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова.")
                            continue
                        if type(num1) == float and num1 >= 0:
                            print(f'Вы ввели число: {num1}')
                            break
                        else:
                            print("\nЧисло введено некорректно! (Подкоренное выражение не должно быть отрицательным) Попробуйте снова:")

                    result = root(num1)
                    print(f'\nКорень из числа {num1} равен: {result}')

                case 'cos':
                    while True:
                        try:
                            num1 = float(input("\nВведите cosX: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели число (X): {num1}')
                            break
                        else:
                            print("\nЧисло введено некорректно!")

                    result = cos(num1)
                    print(f'\nCos{num1} равнен: {result}')

                case 'sin':
                    while True:
                        try:
                            num1 = float(input("\nВведите sinX: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели число (X): {num1}')
                            break
                        else:
                            print("\nЧисло введено некорректно!")

                    result = sin(num1)
                    print(f'\nSin{num1} равнен: {result}')

                case 'tg':
                    while True:
                        try:
                            num1 = float(input("\nВведите sinX: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова.")
                            continue
                        if type(num1) == float:
                            print(f'Вы ввели число (X): {num1}')
                            break
                        else:
                            print("\nЧисло введено некорректно!")

                    while True:
                        try:
                            num2 = float(input("\nВведите cosX: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова.")
                            continue
                        if type(num2) == float:
                            print(f'Вы ввели число (X): {num2}')
                            break
                        else:
                            print("\nЧисло введено некорректно!")

                    result = tg(num1, num2)
                    print(f'\ntg {num1}/{num2} равнен: {result}')

                case '!':
                    while True:
                        try:
                            num1 = int(input("\nВведите число, из которого хотите вычеслить факториал: "))
                        except ValueError:
                            print("\nВы ввели некорректно число! Попробуйте снова.")
                            continue
                        if type(num1) == int and num1 >= 0:
                            print(f'Вы ввели число: {num1}')
                            break
                        else:
                            print("\nТолько положительные и натуральные числа!")

                    result = factorial(num1)
                    print(f'\nФакториал числа {num1} равен: {result}')
        else:
            print("Данной оперции нет. Попробуйте снова:")
    else:
        print("Данной оперции нет. Попробуйте снова:")