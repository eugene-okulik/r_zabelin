# This app takes the two legs of a right triangle and calculates its hypotenuse and area.

# Block 1: testing integer numbers

first_num1 = 5

second_num1 = 3

hypotenuse1 = (first_num1 ** 2 + second_num1 ** 2) ** 0.5

area1 = (first_num1 * second_num1) / 2

print("Block 1: int")

print("Hypotenuse = ", hypotenuse1)

print("Area = ", area1)

# Block 2: testing float numbers

first_num2 = 2.5

second_num2 = 4

hypotenuse2 = (first_num2 ** 2 + second_num2 ** 2) ** 0.5

area2 = (first_num2 * second_num2) / 2

print("Block 2: float")

print("Hypotenuse = ", hypotenuse2)

print("Area = ", area2)

# Block 3: testing negative numbers

first_num3 = -7

second_num3 = 2.3

hypotenuse3 = (first_num3 ** 2 + second_num3 ** 2) ** 0.5

area3 = (first_num3 * second_num3) / 2

print("Block 3: negative num")

print("Hypotenuse = ", hypotenuse3)

print("Area = ", area3)

# Block 4: testing zero

first_num4 = 0

second_num4 = 3.14

hypotenuse4 = (first_num4 ** 2 + second_num4 ** 2) ** 0.5

area4 = (first_num4 * second_num4) / 2

print("Block 4: zero")

print("Hypotenuse = ", hypotenuse4)

print("Area = ", area4)
