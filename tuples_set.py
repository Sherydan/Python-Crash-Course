# a tuple is a collection which is ordered and unchangeable. allows duplicate members
 #create tuple 
fruits = ('Apples', 'Oranges','Grapes')
# fruits2 = tuple(('Apples', 'Orange', 'Grapes'))

# single value needs trailig comma
fruits3 = ('Apple',)

#get value
print(fruits[1])

#get length
print(len(fruits))

# print(fruits3, type(fruits3))


# a set is a collectin which is unordered and unindexed. no duplicate members

#Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

#Check if in set

print('Apples' in fruits_set)

# add to set
fruits_set.add('Grape')

# remove from set
fruits_set.remove('Grape')

#Clear set
fruits_set.clear()

#delete set

# del fruits_set

print(fruits_set)