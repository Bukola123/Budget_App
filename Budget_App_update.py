database = {} 
class budget:
    def __init__(self,needs,balance):
        self.needs = needs
        self.balance = balance
        
    def deposit(deposit_amt,balance): 
        balance += deposit_amt 
        return balance
       
    def transfer(database,giver , receiver, trans_amt):
        trans_giver = database[giver]
        trans_receiver = database[receiver]
        database[receiver] = int(trans_receiver) + trans_amt
        database[giver] = int(trans_giver) - trans_amt
        return database
    def withdraw(with_cat,with_amt,balance):
        balance -= with_amt
        return balance
    def balance(new_bal):
        for key, value in database.items():
            print(key,value)
    #def transfer(balance,cat_1,tran_amt, cat_2):
        #cat_1 = 

def start():
    print('Available Options \n')
    print('0 Create new category \n')
    print('1 Deposit \n')
    print('2 Withdraw \n')
    print('3 Transfer \n')
    print('4 Check balance \n')
    start = int(input())
    if start == 0:
        create()
        end()
    elif start == 1:
        deposit()
        end()
    elif start == 2:
        withdraw()
        end()
    elif start == 3:
        transfer()
        end()
    elif start == 4:
        check_balance()
        end()
            
def create():
    new_cat = input('Enter new categories name \n')
    new_bal = 0
    create_budget = budget(new_cat,new_bal)
    database[new_cat] = new_bal
    
    
def deposit():
    depo_cat = input('Enter category to fund \n')
    if depo_cat in database:
        deposit_amt = int(input('Enter amount to deposit \n'))
        balance = int(database[depo_cat])
        depo_budget = budget.deposit(deposit_amt,balance) #transferring info back to deposit function inside budget
        database[depo_cat] = depo_budget
    else:
        error()
def transfer():
    print('You are about to transfer \n')
    giver = input('Enter Category to transfer from \n')
    receiver = input('Enter category to receive fund \n')
    db_giver = database[giver]
    db_receiver = database[receiver]
    if giver and receiver in database:
        trans_amt = int(input('Enter amount to transfer \n'))
        if trans_amt <= db_giver:
            trans_final = budget.transfer(database, giver , receiver, trans_amt)
            for key, value in trans_final.items():
                print(key,value)
    else:
        print('One of the category input is not correct, try again')
        
    
def withdraw():
    with_cat = input('Enter category to withdraw \n')
    if with_cat in database:
        with_amt = int(input('Enter amount to withdraw \n'))
        balance = int(database[with_cat])
        if with_amt <= balance:
            with_budget = budget.withdraw(with_cat,with_amt,balance)
            database[with_cat] = with_budget
        else:
            print('Insufficient Fund')
    else:
        error()
def check_balance():
    check_cat = input('Enter category to check balance')
    if check_cat in database:
        balance = budget.balance(check_cat)
        print(balance)
def end():
    print('1 Did you want to perform another operation \n')
    print('2 logout \n')
    end = int(input())
    if end == 1:
        start()
    elif end == 2:
        logout()
    else:
        print('You have selected an invalid option, you are hereby logout \n')
        logout()
def logout():
    print('Thank you for using Budget App')

def error():
    print('Category not found, try again or create category \n')
    print('1 Try again \n')
    print('Create category \n')
        
def login():
    print('Welcome to Budget App \n')
    start()
    
    
login()
