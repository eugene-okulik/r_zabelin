# This app extracts a number from a result string and adds 10

string1 = "результат операции: 42"

string2 = "результат операции: 514"

string3 = "результат работы программы: 9"

index1 = string1.index(':') + 2

number1 = int(string1[index1:])

print(number1 + 10)

index2 = string2.index(':') + 2

number2 = int(string2[index2:])

print(number2 + 10)

index3 = string3.index(':') + 2

number3 = int(string3[index3:])

print(number3 + 10)