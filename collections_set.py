fruits = {"apple", "orange", "banana", "grape"}
print(fruits) #{'banana', 'apple', 'orange', 'grape'}   #unordered

fruits.add("kiwi") #{'kiwi', 'banana', 'apple', 'orange', 'grape'} 
fruits.add("kiwi") #{'kiwi', 'banana', 'apple', 'orange', 'grape'}  #NO DUPLICATE
fruits.remove("banana") #{'kiwi', 'apple', 'orange', 'grape'}   

fruits.pop() #randomly removes an item {'apple', 'orange', 'grape'}
fruits.clear() #set() clear the set
