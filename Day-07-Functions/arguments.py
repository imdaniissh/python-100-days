#===================================
#FUNCTION ARGUMENTS
#===================================

#Arguments are values passed to a functiom

#1.Positional Argument

def introduce(name,age):
  print("Name",name)
  print("Age",age)
introduce("Danish",23)

#2.Keyword Argument

def student(name,course):
  print("Name:",name)
  print("Course:",course)
student(course="python",name="danish")

#3. Default Arguments

def country(name,country="India"):
  print(name,"is from",country)
  country("Danish")
  country("John","USA")


