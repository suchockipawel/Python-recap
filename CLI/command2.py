import sys
import os
args = sys.argv[1:]
print(args)

def help():
    print("this is some description to the code")
    
def create_file():
    name = input("give file name")
    os.system(f"touch {name}.txt")
    
def write():
    with open("file.txt","a") as f:
        f.write("hellooooooo\n")
        
def create_table(table_name):
    print(f"the table {table_name} was created")
def delete():
    os.system("rm file.txt")
    
if "help" in args or "h" in args:
    help()
if  "makefile" in args or "mkf" in args:
    create_file()
if "write" in args:
    write()
if "createtable" in args:
    create_table("some cool table")
if "delete" in args:
    delete()
    print("file deleted successfully")