e = [0]

tea = ["+","-","*","/"]

def number():
    ea = input("Number")
    if type(int(ea)) is not int:
        print("error , try again")
        number()
    op = input("Operator")
    
    ea = int(ea)
    
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
        e[0] *= ea
    

while True:
    print(e[0])
    number()