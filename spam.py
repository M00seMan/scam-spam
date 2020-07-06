#!/usr/bin/env python

import requests
import os
import random
from random import randint
import secrets
import string
import json

chars = string.ascii_letters + string.digits + '!?*@$'
alphabet = string.ascii_letters + string.digits
random.seed = (os.urandom(1024))

url             = ''
username_field  = ''
password_field  = ''

names 	    = json.loads(open('names.json').read())
lastnames   = json.loads(open('lastnames.json').read())
emails 	    = json.loads(open('emails.json').read())

try:
	for i in i:
        

       name = random.choice(names)
        lastname = random.choice(lastnames)
        email = "@" + random.choice(emails)

        #name_extra = ''.join(random.choice(string.digits))
        name_extra = ''.join(str(random.randint(1, 999)))


        usernamegen = [
            name.lower() + name_extra + email,
            name.lower() + '.' + lastname.lower() + email,
            name.lower() + '.' + lastname.lower() + name_extra + email
        ]
        username = random.choice(usernamegen)


        lenght = random.randint(8, 18)
        pwgen = [
            username + str(random.randint(100, 9999)),
            str(random.randint(100, 9999)) + username + str(random.randint(100, 9999)),
            str(random.randint(100, 9999)) + username,
            ''.join(secrets.choice(alphabet) for i in range(lenght))
        ]
        password = random.choice(pwgen)


		requests.post(url, allow_redirects=False, data={
			username_field : username,
			password_field : password
		})


		print(f'Spamming username {username} and password {password}')

except KeyboardInterrupt:
	pass

except requests.exceptions.MissingSchema:
	print "Invalid URL"
