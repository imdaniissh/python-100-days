#======================================
# VARIABLE SCOPE
#======================================

# Scope determines where a variablecan be accessed.

# 1.Local Variable
def student():
  name="Danish" # Local Variable:> Created inside a function, Can only be used inside that function
  print("Inside Function:",name)
student()

#2. Global Variable
college="JMI" #Global Variable:> created outside a function, Can be accessed from anywhere in the program

def show_college():
  print("College:",college)
show_college()
print("outside function:",college)



