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
        self.suma -=  amount

    def get_dluzi_mu(self) -> dict:
        return self.dluzi_mu

    def set_dluzi_mu(self, name: str, amount: float):
        if name not in self.dluzi_mu:
            self.dluzi_mu[name]=0
        self.dluzi_mu[name] += amount    
        self.suma += amount 

    def get_suma(self, suma: float):
        self.suma = suma


class Ledger:  # definuje tridu banka s uzivately
    _users: dict[str, User]

    def __init__(self):
        self._users = dict()  # vytvor prazdny dict - konstruktor

    def get_user(self, name: str) -> User:  # tohle chce dopsat
        if name not in self._users:
            raise
        return self._users[name]

    def add_user(self, name: str):
        if name in self._users:
            raise
        self._users[name] = User(name)

    # nezapomen ze to je i naopak kdo dluzi tomu je dluzny 
    # musi se pridavat ne prepisovat -> get pak set
    def transaction(self, dluznik_name: str, veritel_name: str, amount: float):
        if dluznik_name not in self._users:
            self.add_user(dluznik_name)
        if veritel_name not in self._users:
            self.add_user(veritel_name)
       
        veritel = self.get_user(veritel_name)
        veritel.set_dluzi_mu(dluznik_name,amount)
        
        dluznik = self.get_user(dluznik_name)
        dluznik.set_dluzi(veritel_name,amount)
        

    
