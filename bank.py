
def bank_details(account_number, holder_name, account_type, balance):
    print("\nBank Account Details")
    print("---------------------")
    print("Account Number :",account_number)
    print("Account Holder :",holder_name)
    print("Account Type   :",account_type)
    print("Balance        :",balance)

acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = input("Enter account balance: ")

bank_details(acc_no, name, acc_type, balance)
