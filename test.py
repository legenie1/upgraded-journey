# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function


# # Calling the above function gives:
# add_ten = outer_function(10)
# answer = add_ten(5)

# # Result = 15
# print(answer)


# def decorate_me(function):
#     def beautifier():
#         print("I have been made beautiful")
#         function()
#     return beautifier


# def augly():
#     print("I am augly, i want to be beautiful")


# # Beautifying our augly() function
# decorated_function = decorate_me(augly)

# # We call the decorated_function() function
# decorated_function()


# def decorate_me(function):
#     def beautifier():
#         print("I have been made beautiful")
#         function()
#     return beautifier


# @decorate_me
# def augly():
#     print("I am augly, i want to be beautiful")


# # Calling our function
# augly()


# # A Decorator that converts all strings to uppercase representation
# def uppercase_decorator(function):
#     def wrap():
#         funct = function()
#         to_uppercase = funct.upper()
#         return to_uppercase

#     return wrap


# def split_string(function):
#     def wrap():
#         funct = function()
#         split_me = funct.split()
#         return split_me

#     return wrap

# # A simple greeting function with two decorators


# @split_string
# @uppercase_decorator
# def greetings():
#     return 'Greetings to dit students'


# # We call our greetings function
# answer = greetings()
# print(answer)


# # Our smart and intelligent divider function
# def smart_divider(function):
#     def divider(x, y):
#         print("Let me divide ", x, "by ", y)
#         if y == 0:
#             print("Sorry, can't perform the division")
#             return

#         return function(x, y)
#     return divider

# # Custom function for division


# @smart_divider
# def divider(x, y):
#     print(x/y)


# divider(4, 8)
# divider(5, 0)
# divider(10, 2)

class ClassDecorator:
    # accept the class as argument
    def __init__(self, student):
        self.student = student

    # accept the class's __init__ method arguments
    def __call__(self, name):
        # define a new display method
        def newdisplay(self):
            print('Name: ', self.name)
            print('Class: Python')

        # replace display with newdisplay
        self.student.display = newdisplay

        # return the instance of the class
        obj = self.student(name)
        return obj


@ClassDecorator
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print('Name: ', self.name)


obj = Student('Moffo Sergeo')
obj.display()
