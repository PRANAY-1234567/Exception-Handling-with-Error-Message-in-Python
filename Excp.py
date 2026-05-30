print("Program starts...")

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a / b

    print("The division of", a, "and", b, "is", c)

except Exception as e:
    print("Error in data :", e)

print("Program ends...")