from tabulate import tabulate
from colors import color as c
import validaciones as va
import os

def Finanzas():
    os.system('cls')
    print(f"\nUSER ----> {c('green',f'{va.userName}')}\n")
    
    ingresos = []
    egresos = []
    historial = []
    header = ["TIPO","RAZON","VALOR"]
    print (c('cyan','CONTABILIDAD'))
    y=False

    while not y:
        data_ingresos = []
        data_egresos = []
        data_historial = []

        print("\n")
        op = input(f"{c ('yellow','1.')} Ingresos \n{c ('yellow','2.')} Egresos \n{c ('yellow','3.')} Historicos \n\n{c ('yellow','Other key.')} Salir \n--> ")
        print("\n")

        if op == "1":
            os.system('cls')
            x=False

            while not x:
                n = True
                k = True
                while n:
                    print(c('green','AGREGAR INGRESO'))
                    print("\n")
                    valor = va.validar_valor()
                    if valor:
                        n = False
                
                while k:
                    razon = input("Razon: ")
                    print("\n")
                    if razon != "":
                        if len(razon) > 15:
                            print(c('red','maximo 15 caracteres'))
                            print("\n")
                        else:
                            k=False
                    else:
                        k=False

                ingreso = {"tipo":"ingreso","razon": razon ,"valor": valor }
                ingresos.append(ingreso)
                historial.append(ingreso)
                op=input("continiuar  Y/N : ")
                print("\n")

                if op.lower() == "y":
                    x=False

                else:
                    os.system('cls')
                    x=True

        elif op == "2":
            os.system('cls')
            x=False

            while not x:
                n = True
                k = True
                while n:
                    print(c('red','AGREGAR EGRESO'))
                    print("\n")
                    valor = va.validar_valor()*-1
                    if valor:
                        n = False
                while k:
                    razon = input("Razon: ")
                    print("\n")
                    if razon != "":
                        if len(razon) > 15:
                            print(c('red','maximo 15 caracteres'))
                            print("\n")
                        else:
                            k=False
                    else:
                        k=False

                egreso = {"tipo":"egreso","razon":razon ,"valor":valor }
                egresos.append(egreso)
                historial.append(egreso)
                
                op=input("continiuar  Y/N : ")
                print("\n")

                if op.lower() == "y":
                    continue

                else:
                    os.system('cls')
                    x=True

        elif op == "3":
            os.system('cls')
            t = False
            while not t:

                print("_"*120)
                print(c("cyan","HISTORICOS"))
                print("\n")
                op2 = input(F"{c ('yellow','1.')} Historial Ingresos \n{c ('yellow','2.')} Historial Egresos \n{c ('yellow','3.')} Historial Completo \n{c ('yellow','Other key.')} Atras \n-->  ")
                print("\n")
                
                if op2 == "1":
                    os.system('cls')
                    if not len(ingresos) == 0:
                        total = 0
                        
                        for x in ingresos:  
                            data = []

                            for i in x.values():
                                data.append(i)

                            data_ingresos.append(data)
                            valor_x = x['valor']
                            total += valor_x
                        print(c('green','HISTORICO DE INGRESOS'))
                        print("\n")
                        table_ingresos = tabulate(data_ingresos,header,tablefmt="grid")
                        print(table_ingresos) 
                        print("\n")
                        print(c('green','TOTAL INGRESOS = $'f"{'{:,}'.format(total)}"))
                        print("\n")
                        print("_"*120)

                    else:
                        print(c('yellow','no hay historico de ingresos'))
                        print("\n")

                elif op2 == "2":
                    os.system('cls')
                    if not len(egresos) == 0:
                        total = 0

                        for x in egresos:
                            data = []

                            for i in x.values():
                                data.append(i)

                            data_egresos.append(data)
                            valor_x = x['valor']
                            total += valor_x

                        print(c('red','HISTORICO DE EGRESOS'))
                        print("\n")
                        table_engresos = tabulate(data_egresos,header,tablefmt="grid")
                        print(table_engresos)
                        print("\n")
                        print(c('red','TOTAL EGRESOS = $'f"{'{:,}'.format(total)}"))
                        print("\n")
                        print("_"*120)

                    else:
                        print(c('yellow','no hay historico de egresos'))
                        print("\n")
                        print("_"*120)

                elif op2 == "3":
                    os.system('cls')
                    if not len(historial) == 0:
                        valance = 0
                        for x in historial:
                            data = []
                            valance += x["valor"]

                            for i in x.values():
                                if type(i) == int:
                                    data.append('{:,}'.format(i))
                                else: 
                                    data.append(i)

                            data_historial.append(data)

                        table_historial = tabulate(data_historial,header,tablefmt="grid")
                        print(table_historial)
                        print("\n")
                        if valance <= 0 :
                            print(c('red','VALANCE DE HISTORIAL : $'f"{'{:,}'.format(valance)}"))
                        else:
                            print(c('green','VALANCE DE HISTORIAL : $'f"{'{:,}'.format(valance)}"))
                        print("\n")
                        print("_"*120)

                    else:
                        print(c('yellow','no hay registros de ingresos ni de egresos'))
                        print("\n")
                        print("_"*120)
                else:
                    t=True
                    os.system('cls')
        
        else :
            os.system('cls')
            import menus
            menus.Menu_second()

    