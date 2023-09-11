from registro import users
import validaciones as va
import os
from colors import color as c

def Login ():
    os.system('cls')

    print(c("cyan","INICIO DE SESION \n"))
    print(c("yellow","Seleccione con que desea iniciar sesion\n"))
    op = input(f"{c ('yellow','1.')} Email\n{c ('yellow','2.')} Telefono \n{c ('yellow','Other key.')} Salir  \n--> ")

    if op == "2":
        os.system('cls')
        phone = input("Telefono: ")
        user = va.find_user_phone(phone,users)
        if user != None:
            bol = 0
            while bol < 3:
                psw = input("Contraseña: ")
                if psw != user["psw"]:
                    bol += 1
                    print(c("red","\nContraseña incorrecta\n"))
                else:
                    print(c("yellow","\nRESUELVE EL CAPCHA PARA CONTINUAR\n"))
                    x = 0
                    while x < 3:
                        capcha = va.capcha()
                        if capcha:
                            va.userName = user["name"]
                            from menus import Menu_second
                            Menu_second()
                            
                        else:
                            x += 1
        else: 
            print(c("red",f"\nTelefono ({phone}) no esta registrado\n"))

    elif op == "1":
        os.system('cls')
        Email = input("Email: ")
        user = va.find_user_email(Email,users)
        if user != None:
            bol = 0
            while bol < 3:
                psw =input("Contraseña: ")
                if psw != user["psw"]:
                    bol += 1
                    print(c("red","\nContraseña incorrecta\n"))
                else:
                    print(c("yellow","\nRESUELVE EL CAPCHA PARA CONTINUAR\n"))
                    x = 0
                    while x < 3:
                        capcha = va.capcha()
                        if capcha:
                            va.userName = user["name"]
                            from menus import Menu_second
                            Menu_second()
                            
                        else:
                            x += 1
        else: 
            print(c("red",f"\nEmail ({Email}) no esta registrado\n"))


    else: 
        import menus
        menus.Menu_home()

Login()