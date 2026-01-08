from bank import bank_details

def test_bank_details():
    expected = {
        "acc_no": 101,
        "name": "Shweta",
        "acc_type": "canara",
        "bal": 800000
    }

    result = bank_details(101, "Shweta", "canara", 800000)

    assert result == expected
