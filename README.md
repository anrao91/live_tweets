LiveTweets
=======

LiveTweet is a simple django app which retriews tweets of a given hashtag

## Getting started

* Install requirements in the virtualenv

```
virtualenv venv
source ./venv/bin/activate
xargs -a requirements.txt -n 1 pip install
```

* Run the inital migrations

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


* When new migrations need to be created

```
python manage.py makemigrations
python manage.py migrate
```
