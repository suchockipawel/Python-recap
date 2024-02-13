import sys 

arguments = sys.argv[1:]

print(arguments)



def say_hello():
    print("Hello people")
    
if "hello" in arguments or "h" in arguments:
    say_hello()