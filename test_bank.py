from bank import bank_details

def test_bank_details():
    expected = {
        "acc_no": 10,
        "acc_no": 10,
        "name": "Shweta",
        "acc_type": "canara",
        "bal": 80000
    }

    result = bank_details(10, "Shweta", "canara", 80000)

    assert result == expected
