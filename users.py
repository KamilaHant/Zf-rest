from dataclasses import dataclass


@dataclass
class User:
    jmeno: str
    dluzi: dict[str, float]
    dluzi_mu: dict[str, float]
    suma: float


class Bank:  # definuje tridu banka s uzivately
    _users: dict[str, dict[str, float]]

    def __init__(self):
        self._users = dict()  # vytvor prazdny dict

    def get_user(self, user: str):
        pass

    def add_user(self, user: str) -> User:
        if user in self._users:
            raise
        self._users[user] = dict()
        return User(jmeno=user, dluzi={}, dluzi_mu={}, suma=0)

    def transaction(self, debtor: str, creditor: str, amount: float):
        pass
