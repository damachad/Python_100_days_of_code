from art import logo

# Calculator functions

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Dictionary with basic functions associated to their symbols

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# Recursive function to calculate a result with any given two numbers and an operation symbol

def calculator():
  print(logo)

  previous_num = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  switch = True
  
  while switch == True:
    operation_symbol = input("Pick an operation: ")
    next_num = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(previous_num, next_num)
    
    print(f"{previous_num} {operation_symbol} {next_num} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower() == 'y':
      previous_num = answer
    else:
      switch = False
      calculator()

calculator()
