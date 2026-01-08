
def bank_details(acc_no, name, acc_type, balance):
    print("\nBank Details")
    print("-------------")
    print("Account Number :", acc_no)
    print("Account Holder :", name)
    print("Account Type   :", acc_type)
    print("Balance        :", balance)

acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = input("Enter balance: ")

bank_details(acc_no, name, acc_type, balance)
