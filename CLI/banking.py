import sys
import getopt
import json
import os

database='bank_database.json'
user_data={}

def save_user_in_db():
    with open(database,'w') as f:
        json.dump(user_data,f,indent=4)# dump means write in json file
        
def load_users_data():
    global user_data #otherwise it will create new file everytime
    if os.path.exists(database):#checking if the file is in the path or not
        with open(database,'r') as f:
            user_data=json.load(f)# load means read in json file
def register_user(username,password):
    if username not in user_data:
        user_data[username] ={'password': password,'balance':0.0}
        save_user_in_db()
    else:
        print(f"User '{username}' already exists. Please choose a different username.")
        

def login(username, password):
    if username in user_data and user_data[username]["password"] == password:
        return True
    else:
        print("Invalid credentials. Please check your username and password.")
        return False
    
def display_balance(username):
    password = input('Please enter your password : ')
    if login(username,password):
        print(f"Your account balance is ${user_data[username]['balance']:.2f}")
    else:
        print('Invalid username/password')
        sys.exit(2)
        
def deposit(username, amount):
    password = input('please enter your password : ')
    if login(username,password):
        user_data[username]["balance"]+= amount
        save_user_in_db()
        print(f"Deposited ${amount:.2f}. New balance: ${user_data[username]['balance']:.2f}")
    else:
        print('Invalid username/password')
        sys.exit(2)
        
def withdraw(username, amount):
    password = input('please enter your password : ')
    if login(username,password):
        if user_data[username]['balance'] >= amount:
            user_data[username]["balance"] -= amount
            save_user_in_db()
            print(f"Withdrew ${amount:.2f}. New balance: ${user_data[username]['balance']:.2f}")
        else:
            print("Insufficient funds.")
    else:
        print('Invalid username/password')
        sys.exit(2)
        
def main(arguments):
    load_users_data()
    short_options = 'r:d:w:b'
    long_options =['register=','deposit=','withdraw=','balance=']
    try :
        opts,args=getopt.getopt(arguments,short_options,long_options)
    except getopt.error as e:
        print(f'something bad happened {e}')
        sys.exit(2)
    for opt , value in opts:
        if opt in ('-r','--register'):
            #username:password
            username,password=value.split(':')
            register_user(username,password)
        elif opt in ('-b','--balance'):
            display_balance(args[0])           
        elif opt in ('-d','--deposit'):
            print(arguments)
            print(opts)
            print(value)
            print(args)
            deposit(args[0], float(value))
        elif opt in ("-w", "--withdraw"):
            withdraw(args[0], float(value))

if __name__ == "__main__":
    main(sys.argv[1:])     