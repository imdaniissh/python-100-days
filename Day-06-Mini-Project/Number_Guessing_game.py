import random
target=random.randint(1,100)
attempt_count=0
while attempt_count<10:
  number=int(input("enter the number")
  
  difference=abs(target-number)
  if number==target:
             print("you have guessed the right number")
             attempt_count+=1
             print("Attempts:",attempt_count)
             score=100-(attempt_count-1)*10
             print("Score:",score)
             break
  elif number>100 or number<1:
            print("invalid number")
            continue
     
            
  elif number>target and difference>=5:
             print("too high")
             attempt_count+=1
             print("Attempt Left:",10-attempt_count)
             
             

  elif number<target and difference>=5:
             print("too low")
             attempt_count+=1
             print("Attempt Left:",10-attempt_count)
             

  else:
            print("very close")
            attempt_count+=1
            print("Attempt Left:",10-attempt_count)

if attempt_count==10:
  print("Game over")
  print("The correct number was",target)
