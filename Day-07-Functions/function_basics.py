#=======================================
# FUNCTIONS IN PYTHON
#=======================================

# What is a Function?
# A function is a block of reusable code that performs a specific task

#Syntax:
# def function_name():
#    code

#==========================
#Example 1: Simple function
#==========================
def greet():
  print("hello")
greet()

#===========================
#Example 2: Function Called Multiple Times
#===========================

def say_hello():
  print("hello")
say_hello()
say_hello()
say_hello()

#===========================
#Example 3: Function with parameter
#===========================

def greet(name):
  print("hello",name)
greet("danish")
greet("at")

#============================
# Parameters vs Arguments
#============================

#Parameter-> Variable inside function
#Argument-> Actual value passed while calling the function

def student(name,age):
  print("Name",name)
  print("Age",age)
student("Danish",23)

#===========================
#Why Function ?
#===========================

#1.Code Reusability
#2.Cleaner Code
#3.Easy to Bug
#4.Better Organization







