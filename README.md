# RESTful API for tracking transactions
written by: Kamila Hantova

Simple ledger API to add new user and transactions in style "who - to who - how much".

## Prerequisities 

- Python 3.10.9
- web browser

### How to run

```
python main.py
```

Go to we browser:

[localhost:81](localhost:81/)

It is possible to add suffix to the URL dependent on the required method

Get user by name: ``/user/<user_name>``

Add new user: ``/add``

Add transaction: ``/transaction``

### Methods

Datas of users are given in formate: 
```
{
"jmeno": "",
"dluzi": {
"jmeno": caska,
},
"dluzi_mu": {
"jmeno": caska,
},
"suma": "<(celková dlužená částka) - (celková dlužná částka)>"
}
```

#### GET

Get information of one user by name. 

[localhost:81/user/<name>](localhost:81/user/)

#### POST

1. Add new use by payload: ``{"user":<name of new user(unique)>}``

[localhost:81/add](localhost:81/add)

2. Add new transaction: ``{"veritel":<name of creditor>,"dluznik":<name of debtor>,"castka":amount}``

[localhost:81/transaction](localhost:81/transaction)


