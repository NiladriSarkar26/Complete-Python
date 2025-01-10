# input = a function that prompts user to enter data
#          returns entered data as a string

name = "Niladri"
print(input ("what is your name "))

#ERROR:as input() gives the result as a string, we cant concatenate(+) it. 
# age = input("What is your age")
# age = age+1
# print (age)

#CORRECT
age = int(input("What is your age: "))
age+=1
print(f"My age is{age}")
