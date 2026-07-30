#1
#use for loop to print number from 1 to 10
for i in range(1,11):
  print(i)

#2.Print numbers from 1 to 100:
#Skip numbers divisible by 3 using continue.
#Stop the loop when the number reaches 50 using break.
for i in range(1,101):
  if i%3==0:
    continue
  elif i==50:
    break
  print(i)

#3.Create a password authentication system.
#The correct password is "python123".
#Keep asking the user to enter the password until it is correct.
#Print "Access Granted" and exit the loop.
password=input("enter the password")
while True:
  if password=="python123":
    print("access granted")
    break
  else:
    print("Wrong password.Try again.")


    
