# calculator.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")

choice = input("Enter choice: ")

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
else:
    print("Invalid choice")
