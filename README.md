# Helping Hands
Web app allowing NGOs to publish events and volunteers to sign up


# Things you need to get the server running:

## Tutorials:
https://gun.io/blog/setting-up-a-django-project/

https://docs.djangoproject.com/en/1.5/intro/tutorial01/


## Dependencies:
python 2.7 (trust me.)

easy_install, brew, pip

Git 1.7/1.8

virtualenv

Django==1.5

MySQL-python==1.2.5

South==1.0.2

Text editor (Sublime, vim, Komodo, gedit)

selenium (installed with easy_install)

chromedriver (installed with brew)
 
wheel==0.24.0

### Start the mysql server:

mysql.server start

### Start the django server:

cd HelpingHands/helping_hands_site

python manage.py runserver

### Synchronize database after changing settings.py

cd HelpingHands/helping_hands_site

python manage.py syncdb

./manage.py migrate