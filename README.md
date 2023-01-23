# RESTful API for tracking transactions

written by: Kamila Hantova

Simple ledger API to add new user and transactions in style "who - to who - how much".

## Prerequisities 

- Python 3.10.9
- web browser

## How to run

```bash
python main.py
```

Go to web browser:

[http://localhost:81](http://localhost:81/)

It is possible to add suffix to the URL dependent on the required method

Get user by name: ``/user/<user_name>``

Add new user: ``/add``

Add transaction: ``/transaction``

### Methods

Data of users are given in format: 

```json
{
    "jmeno": "",
    "dluzi": {
        "<jmeno_veritele>": <dluzna_castka>
    },
    "dluzi_mu": {
        "<jmeno_dluznika>": <dluzna_castka>
    },
    "suma": "<(celková dlužená částka) - (celková dlužná částka)>"
}
```

#### GET

Get information of one user by name. 

[localhost:81/user/<name>](localhost:81/user/)

#### POST

1. Add new user: ``{"user":<name of new user(unique)>}``

[localhost:81/add](localhost:81/add)

2. Add new transaction: ``{"veritel":<name of creditor>,"dluznik":<name of debtor>,"castka":amount}``

[localhost:81/transaction](localhost:81/transaction)

## Test


### How to run 

```bash
pytest
```
