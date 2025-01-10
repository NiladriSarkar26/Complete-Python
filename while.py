#while loop = execute some code as long as a condition is true

game = input("Enter a game that you like(press q to quit): ")

while not game == 'q':  #game != "q"
    print(f"I like {game} too!")
    game = input("Enter a game that you like(press q to quit): ")

print("Goodbye!")


num=int(input("Enter a number between 1 and 10: "))

while 1<=num<=10:
    print("Enter next number between 1 and 10: ")
    num=int(input("Enter a number between 1 and 10: "))

print("Enter a correct number")
