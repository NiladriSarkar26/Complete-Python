#logical operators = evaluate multiple conditions(or, and, not)
#               or = at least one condition is true
#               and = both conditions must be true  
#               not = inverts the condition(not false, not true)


weather = "sunny"

temp = 25
is_raining = True

if weather == "sunny" or temp>=25 or not is_raining:
    print("Event cancelled")
else:
    print("Event is not cancelled") 