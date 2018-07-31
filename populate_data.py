import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django

django.setup()

## FAKE POPULATION SCRIPT
import random

from appTwo.models import User
from faker import Faker


# create instance of faker object
fakegen = Faker()

def populate(number):
	for entry in range(number):
		fake_first = fakegen.first_name()
		fake_last = fakegen.last_name()
		fake_email = fakegen.email()

		# create new user entry
		new_user = User.objects.get_or_create(
			first_name=fake_first, 
			last_name=fake_last, 
			email=fake_email)[0]

if __name__ == '__main__':
	print('populating script!')
	populate(20)
	print('populating complete!')
