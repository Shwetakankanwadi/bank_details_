class BankAccount:
    def __init__(self, name, balance, account_type, account_number):
        self.name = name
        self.balance = balance
        self.account_type = account_type
        self.account_number = account_number

    def validate(self):
        if self.name and self.balance >= 0 and self.account_type in ["Savings", "Current"] and len(self.account_number) == 10:
            return True
        else:
            return False


acc = BankAccount("Shweta", 5000, "Savings", "1234567890")
print(acc.validate())
