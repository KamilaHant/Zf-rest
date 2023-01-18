from dataclasses import dataclass
import dataclasses
import json


#@dataclass
class User:
    jmeno: str
    dluzi: dict[str, float]
    dluzi_mu: dict[str, float]
    suma: float

    def __init__(self):
        self.dluzi = dict()
        self.dluzi_mu = dict()

    def get_dluzi(self) -> dict:
        return self.dluzi

    def set_dluzi(self, name: str, amount: float):
        self.dluzi[name]=amount    





class Ledger:  # definuje tridu banka s uzivately
    _users: dict[str, User]

    def __init__(self):
        self._users = dict()  # vytvor prazdny dict - konstruktor

    def get_user(self, name: str) -> User : #tohle chce dopsat
        if name not in self._users:
            raise
        x = self._users[name]
        return x    

    def add_user(self, name: str):
        if name in self._users:
            raise
        self._users[name] = User(jmeno=name,dluzi={},dluzi_mu={},suma=0)

    def transaction(self, dluznik: str, veritel: str, amount: float): #nezapomen ze to je i naopak kdo dluzi tomu je dluzny
        if dluznik not in self._users:
            raise
        self._users[veritel]= User
            



