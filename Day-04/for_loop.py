#
=======================================
# For Loop in Python
#
=======================================
# Defination
#A for loop is used to iterate over a sequence or to execute a block of code a specific number of time

#Syntax
for variable in sequence:
  #code to execute
#range() function
#the range() function generates a sequence of numbers 
#syntax
#range(stop)->Starting value(default is 0)
#range(start,stop)
#range(start,stop,step)
#step-> Increment or decrement value(default is 1)
#eg
for i in range(5):
  print(i)
for i in range(2,11,2):
  print(i)
#loop through a string
word="python"
for letter in word:
  print(letter)
