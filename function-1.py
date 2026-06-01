#function definition: a function is a reusable block of code that performs a specific task.
# It is defined using the def keyword followed by the function name and parentheses.Functions can take parameters,
# which are values passed to the function when it is called, and they can return a value using the return statement.
# Functions help in organizing code, improving readability, and promoting code reusability.
# This code defines a function called greet that takes a name as a parameter and returns a greeting message.
# The function is then called with the argument "Alice",and the resulting greeting message is printed

def say_hello():
    print("Hello, World!")
    print("Welcome to Python programming.")
    print("------------------------------")
say_hello()
say_hello()
say_hello()
say_hello()

print("=============================================================")

def sum_numbers():
    a = 5
    b = 10
    return a + b # the next line of code will not be executed after the return statement is executed
    print("This line will not be executed.")

print("The sum of a and b is:", sum_numbers())

print("=============================================================")

name = input("what is your name? ")
family = input("what is your family name? ")

dic1 = {"name": name, "family": family}
def full_name(firstName, lastName):
    return f"{firstName} {lastName}"

print(f"full name is: {full_name(dic1['name'], dic1['family'])}")
