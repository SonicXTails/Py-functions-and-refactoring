width = float
height = float
result = float
rec = int


def rectangle_area (width, height):
    result = width * height
    return result

#code
#code
#code
#code
#code

while True:
    rec = int(input("\nВведите операцию, (1, 2): "))
    match rec:
        case 1:
            result = rectangle_area(100, 300)
            print("Площадь данного прямоугольника:",result)
        case 2:
            width = float(input("Введите ширину: "))
            height = float(input("Введите высоту: "))
            result = rectangle_area(width, height)
            print("Площадь данного прямоугольника:", result)