# format specifiers = {value:flags} format a value based on what flags are inserted
#
# .(number)f = round to that many decimal places (fixed point)
# (number) = allocate that many spaces
# 03 = allocate and zero pad that many spaces
# < = left justify
# > = right justify
# ^ = center align
# + = use a plus sign to indicate positive value
# = = place sign to leftmost position
# ' ' = insert a space before positive numbers
# , = comma separator


price1= 3.1467
price2 = -987.56
price3= 1200000.654

print(f"Price 1 is ${price1:.2f}") #:.2f means round off to decimal upto 2 places
print(f"Price 2 is ${price2:9}") #allocate 9 space to the number, if number is say of 7 digit, the starting 2 digit will be spaces and if we say :4 but number is of 7 digit, then number will be printed as it is i.e, of 7 digits
print(f"Price 3 is ${price3:+,.4f}")