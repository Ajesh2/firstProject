import math
inp = ""
more = True
def toList(t):
    inp += str(t)
operations = ["+","-","*","/"]
print("For addition type \'+', for subtraction type \'-', for mulitplication type \'*', for division type \'/'")
print("type \"done\" when done")
while more:
    a = input("number")
    if type(a) == int:
        toList(a)
        b = input("operation")
        if b in operations:
            toList(b)
        else:
            print("invalid operation")


    else:
        print("invalid number")
    
    

