#username must not contain digits

username=input("Enter a username: ")

if len(username) >12: #length of username
    print("username musn't exceed more than 12 characters")
elif not username.find(" ")==-1:  #if results find space
    print("Your username cant contain spaces")
elif not username.isalpha(): #if result contains numeric value
    print("Your username cant contain numbers")
else:
    print(f"Welcome {username}")