# A module is baically a file containing a set of functions to include in your application.
# there are core python modules, modules you can install using the pip manager
# including django as well as custom modules

import datetime
from datetime import date

import time 

today = date.today()

timestamp = time.time()

# pip module 
from camelcase import CamelCase

c = CamelCase()

print(c.hump('hello there world'))

print(timestamp)

# custom module

import validator
from validator import validate_email

email = 'test4testcom'

if validate_email(email):
    print('email is valid')
else:
    print('email is invalid')

