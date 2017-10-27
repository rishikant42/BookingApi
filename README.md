# Booking API in Python with Djnago

Install instructions:

```
$ git clone https://github.com/rishikant42/BookingApi
$ cd BookingApi
```

Install dependencies:

```
$ pip install -r requirements.txt
```


Init DB:

```
$ python manage.py makemigrations products
$ python manage.py migrate
```

Load test data

```
$ python manage.py loaddata testdata.json
```

Run server on locathost:

```
$ python manage.py runserver
```
