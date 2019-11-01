# a dictionary is a collection which is unordered , changeable and indexed. no duplicate members

#create dict
person = {
    'first_name': 'Luis',
    'last_name':  'Tobar',
    'age': 27
}

# use constructor

# person2 = dict(first_name = 'Jhon', last_name = 'Doe')

#get a value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

print(person)

# get keys

print(person.keys())

#get items
print(person.items())

#copy dict

person2 = person.copy()
person2['city'] = 'Chimbarongo'

# print(person2)

#remove item

del(person['age'])
person.pop('phone')

#clear 
person.clear()

# get length
print(len(person2))

#list of dict

people = [
    {'name': 'Juan', 'age': 24},
    {'name': 'Pedro', 'age': 30}
]

print(people)

print(people[1]['name'])



# print(person2, type(person))