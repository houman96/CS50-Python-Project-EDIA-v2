from project2.project import greeting
from project2.project import disease
from project2.project import drugdose

def test_greeting():
    assert greeting("yes") == True
    assert greeting("no") == False

def test_disease():
    assert disease() == "shock" #shock
    assert disease() == "cpr" #cpr


def test_drugdose():
    assert drugdose("shock") == "3.75 mg/kg then 5-10 µg/kg/min\n" #amrinone
    assert drugdose("cpr") == "1-2 g infusion\n" #mgso4
