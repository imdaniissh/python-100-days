#
================================
#infinite loop
================================
#Definition
#An infinite loop is a loop that keeps running continuosly because its stopping condition never become false
#example
while True:
  print("hello")

#Real life uses 
# 1.ATM Machine
# 2.Games
# 3.Chat Application

#
=================================
#break statement
=================================
#Definition 
#The break Statement is used to immediately terminate a loop. When Python encounters break, it exits the loop and continues executing the code after the loop

#example
while True:
  name=input("enter your name")
  if name=="exit":
    break
  print("hello",name)
#Real life use:
#GAME:-if player press "Quit" then game will close
#Search:- if we find the required item search will stop

#
====================================
#Continue statement
====================================
#The continue statement is used to skip the current iteration of a loop and move directly to next iteration 

#use of continue
#1. for skiiping iteration for a particular condition

#example:
for i in range(1,6):
  if i==3:
    continue
  print(i)
  
