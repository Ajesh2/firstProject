e = 0

tea = ["+","-","*","/"]

def number():
    ea = input("Number")
    global e
    try: 
        if type(int(ea)) is int:
            op = input("Operator")
            
            ea = int(ea)
            
            if op not in tea:
                print("error , try again")
                number()
            if op == "+":
                e += ea
            if op == "-":
                e -= ea
            if op == "/":
                e /= ea
            if op == "*":
                e *= ea
    except:
        print("error , try again")
        number()
    

while True:
    print(e)
    number()
