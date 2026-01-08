def bank_details(acc_no, name, acc_type, bal):
    return {
        "acc_no": acc_no,
        "name": name,
        "acc_type": acc_type,
        "bal": bal
    }

if __name__ == "__main__":
    acc_no = int(input("Enter account number: "))
    name = input("Enter name: ")
    acc_type = input("Enter account type: ")
    bal = int(input("Enter balance: "))

    result = bank_details(acc_no, name, acc_type, bal)
    print(result)
