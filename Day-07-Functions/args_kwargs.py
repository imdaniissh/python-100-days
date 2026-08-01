#==============================
# *args and **kwargs
#==============================

# *args allows a function to accept multiple positional arguments

#1. *args
#stored as a tuple
def add(*numbers):
  print(numbers)
  print("Sum=",sum(numbers))
add(10,20)
add(10,20,30,40,50)

#2. **kwargs
#**kwargs allows a function to accept any number of keyword arguments
#stored as a dictionary

def student(**details):
  print(details)
student(name="Danish",age=23.course="Python")

#3 using *args and **kwargs together

def demo(*args,**kwargs):
  print("Args:",args)
  print("Kwargs",kwargs)
demo(10,20,30, name="Danish", city="Delhi")
