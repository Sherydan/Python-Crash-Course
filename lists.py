#create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'oranges', 'Grapes','Pears']

#use a constructor
# numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)

#get a value
print(fruits[1])

#get length
print(len(fruits))

# apend
fruits.append('Mangos')

#remove
fruits.remove('oranges')

#insert into position
fruits.insert(2, 'Strawberries')

#change a value 
fruits[0] = 'Blueberries'

#remove from certain position (pop)

fruits.pop(2)

#reverse
fruits.reverse()

#sort list
# CASE SENSITIVE, IT DOESNT SORT A STRING WITH LOWERCASE ALONGSIDE WITH ONE WITH UPPERCASE

fruits.sort()

#reverse list
fruits.sort(reverse=True)


print(fruits)

