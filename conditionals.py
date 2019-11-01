# IF / ELSE 
x = 1
y = 1

# comparision operators (==, !=, >, <,>=, <=)

#simple
# if x > y:
#     print(f'{x} is greater than {y}')


# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{y} is greater than {x}')

# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less or equal to 10')

# logical operators (and, or, not)
# if x > 2 and x <= 10:
#     print(f'{x} is greater than 2 and less or equal to 10')

# if not(x==y):
#     print(f'{x} is not equal to {y}')


#member ship operators

numbers = [1,2,3,4,5]

# IN
if x in numbers:
    print(x in numbers)

# NOT IN
if x not in numbers:
    print(x not in numbers)

# identity operators
if x is y:
    print(f'{x} is {y}')

if x is not y:
    print(f'{x} is {y}')