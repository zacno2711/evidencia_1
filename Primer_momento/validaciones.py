import re
import random
from colors import color as c



def validar_nombre(name):
    if len(name)<3:
        print(c("red","Minimo 3 caracteres"))
        return True
    else :
        return False

def contiene_solo_numeros(cadena):
    patron = r'^\d+$'
    if re.match(patron, cadena):
        return True
    else:
        return False
    
def validar_usuario_phone(phone,users):
    bol = False
    for x in users:
        if phone == x["phone"]:
            bol = True
    if bol:
        return True
    else:
        return False

def validar_usuario_email(email,users):
    bol = False
    for x in users:
        if email == x["email"]:
            bol = True
    if bol:
        return True
    else:
        return False
      
def validar_telefono(phone, users):
    bol = False
    if contiene_solo_numeros(phone):
        if len(phone) < 10 :
            print(c("red","Telefono debe de tener al menos 10 digitos"))
            bol = False
        else:
            if not validar_usuario_phone(phone,users):
                bol = True
            else:
                print(c("red","Telefono registrado, intente con otro" ))
                bol = False
    else : 
        print(c("red","El telefono solo puede contener numeros"))
        bol = False

    if bol:
        return True
    else:
        return False

def validar_email(email, users):
    bol = False
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, email):
        if not validar_usuario_email(email, users):
            bol = True
        else:
            print(c("red","Email registrado"))
            bol = False
    else:
        print(c("red", "Email invalido")) 
        bol = False
    if bol:
        return True
    else:
        return False
    
def validar_password(psw):
    if len(psw) >= 5:
        patron = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,}$'
        if re.match(patron, psw):
            return True
        else:
            print(c("red","- Debe contener al menos una letra mayúscula o minúscula. \n- Debe contener al menos un dígito numérico.")) 
            return False
    else:
        print(c("red","- Debe contener al menos 5 caracteres"))
        return False

def find_user_email(email, users):
    for x in users:
        if email == x ["email"]:
            return x
        else:
            return None

def find_user_phone(phone, users):
    bol = False
    for x in users:
        if phone == x ["phone"]:
            bol = True
            break
        else:
            bol = False

    if bol:
        return x
    else:
        return None
    


def operation(a,b,c):
    if(c=="+"):
        return a + b
    elif(c=="-"):
        return a - b
    elif(c=="*"):
        return a * b

def capcha ():
   
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.choice(["-","+","*"])

    op = int(input(f"{a} {c} {b}: "))
    r = operation(a, b, c)
    if r == op: 
        return True
    else:
        return False

def validar_valor():
    try: 
        valor = input("Valor: ")
        if valor == "":
            print(c('red','valor vacio'))
            return False
        else:
            return int(valor)
    except ValueError:
        print(c('red',f'Valor solo acepta numeros \n'))
        return False

def validar_razon():
    razon = input("Razon: ")
    if razon != "":
        if len(razon) > 15:
            print(c('red','maximo 15 caracteres'))
        else:
            return False
    else:
        return False
    
userName = ""