
# Factorial Program
# Factorial of n = 1 * 2 * 3 * ... * n

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial of", number, "is", factorial)
