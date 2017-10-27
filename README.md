# Booking API in Python with Djnago

Install instructions:

```
$ git clone https://github.com/rishikant42/BookingApi
$ cd BookingApi
```

Create virtual env & Install dependencies:

```
$ virtualenv env
$ source env/bin/activate
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

# Examples

* List of products
```
$ curl http://127.0.0.1:8000/products/ | json_pp 

[
   {
      "summary" : "Best package under 2000",
      "title" : "Ross Island + North Bay",
      "price" : 1800
   },
   {
      "summary" : "Best package under 4000",
      "title" : "Discover Scuba",
      "price" : 3800
   }
]
```

* Detail of single product
```
$ curl http://127.0.0.1:8000/products/1/ | json_pp
{
   "age_requirement" : "below 18 are not allowed",
   "food" : "Breakfast + Lunch + Dinner",
   "id" : 1,
   "price" : 1800,
   "about_vendor" : "Ocean tribe with full of fun",
   "duration" : "3 hours",
   "medical_requirement" : "yes",
   "title" : "Ross Island + North Bay",
   "about_activity" : "Ocean tribe...",
   "other_facilities" : "Rain Dance + Disco",
   "summary" : "Best package under 2000"
}
```

* Create new product
```
 $ curl -H "Content-Type: application/json" -X POST -d '{"title":"Boating + Hotel", "age_requirement":"no specification", "summary":"Have fun with family", "price":4500, "food":"Breakfast + Dinner", "about_activity":"Ocean tribe...", "about_vendro":"ocean tribe is ...."}' http://127.0.0.1:8000/products/
```

* update existing product
```
$ curl -H "Content-Type: application/json" -X PUT -d '{"title":"updated title", "summary":"updated summary", "price":"updated price"}' http://127.0.0.1:8000/products/4/ 
```

# Ticket booking examples

* List of booked ticket
```
$ curl http://127.0.0.1:8000/bookticket/ | json_pp
[
   {
      "product" : {
         "summary" : "Best package under 4000",
         "price" : 3800,
         "title" : "Discover Scuba"
      },
      "first_name" : "lokesh",
      "title" : "Mr",
      "id" : 1,
      "nationality" : "Indian",
      "contact_info" : {
         "name" : "rishi",
         "ph_number" : 1245645,
         "email" : "rksbtp@gmail.com"
      },
      "last_name" : "",
      "age" : 25
   },
   {
      "last_name" : "",
      "age" : 20,
      "title" : "Mr",
      "product" : {
         "title" : "Ross Island + North Bay",
         "price" : 1800,
         "summary" : "Best package under 2000"
      },
      "first_name" : "Amit",
      "contact_info" : {
         "email" : "rksbtp@gmail.com",
         "name" : "rishi",
         "ph_number" : 1245645
      },
      "nationality" : "Indian",
      "id" : 2
   }
]
```

* book new ticket
```
$ curl -H "Content-Type: application/json" -X POST -d '{"contact":"{\"name\":\"rishi\", \"ph_no\":1245645, \"email\":\"rksbtp@gmail.com\", \"title\":\"Mr\"}", "title":"Mr", "first_name":"Rohit", "product":1, "age":20}' http://127.0.0.1:8000/bookticket/
```
