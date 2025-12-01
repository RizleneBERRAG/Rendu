# Demander les trois nombres
a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = int(input("Input the third number: "))

# Trouver la médiane
median = sorted([a, b, c])[1]

print("Median of the above three numbers -")
print(median)
