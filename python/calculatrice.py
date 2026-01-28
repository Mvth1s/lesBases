def addition(a: int, b:int):
    return a + b
    
def soustraction (a: int, b:int):
    return a - b

def multiplication (a:int, b:int):
    return a * b

def division (a:int, b:int):
    return a / b
    
print ("----------------test de ces fonctions simple----------------")
a = 2
b = 9

print ("Addition : "+ str(a) + " + "+ str(b) + " = " + str(addition(a,b)))
print ("Soustraction : "+ str(a) + " - "+ str(b) + " = " + str(soustraction(a,b)))
print ("Multiplication : "+ str(a) + " x "+ str(b) + " = " + str(multiplication(a,b)))
print ("Division : "+ str(a) + " / "+ str(b) + " = " + str(division(a,b)))