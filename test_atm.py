from atm import ATM

def test_initial_balance():
    atm = ATM(500)
    assert atm.balance == 500

def test_deposit():
    atm = ATM(100)
    atm.deposit(50)
    assert atm.balance == 150

def test_withdraw():
    atm = ATM(200)
    atm.withdraw(50)
    assert atm.balance == 150

def test_insufficient_funds():
    atm = ATM(100)
    atm.withdraw(200)
    assert atm.balance == 100

def test_negative_deposit():
    atm = ATM(100)
    atm.deposit(-50)
    assert atm.balance == 100

def test_negative_withdraw():
    atm = ATM(100)
    atm.withdraw(-20)
    assert atm.balance == 100