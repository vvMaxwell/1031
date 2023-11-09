import main

if main.operation == "add":
    result = main.add(main.first_number, main.second_number)
elif main.operation == "subtract":
    result = main.sub(main.first_number, main.second_number)
elif main.operation == "multiply":
    result = main.mult(main.first_number, main.second_number)
elif main.operation == "divide":
    result = main.div(main.first_number, main.second_number)
print(f"Result: {result}")
