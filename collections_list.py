#collection = single variable used to store multiple values
#list = [] ordered and changeable. Allows duplicate members.
#tuple = () ordered and unchangeable. Allows duplicate members. FASTER
#set = {} unordered and unindexed/immutable, but can add or remove. No duplicate members.

#try using tuples over lists if you don't need to change the values

fruits = ["apple", "orange", "banana", "grape"]

print(fruits) #['apple', 'orange', 'banana', 'grape']
print(fruits[1]) #orange
print(fruits[-1]) #grape

print(len(fruits)) #4
print("apple" in fruits) #True  #check if apple is in the list

fruits[0]="mango" #['mango', 'orange', 'banana', 'grape']

fruits.append("kiwi") #['mango', 'orange', 'banana', 'grape', 'kiwi']   
fruits.remove("banana") #['mango', 'orange', 'grape', 'kiwi']   
fruits.insert(1, "strawberry") #['mango', 'strawberry', 'orange', 'grape', 'kiwi']
fruits.sort() #['grape', 'kiwi', 'mango', 'orange', 'strawberry'] sorting in alphabetical order
fruits.reverse() #['strawberry', 'orange', 'mango', 'kiwi', 'grape'] reverse the list

fruits.count("mango") #1 count the number of mango in the list

fruits.clear() #[] clear the list


