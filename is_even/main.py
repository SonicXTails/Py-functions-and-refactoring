check = bool
def is_even(number):
    result = number % 2
    if result == 0:
        check = True
    else:
        check = False
    return check


number = float(input("Введите число: "))
number = is_even(number)
print("Чётность:", number)
