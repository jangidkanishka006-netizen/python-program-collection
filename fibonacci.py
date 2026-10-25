
# Fibonacci Series Program

terms = int(input("How many terms do you want? "))

first, second = 0, 1

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")

    for i in range(terms):
        print(first, end=" ")
        first, second = second, first + second
