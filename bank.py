acc_no = input("Enter account number: ")
name = input("Enter name: ")
acc_type = input("Enter account type: ")
bal = input("Enter balance: ")

def bank_details(acc_no, name, acc_type, bal):
    return {
        "acc_no":acc_no,
        "name":name,
        "acc_type":acc_type,
        "bal":bal
    }
