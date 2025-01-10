#variable = container for a value(string, float, integer, boolean)


#STRINGS: series of characters, can include number as well 
name = "niladri"

print(name) #--> niladri
print("name") #--> name

#we will use f-string
print(f"Hello {name}") # --> Hello niladri, here the f stands for format, {} can be thought of as placeholder

school = "south point "
print(f"You went to {school}school") # --> You went to south point school
print("you went to " +school +"school") #this method(concatenation) only works for STRINGS


#INTEGER
age=20
num_students = 66

print(f"Your age is {age}")
#print("your class has " + num_students + " students") #concatenation will not work for strings


#FLOAT: contains decimal

price = 10.87

print(f"The price is Rs{price}")


#BOOLEAN: Ttue or False

is_student = True

if is_student:
    print("you are a student")
else:
    print("you are not a student")
