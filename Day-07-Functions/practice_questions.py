#1. Write a function square(number) that returns the square of a number

def square(num):
  ans=num*num
  return ans
x=int(input("enter the number"))
solution=square(x)
print(solution)
      
#2. Write a function to find the greatest of two number

def greatest(a,b):
  if a>b:
    return a
  else:
    return b
x=int(input("enter the number"))
y=int(input("enter the number"))
solution=greatest(x,y)
print(solution)

#3. write a function to check even or odd number

def is_even(num):
  if num%2==0:
    return "even"
  else:
    return "odd"
num=int(input("enter the number")
print(is_even(num))

#4. write a fuction to make a calculator

    def calculator(num1,operator,num2):
      if operator== "+":
        return num1+num2
      elif operator== "-":
        return num1-num2
      elif operator== "*":
       return num1*num2
      elif operator="/":
          return num1/num2
      else:
        return "invalid operator"

      num1=int(input("enter the number")
      num2=int(input("enter the number")
      operator=input("enter the operator")
      print(calculator(num1,operator,num2)
            
               
#5. write a function to find the factorial

    def factorial(n): 
      product=1
      for i in range(1,n):
        product*=i
      return product
    n=int(input("enter the number")
    print(factorial(n))
          
      
    
