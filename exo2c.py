numbers = []

input_len = int(input("enter input len : "))

for i in range(input_len) :
    val = float(input(f"Enter number{i + 1} : "))
    numbers.append(val)

numbers.sort()

n = len(numbers)
mid = n // 2

if n % 2 == 1:
    median = numbers[mid]
else:
    median = (numbers[mid - 1] + numbers[mid]) / 2

print("median :", median)