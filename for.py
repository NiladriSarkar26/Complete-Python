#for loops = execute a block of code a fixed(known) number of times
# we can iterate over a range, string, sequence etc

for i in range(1,11): #range(1,11) means 1 to 10, 11 is not included
    print(i)
 
print("\n")

for i in reversed(range(1,10,2)): #reversed(range(1,10,2)) means 9 to 1, 10 is not included and skip 2 places
    print(i)
print("\n")

for i in range(1,21):
    if i == 13:
        continue #skip the current iteration
    elif i == 16:
        break   #break the loop
    else:
        print(i)