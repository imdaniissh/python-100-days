#===================================
#Accessing LIST Elements
#===================================

#Accessing Elements using Positive Index
fruits=["Apple","Banana","Mango","Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

#==================================
#Accessing Elements using Negative Index
#==================================

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])

#====================================
#Accessing Multiple Elements(Slicing)
#====================================
numbers=[10,20,30,40,50,60]
print(numbers[1:4]) #20,30,40
print(number[:3])#10,20,30
print (number[:]) #complete list


#====================================
#Check if an item exist
#====================================

fruits=["Apple","Banana","Mango"] 
print("Banana" in fruits) #True
print("Orange" in fruits) #False


