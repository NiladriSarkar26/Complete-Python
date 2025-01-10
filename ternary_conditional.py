#conditional expression = A one-line shortcut for the if-else statement(TERNARY OPERATOR)
#                         print or assign one of two values based on a condition
#                         x if condition else y

num = -6

print("odd" if num%2!= 0 else "even")

a=-73
result = "Positive" if a>0 else "Negative or 0"
print(result)


m=19
n=34
max_num= m if m>n else n #read as: return m if m>n,else return n
print(max_num)