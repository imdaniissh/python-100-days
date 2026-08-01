#===========================
#Return
#===========================
#Definition
#The return statement sebds a value back from a function 

#============================
#print() vs return
#=============================

#print()
#displays output on the screen

#return
#returns a value from the function and later can be stored in a variable

#Example
def add(a,b):
  return a+b
result=add(10,20)
print("Sum=",result)

#Return in Conditional statement

def check_even(number):
  if number%2==0:
    return "even"
  return"odd"
print(check_even(8))


