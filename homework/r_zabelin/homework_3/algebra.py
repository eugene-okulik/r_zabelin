# This app takes two numbers x and y and calculates the expression x - y/5 + x*y.

# Block 1: testing integer numbers

first_num1 = 5

second_num1 = 3

print("Block 1:  int")

print("x - y / 5 + x * y =", (first_num1 - second_num1 / 5) + (first_num1 * second_num1))

# Block 2: testing float numbers

first_num2 = 2.5

second_num2 = 4

print("Block 2: float")

print("x - y / 5 + x * y =", (first_num2 - second_num2 / 5) + (first_num2 * second_num2))

# Block 3: testing negative numbers

first_num3 = -7

second_num3 = 2.3

result_step1_b3 = second_num3 / 5

result_step2_b3 = first_num3 - result_step1_b3

result_step3_b3 = first_num3 * second_num3

final_result_b3 = result_step2_b3 + result_step3_b3

print("Block 3: negative num")

print("x - y / 5 + x * y =", final_result_b3)

# Block 4: testing zero

first_num4 = 0

second_num4 = 3.14

result_step1_b4 = second_num4 / 5

result_step2_b4 = first_num4 - result_step1_b4

result_step3_b4 = first_num4 * second_num4

final_result_b4 = result_step2_b4 + result_step3_b4

print("Block 4: zero")

print("x - y / 5 + x * y =", final_result_b4)
