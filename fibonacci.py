try:
    count = int(input("How many Fibonacci numbers do you want? "))

    if count <= 0:
        print("Please enter a positive integer.")
    else:
        first, second = 0, 1

        for i in range(count):
            print(first, end=" ")
            first, second = second, first + second

        print()

except ValueError:
    print("Invalid input! Please enter an integer.")
