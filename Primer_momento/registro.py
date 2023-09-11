import validaciones as va
import os
from colors import color as c


users = [{"email":"juan@gmail.com","name":"pablo","phone":"1234536456","psw":"Juan123"},
         {"email":"kelly@gmail.com","name":"kelly","phone":"3023456655","psw":"KellY123"},
         {"email":"lucas@hotmail.com","name":"lucas","phone":"23433332233","psw":"lUcAs123"}]

def Registro():
    os.system('cls')
    x = False
    while not x:
        count = 0
        while count < 3:
            print(c("cyan","REGISTRO DE USUARIO\n"))
            name = input("Nombre :")
            if va.validar_nombre(name):
                count+=1
            else:
                count = 0
                break

        while count < 3:
            phone =  input("Telefono :")
            if va.validar_telefono(phone,users):
                count = 0
                break
            else:
                count+=1 
                

        while count < 3:
            email =  input("Email :")
            if va.validar_email(email, users):
                count = 0
                break
            else:
                count +=1
        
        while count < 3: 
            psw = input("Contraseña: ")
            if va.validar_password(psw):
                user = {"email":email,"name":name,"phone":phone,"psw":psw}
                users.append(user)
                print(c("green","USUARIO CREADO"))
                print("\n")
                import menus
                menus.Menu_home()
            else:
                count += 1

        
        if count == 3:
            print(c("red","REGISTRO DE USUARIO CANCELADA"))
            import menus
            menus.Menu_home()
