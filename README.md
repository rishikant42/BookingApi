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
      "price" : 5500,
      "title" : "Ross Island + North Bay",
      "summary" : "Have fun with family"
   },
   {
      "title" : "Discover Scuba",
      "price" : 2800,
      "summary" : "Best package under 3000"
   }
]
```

* Detail of single product
```
$ curl http://127.0.0.1:8000/products/1/ | json_pp

{
   "summary" : "Have fun with family",
   "about_activity" : "Ocean tribe...",
   "price" : 5500,
   "duration" : "3 hours",
   "medical_requirement" : "Yes",
   "age_requirement" : "Below 18 are not allowed",
   "title" : "Ross Island + North Bay",
   "food" : "Breakfast + Dinner",
   "about_vendor" : "have lot of activites to do...",
   "other_facilities" : "Swimming, Boating & Hotel are included",
   "id" : 1
}

```

* Create new product
```
$ curl -H "Content-Type: application/json" -X POST -d '{"title":"Discover new world", "age_requirement":"min 18", "summary":"Best package under 4000", "price":3800, "food":"Breakfast + Dinner", "about_activity":"Ocean tribe...", "about_vendro":"ocean tribe is ...."}' http://127.0.0.1:8000/products/
```

* update existing product
```
$ curl -H "Content-Type: application/json" -X PUT -d '{"medical_requirement":"Yes", "price":5500, "title":"Ross Island + North Bay"}' http://127.0.0.1:8000/products/3/
```

# Ticket booking examples

* List of booked ticket
```
$ curl http://127.0.0.1:8000/bookticket/ | json_pp

[
   {
      "travellers" : [
         {
            "passport" : 123456789,
            "name" : "amit",
            "age" : 12,
            "nationality" : "Indian",
            "title" : "MR"
         },
         {
            "nationality" : "Indian",
            "title" : "MR",
            "passport" : 12345,
            "name" : "vivek",
            "age" : 22
         }
      ],
      "product" : {
         "price" : 5500,
         "title" : "Ross Island + North Bay",
         "summary" : "Have fun with family"
      },
      "id" : 1,
      "contact_info" : {
         "email" : "rksbtp@gmail.com",
         "ph_no" : 1245645,
         "name" : "rishik",
         "title" : "Mr"
      }
   }
]

```

* book new ticket
```
$ curl -H "Content-Type: application/json" -X POST -d '{"contact":"{\"name\":\"ravi\", \"ph_no\":1245645, \"email\":\"rkp1986@gmail.com\", \"title\":\"Mr\"}", "travellers":"[{\"title\":\"MR\", \"name\":\"mukesh\", \"age\":15, \"nationality\":\"Indian\", \"passport\":123456789 }, {\"title\":\"MR\", \"name\":\"rakesh\", \"age\":22, \"nationality\":\"Indian\", \"passport\":12345 }]",  "product":2, "age":20}' http://127.0.0.1:8000/bookticket/ 
```
