import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_triangle_sides(x1, y1, x2, y2, x3, y3):
    side1 = distance(x1, y1, x2, y2) *60 /37.5
    side2 = distance(x2, y2, x3, y3) *60 /37.5
    side3 = distance(x3, y3, x1, y1) *60 /37.5

    return side1, side2, side3

# Nhập tọa độ của ba điểm a, b, c
x1, y1 = map(float, input("Nhập tọa độ của điểm a (x y): ").split())
x2, y2 = map(float, input("Nhập tọa độ của điểm b (x y): ").split())
x3, y3 = map(float, input("Nhập tọa độ của điểm c (x y): ").split())

# Tính độ dài của ba cạnh tam giác
side1, side2, side3 = calculate_triangle_sides(x1, y1, x2, y2, x3, y3)

# In kết quả
print(f"Độ dài của ba cạnh tam giác là: {side1}, {side2}, {side3}")
