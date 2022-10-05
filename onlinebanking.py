
# function to load
from operator import truediv

# load user names into a list of dictionaries
def load_user():
    file = open('data.txt', 'r')

    users = [] 

    for line in file.readlines():
        user = {}
        user_list = line.split(',')
        user["username"] = user_list[0]
        user["password"] = user_list[1]
        user["fullname"] = user_list[2]
        user["balance"] = int(user_list[3])
        users.append(user)

    file.close()

    return users

# prompt user for username and password
def prompt_user(users): 
    username = input("\nInput username: ")
    password = input("Input password: ")

    for user in users:
        if username == user["username"] and password == user["password"]:
            return user

# display full name and account balance
def display_account(user):
    if (user):
        print(f"Name: {user['fullname']}")
        print(f"Balance: ${user['balance']}")
        deposit_withdraw = input("\nWithdraw or Deposit (Press any key to quit): ")
        if deposit_withdraw.lower() == "deposit":
            deposit(user)
        elif deposit_withdraw.lower() == "withdraw":
            withdraw(user)
    else:
        print("Username and password not found")

# adds funds to user balance 
def deposit(user):
    deposit_amount = int(input("\nDeposit amount: \n$"))
    user["balance"] += deposit_amount
    print(f"\nUpdated Balance: ${user['balance']}")

# removes funds from user balance
def withdraw(user):
    withdraw_amount = int(input("\nWithdraw amount: \n$"))
    user["balance"] -= withdraw_amount
    if user["balance"] < 0:
        print(f"\nDang, you're in the negatives bro")
    print(f"Updated Balance: ${user['balance']}")



users = load_user()
validuser = prompt_user(users)
display_account(validuser)