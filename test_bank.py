import builtins
from bank import bank_details

def test_bank_details_with_mock_input(monkeypatch):
    inputs = iter(["101", "Shweta", "canara", "800000"])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs)
    )

    acc_no = int(input("Enter account number: "))
    name = input("Enter name: ")
    acc_type = input("Enter account type: ")
    bal = int(input("Enter balance: "))

    result = bank_details(acc_no, name, acc_type, bal)

    expected = {
        "acc_no":101,
        "name":"Shweta",
        "acc_type":"canara",
        "bal":800000
    }

    assert result == expected
