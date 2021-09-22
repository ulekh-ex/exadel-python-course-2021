import math

def get_params(label):
    data = input(label)
    return map(int, data.split(" "))

def base_calculate():
    base, height = get_params("Enter base and height: ")
    area = round(0.5 * base * height, 2)
    print(f"Area is {area}")

def angle_calculate():
    a, b, angle = get_params("Enter 2 sides and angle(degrees) between them: ")
    area = round(0.5 * a * b * math.sin(math.radians(angle)), 3)
    print(f"Area is {area}")

def close():
    print('Goodbye')
    exit(0)

def init(variants):
    print("""
    Welcome to the triangle area calculation tool.
    
    Menu:
        1. Calculate triangle area by base and height
        2. Calculate triangle area by 2 sides and angle between them
        3. Exit
    """)
    number: int = int(input('Enter menu item number: '))

    action = variants.get(number - 1)

    if (action is None):
        print('Command not found')
        init(variants)

    action()
    init(variants)


variants = {
    0: base_calculate,
    1: angle_calculate,
    2: close
}

init(variants)