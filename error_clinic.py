
#Snippet 1
# x = 10
# y = 0

# if y !=0:
#     result = x / y
#     print("Result:", result)
# else:
#     print("Cannot divide by zero")

#PREDICT: I think that the error type that is going to run is ZeroDivisionError because y = 0 and you can't divide by 0.

#Snippet 2
# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(numbers[i])
#PREDICT: I think that the error type that will run is an IndexError.

#Snippet 3
# def calculate_area(radius):
#     area = 3.14 * radius ** 2
#     return area

# radius = 5
# print(calculate_area(radius))
#PREDICT: I think that that the error type that will run is a SyntaxError because there is a : missing at the end of the function.

#Snippet 4
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))
# print(is_even(7))
#PREDICT: I think that the error type to run will be a SyntaxError again because there is two :'s missing.

#Snippet 5
# for i in range(5):
#     print(i)
#PREDICT: I think it'll be a SyntaxError once again.

#Snippet 6
# def greet(name):
#     return "Hello, " + name
# print(greet("Alice"))
#PREDICT: I think that the error type that will run is also a SyntaxError because there is no '+' to join the words together.

#Snippet 7
# numbers = [1, 2, 3, 4, 5]
# total = 0

# for number in numbers:
#     total += number

# print("Sum of numbers:", total)
#PREDICT: I think that the error type that will run is an IndentationError because the for loop is not indented.

#Snippet 8
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))
#PREDICT: I think that the error type that will run is going to be an Infinite loop because 'n' is increasing, not decreasing.

#Snippet 9
# name = input("Enter your name: ")
# if name == "Alice" or name == "Bob":
#     print("Hello, " + name)
# else:
#     print("Hello, stranger!")
#PREDICT: There will be no error type, but the only thing that will run is " Hello + name".

#Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero"
    result = x / y
    

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))
#PREDICT: I think the error type that will run is an indentationError because there is nothing to specify that we cannot devide by zero.