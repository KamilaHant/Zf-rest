import dataclasses

from users import User, Bank
import json


def test_bank():
    bank = Bank() #vytvor banku
    assert bank.add_user("Petr") == User(jmeno="Petr", dluzi={}, dluzi_mu={}, suma=0)  # pridej uzivatele
    try:
        bank.add_user("Petr")  # pridej uzivatele
        assert False
    except Exception as e:
        assert not isinstance(e, AssertionError),"repeated addition should failed"
        print("user is already there")
        pass


def test_form_user_json():
    user = User(jmeno="Petr",
                dluzi={"Pavel": 15.0,
                       "Jiri": 1.0,
                       "Dan": 4.5},
                dluzi_mu={"Jakub": 2.5,
                          "Pavel": 6.75},
                suma=10)
    print(json.dumps(dataclasses.asdict(user)))


if __name__ == "__main__":
    test_bank()
   # test_form_user_json()

