#create function
def sayhello(name = 'Sam'):
    print(f'Hello {name}')

sayhello('luis')

#return value
def getSum(num1, num2):
    total = num1 + num2
    return total
num = getSum(99, 9)
print(num)

#lambda functuion is a smallm anonymus function
# a lambda function can take any nymber of arguments, but can only have one expression.
# very similar to JS arrow functions
getSum2 = lambda num1, num2: num1 + num2

print(getSum2(10, 3))