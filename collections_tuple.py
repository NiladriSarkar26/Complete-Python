fruits = ("apple", "orange", "banana", "grape")

print(fruits) #('apple', 'orange', 'banana', 'grape')   
print(fruits[1]) #orange    
print(fruits.count("apple")) #1

for fruit in fruits:
    print(fruit)

# fruits[0]="mango" #TypeError: 'tuple' object does not support item assignment 