from tabulate import tabulate
import os 
from colors import color as c
import validaciones as va

def Simulador_credito():
    os.system('cls')
    print(f"\nUSER ----> {c('green',f'{va.userName}')}\n")

    bol = False
    while not bol:
        print(c("cyan","SIMULADOR DE CREDITO \n"))
        Vcompra = int(input("valor de la compra: "))
        cuotas = int(input("en cuantas cuotas va a pagar: "))
        Vcuota = Vcompra/cuotas
        print (f"valor cuota {Vcuota}")
        count = 0
        cupo = 0
        saldo = Vcompra

        headers = ["N cuota", "Saldo", "Cupo"]
        fulldata= []

        while count < cuotas :
            cupo += Vcuota
            saldo -= Vcuota

            data= [count+1,int(saldo),int(cupo)]
            fulldata.append(data)
            count+=1
        
        os.system('cls')

        table = tabulate(fulldata, headers=headers, tablefmt="grid")
        print(table)

        op = input("\n Desea simular otro credito Y/N: ")
        if op.lower()=="n":
            os.system('cls')
            from menus import Menu_second
            Menu_second()
        else:
            os.system('cls')
            pass  





    



    


