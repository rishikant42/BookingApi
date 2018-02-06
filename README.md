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
      "product" : {
         "price" : 5500,
         "title" : "Ross Island + North Bay",
         "summary" : "Have fun with family"
      },
      "contact_info" : {
         "name" : "ravi",
         "ph_no" : 1245645,
         "email" : "rkp1986@gmail.com",
         "title" : "Mr"
      },
      "id" : 2,
      "travellers" : [
         {
            "name" : "mukesh",
            "nationality" : "Indian",
            "title" : "MR",
            "passport" : 123456789,
            "age" : 15
         },
         {
            "passport" : 12345,
            "title" : "MR",
            "age" : 22,
            "name" : "rakesh",
            "nationality" : "Indian"
         }
      ]
   }
]

```

* book new ticket
```
$ curl -H "Content-Type: application/json" -X POST -d '{"contact": {"name":"ravikant", "ph_no":1245645, "email":"rkp1986@gmail.com", "title":"Mr"}, "travellers":[{"title":"MR", "name":"rohit", "age":15, "nationality":"Indian", "passport":1234567 }, {"title":"MR", "name":"abhishek", "age":42, "nationality":"Indian", "passport":123468 }],  "product_id":1}' http://127.0.0.1:8000/bookticket/
```

WebHoook Test
webhook Test2
