import calc

first_number = input("Enter in first number: ")
second_number = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiply/divide: ")
first_number = float(first_number)
second_number = float(second_number)

if calc.operation == "add":
    result = calc.add(first_number, second_number)
elif calc.operation == "subtract":
    result = calc.sub(calc.first_number, calc.second_number)
elif calc.operation == "multiply":
    result = calc.mult(calc.first_number, calc.second_number)
elif calc.operation == "divide":
    result = calc.div(calc.first_number, calc.second_number)
print(f"Result: {result}")
