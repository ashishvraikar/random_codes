#code for finding greatest number among two
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

if first > second:
    print(f"The greatest number is {first}")
elif second > first:
    print(f"The greatest number is {second}")
else:
    print("Both numbers are equal")
