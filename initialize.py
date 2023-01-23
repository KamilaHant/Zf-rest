
def initialize_data(ledger):
    ledger.add_user("Petr")
    ledger.transaction("Pavel", "Petr", 15.0)
    ledger.transaction("Petr", "Jakub", 2.5)
