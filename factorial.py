try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Please enter a non-negative number.")
    else:
        factorial = 1

        for i in range(1, number + 1):
            factorial *= i

        print("Factorial of", number, "is", factorial)

except ValueError:
    print("Invalid input! Please enter an integer.")
    