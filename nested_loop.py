#nested loop = a loop within another loop ( outer, inner)
#  outer loop:
#       inner loop:

for i in range(1,10):
    print(i, end="") #end="" means no new line, 123456789

for i in range(1,10):
    print(i,end=" ") # end=" " means space between the numbers, 1 2 3 4 5 6 7 8 9


for i in range(2): # 123456789 123456789 
    for j in range(1,10):
        print(j, end="")
    print(end=" ")
