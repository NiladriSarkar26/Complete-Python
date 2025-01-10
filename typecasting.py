#typecasting: the process of converting a variable from one datatype to another
#                str(), int(), float(), bool()

name = "Simsung"
age= 20
gpa = 9.0
is_student=True

age = float(age)
print(age) #-->20.0

age = str(age)
print(type(age)) #--> <class 'str'>

# age+=1   #will give error as we cant concatenate an int with a string
age+= "1"
print(age) #-->201

bool_name=bool(name)
print(bool_name) # --> true

bool_name=bool("")
print(bool_name) #-->false, any empty string
