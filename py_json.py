import json

userJSON = '{"first_name": "John", "last_name": "Koe", "Age": 30}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {'make': 'ford', 'model': 'fiesta', 'year': 2018}

carJSON = json.dumps(car)

print(carJSON)