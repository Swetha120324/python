import math

history = []

while True:
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sin")
    print("8. Cos")
    print("9. Log")
    print("10. History")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "0":
        print("Bye da 👋")
        break

    elif choice in ["1","2","3","4","6"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = a + b
            op = "+"
        elif choice == "2":
            result = a - b
            op = "-"
        elif choice == "3":
            result = a * b
            op = "*"
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero ❌")
                continue
            result = a / b
            op = "/"
        elif choice == "6":
            result = a ** b
            op = "^"

        print("Result:", result)
        history.append(f"{a} {op} {b} = {result}")

    elif choice == "5":
        a = float(input("Enter number: "))
        if a < 0:
            print("Invalid input ❌")
            continue
        result = math.sqrt(a)
        print("Result:", result)
        history.append(f"sqrt({a}) = {result}")

    elif choice == "7":
        a = float(input("Enter angle (degrees): "))
        result = math.sin(math.radians(a))
        print("Result:", result)
        history.append(f"sin({a}) = {result}")

    elif choice == "8":
        a = float(input("Enter angle (degrees): "))
        result = math.cos(math.radians(a))
        print("Result:", result)
        history.append(f"cos({a}) = {result}")

    elif choice == "9":
        a = float(input("Enter number: "))
        if a <= 0:
            print("Invalid input ❌")
            continue
        result = math.log(a)
        print("Result:", result)
        history.append(f"log({a}) = {result}")

    elif choice == "10":
        print("\n--- History ---")
        for h in history:
            print(h)

    else:
        print("Invalid choice ❌")