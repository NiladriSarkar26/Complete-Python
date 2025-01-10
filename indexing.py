#indexing = accesing elemetns of a sequence string using [] (index operatos)
#           [start(included) : end(excluded) : step]

credit = "1234-5678-9012-3456"

print(credit[0]) #prints 0th index -->1
print(credit[:4]) #prints from start to 4th index(excluded) -->1234
print(credit[5:9]) #prints from 5th(included) to 9th(excluded) index -->5678 
print(credit[5:]) #prints from 5th to last index -->5678-9012-3456
print(credit[::3]) #counts every 3rd character -->146-136
print(credit[-2]) #2nd last index -->5

print(credit[-4:]) #last 4 index 

#reverse the credit number, just set the step to -1
credit =credit[::-1]
print(credit)

