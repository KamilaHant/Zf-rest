from dataclasses import dataclass
import dataclasses
import json


# @dataclass
class User:

    def __init__(self, name: str):
        self.jmeno = name
        self.dluzi = dict()
        self.dluzi_mu = dict()
        self.suma = 0

    def get_dluzi(self) -> dict:
        return self.dluzi

    def set_dluzi(self, name: str, amount: float):
        if name not in self.dluzi:
            self.dluzi[name]=0
        self.dluzi[name] += amount   
        self.suma +=  amount

    def get_dluzi_mu(self) -> dict:
        return self.dluzi_mu

    def set_dluzi_mu(self, name: str, amount: float):
        if name not in self.dluzi_mu:
            self.dluzi_mu[name]=0
        self.dluzi_mu[name] += amount    
        self.suma -= amount 

    def get_suma(self, suma: float):
        self.suma = suma


class Ledger:  # definuje tridu banka s uzivately
    _users: dict[str, User]

    def __init__(self):
        self._users = dict()  # vytvor prazdny dict - konstruktor

    #GET user
    def get_user(self, name: str) -> User:  # tohle chce dopsat
        if name not in self._users:
            raise
        return self._users[name]

    #POST new user
    def add_user(self, name: str):
        if name in self._users:
            raise
        self._users[name] = User(name)

    #POST transaction (veritel, dluznik, castka)
    def transaction(self, creditor_name: str, debtor_name: str, amount: float):
        if debtor_name not in self._users:
            self.add_user(debtor_name)
        if creditor_name not in self._users:
            self.add_user(creditor_name)
       
        creditor = self.get_user(creditor_name)
        creditor.set_dluzi_mu(debtor_name,amount)
        
        debtor = self.get_user(debtor_name)
        debtor.set_dluzi(creditor_name,amount)
        # nezapomen ze to je i naopak kdo dluzi tomu je dluzny 
        # musi se pridavat ne prepisovat -> get pak set

    
