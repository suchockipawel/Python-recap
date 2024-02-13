import sys

print(sys.argv[1:])
args = sys.argv[1:]
# m + n,m - n,m * n,m / n

n = int(args[0])
op = str(args[1])
m = int(args[2])

if op == "+":
    print("the result is ", n + m)
elif op == "-":
    print("the result is ", n - m)
elif op =="x":
    print("the result is ", n * m)
elif op =="/":
    try: 
       print("the result is ", n / m)
    except ZeroDivisionError:
        print('you cannot divide by zero') 
else:
    print("please enter a valid operator")