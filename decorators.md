---
title: |
  "Working with Python Decorators."
date: March, 2023
lang: en-EN
urlcolor: blue
geometry: "left=2.5cm,right=2.5cm,top=3cm,bottom=3cm"
documentclass: article
fontfamily: Poppins
header-includes: |
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhf{}
  \rhead{Dakar Institute of Technology}
  \lhead{Moffo Sergeo}
  \rfoot{Page \thepage}
  \hypersetup{pdftex,
          pdfauthor={Moffo Sergeo},
          pdftitle={Working with Python Decorators},
          pdfsubject={Working with Python Decorators},
          pdfkeywords={Python, Programming, Decorators},
          pdfproducer={Emacs, Pandoc, Latex, Markdown},
          pdfcreator={Emacs, Pandoc, Latex, Markdown}}
---

# ✨ Decorators ✨

## Table of Content

1. Introduction ...........................................................................
2. Life before Decorators .................................................................
3. What are Decorators ? How it works ? ...................................................
4. Creating Decorators ....................................................................
5. Chaining Decorators ....................................................................
6. Passing arguments to Decorators ........................................................
7. Class Decorator ........................................................................
8. Some Advantages ........................................................................
9. Conclusion .............................................................................

## Prerequesite

1.  Intermediate Knowlegde of OOP - Basically Objects
2.  Understanding of Functions

## Introduction

Hello friends, In this article, we will be talking about Decorators, What they are, How to use them. To leave from a junior to Senior requires good a coding pratice so as to provide High level Code: Clean, Readable, Understandable and Reusable.

Just A decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function. A Decorator is a powerful future that doesn't only applies to Python programming but equally to other programming languages such as Java.
In this article, we will mostly focus on applying Deorators in Python.

A Decorator is represented by name which is preceded by an **@** Symbol

## Life before Decorators

In python, we have inner and outer functions commonly called ** Nested functions **

Below is an example of a nested function

```
def outer_function(x):
  def inner_function(y):
    return x + y
  return inner_function

# Calling the above function gives:
add_ten = outer_function(10)
answer = add_ten(5)
print(answer)

# Result = 15
```

Expected Result

```
15
```

The above example is a simple usecase having only one inner function i.e one function inside the other. Let's consider writing a program with alot of business logic. wrapping all these functions may cause code non-readability and will equally increase the boilerplate code. Even with a clean and clear documentation, it will remain a mystery in our future use.

Summarily, while working with functions, it's possible to:

- Nest functions i.e creating a function in side a function
- Pass argument to function
- Pass argument as function

As a solution to the above problem, it's adviceable to instead use decorators

What are decorators ? this will be the object of the next subtopic, stay focused

## What are Decorators ? How it works ?

A Decorator is simply a function that takes in a function and returns it by adding some additional functionalities.
As we said earlier, a Decorator can be identified by the Special character **@** e.g: **@Notifiable, @Getter, @Setter**.

Going more deeper, a Decorator is a any object which implements the special method `__call__()`\*\* which stands for callable. So basically a decorator is callable that returns a callable.

Below is what a decorator does

```
def decorate_me(function):
  def beautifier():
    print("I have been made beautiful")
    function()
  return beautifier

def augly():
  print("I am augly, i want to be beautiful")

```

From the above code, the **decorate_me()** functions takes in a function a beautifies it, below, we are are going to beautify our ** augly() ** function.
Let's we-write the above code and let's call the beautifier

```
def decorate_me(function):
  def beautifier():
    print("I have been made beautiful")
    function()
  return beautifier

def augly():
  print("I am augly, i want to be beautiful")

# Beautifying our augly() function
decorated_function = decorate_me(augly);

# We call the decorated_function() function
decorated_function()

```

Result

```
I have been made beautiful
I am augly, i want to be beautiful
```

## Creatiing Decorators

I guess, Like me you can find the code abit augly. yes it is, Instead of assigning the function call to the variable python provides us with the symbol **@** to permit function decoration

```
def decorate_me(function):
  def beautifier():
    print("I have been made beautiful")
    function()
  return beautifier

@decorate_me
def augly():
  print("I am augly, i want to be beautiful")

# Calling our function
augly()

```

Output

```
I have been made beautiful
I am augly, i want to be beautiful
```

The augly() function is decorated with decorate_me() decorator using the @decorate_me synthax

## Chaining Decorators

Likely to simple function as we saw in the bginning, it's equally possible to Add multiple decorators to a single function, this process is know as **Chaining**.

```
# A Decorator that converts all strings to uppercase representation
def uppercase_decorator(function):
    def wrap():
        funct = function()
        to_uppercase = funct.upper()
        return to_uppercase

    return wrap


def split_string(function):
    def wrap():
        funct = function()
        split_me = funct.split()
        return split_me

    return wrap

# A simple greeting function with two decorators


@split_string
@uppercase_decorator
def greetings():
    return 'Greetings to dit students'


# We call our greetings function
answer = greetings()
print(answer)

```

Expected Output

```
['GREETINGS', 'TO', 'DIT', 'STUDENTS']
```

# Passing arguments to Decorators

Unlike functions, we can equally pass parameters to decorators, one of the puporse of creating decorators that accept parameters is to permit code reusability
Let's create a decorator that will will divide two integers, by firstly checking the compatibility of the first over the second

```
# Our smart and intelligent divider function
def smart_divider(function):
    def divider(x, y):
      print("Let me divide ", x, "by ", y)
        if y == 0:
            print("Sorry, can't perform the division")
            return

        return function(x, y)
    return divider

# Custom function for division


@smart_divider
def divider(x, y):
    print(x/y)


divider(4, 8)
divider(5, 0)
divider(10, 2)

```

Expected output

```
Let me divide  4 by  8
0.5
Let me divide  5 by  0
Sorry, can't perform the division
Let me divide  10 by  2
5.0
```

## Class Decorator

When working using OOP, it's also possible to decorate our classes thereby providing them with additional functionalities
A clear example using a Student class is shown below

```
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
```

Expected Ouput:

```
Name:  Moffo Sergeo
Class: Python
```

NB: A Decoration can be made using a class Decorator or a Function Decorator

## Some Advantages

working with decorators has many advantages such as:

- Removing Boilerplate code
- Promotes DRY (Don't Repeat Yourself) principle
- Measuring Execution time
- Facilitate code reusability

## Conclusion

Summarily, A Decorator is simply a function that adds more flesh to an existing function or class. We have two types, **Function Decorators** and **Class Decorators**.

### TO know more

I invite you to view the following resources

- https://python-course.eu/advanced-python/decorators-decoration.php
- https://www.programiz.com/python-programming/decorator
- https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/2-functions/3-decorators/
