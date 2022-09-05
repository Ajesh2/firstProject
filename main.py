e = [0]

tea = ["+","-","*","/"]

def number():
    ea = input("Number")
    if type(int(ea)) is not int:
        print("error , try again")
        number()

    ea = int(ea)
    op = input("Operator")
    if op not in tea:
        print("error , try again")
        number()
    if op == "+":
        e[0] += ea
    if op == "-":
        e[0] -= ea
    if op == "/":
        e[0] /= ea
    if op == "*":
        e[0] += ea
    

while True:
    number()
    print(e)
    
