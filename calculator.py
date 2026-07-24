# calculator.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choice: ")

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
elif choice == "3":
    print(a * b)
elif choice == "4":
    print(a / b)
else:
    print("Invalid")
