def add(a,b):
    print(f"The sum of {a} and {b} is: {a+b}")
def multiply(a,b):
    print(f"The product of {a} and {b} is: {a*b}")
def divide(a,b):
    print(f"The quotient of {a} and {b} is: {a/b}")
def sub(a,b):
    print(f"The remainder of {a} and {b} is: {a-b}")

def calc():
    choice= int(input("Enter your choice: \n1 for add \n2 for sub \n3 for multiply \n4 for divide\n"))
    a= int(input("Enter the number: ")) 
    b= int(input("Enter the number: "))
    if choice== 1:
        add(a=a,b=b)
    elif choice==2:
        sub(a=a,b=b)
    elif choice==3:
        multiply(a=a,b=b)
    elif choice==4:
        divide(a=a,b=b)
    else:
        print("Enter A Valid Choice.")
calculate= True
while calculate:
    calc()
    choose= int(input("Do you want to calculate more: \n1 for Yes\n2 for No"))
    if choose== 1:
        calc()
    else:
        break