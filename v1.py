

with open('i3.txt', 'r') as file:
    a = int(file.readline().strip())
    b = int(file.readline().strip())
    c = int(file.readline().strip())
    x = int(file.readline().strip())

y = (a * (x ** 2)) + (b * x) + c
print(f"Value of y: {y}")













