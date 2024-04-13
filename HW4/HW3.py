transactions = []

def check_balance(balance):
    print(f"Ваш текущий баланс: {balance} рублей")

def deposit(balance, amount):
    global transactions
    balance += amount
    transactions.append(f"Пополнение: +{amount} рублей")
    print(f"Вы внесли {amount} рублей")
    return balance

def withdraw(balance, amount):
    global transactions
    if amount > balance:
        print("Недостаточно средств на счете")
    else:
        balance -= amount
        transactions.append(f"Снятие: -{amount} рублей")
        print(f"Вы сняли {amount} рублей")
    return balance

def print_transactions():
    print("История операций:")
    for transaction in transactions:
        print(transaction)

def atm_operations():
    balance = 0
    while True:
        print("\n1. Проверить баланс")
        print("2. Внести деньги")
        print("3. Снять деньги")
        print("4. Вывести историю операций")
        print("5. Выйти")

        choice = input("Выберите операцию: ")

        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            amount = float(input("Введите сумму для пополнения: "))
            balance = deposit(balance, amount)
        elif choice == '3':
            amount = float(input("Введите сумму для снятия: "))
            balance = withdraw(balance, amount)
        elif choice == '4':
            print_transactions()
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите операцию из списка.")

atm_operations()
