from users import Ledger

ledger = Ledger()

def test_transaction():
    ledger.transaction("Marek", "Michal", 10.0)
    assert "Michal" in ledger.get_user("Marek").dluzi_mu
    assert "Marek" in ledger.get_user("Michal").dluzi
