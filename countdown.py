import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

# time.sleep(3) #sleep function of the time module
