import random
import os
from colors import color as c
import validaciones as va

def Game():
    os.system('cls')
    print(f"\nUSER ----> {c('green',f'{va.userName}')}\n")
    print(c("cyan","""
███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░  ███╗░░░███╗░█████╗░██╗░░░██╗░█████╗░██████╗░
████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗  ████╗░████║██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║  ██╔████╔██║███████║░╚████╔╝░██║░░██║██████╔╝
██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║  ██║╚██╔╝██║██╔══██║░░╚██╔╝░░██║░░██║██╔══██╗
██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝  ██║░╚═╝░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝"""))

    print("""
                    INSTRUCCIONES 

    - Ganas puntos si el número aleatorio es distinto de 0.
    - Pierdes vidas si el número es 0.
    - El juego continúa hasta que te quedes sin vidas.
    - Decide si quieres volver a jugar (Y/N) al final.
    - Disfruta del juego en consola.
    """)

    op1 = input(c("yellow","PRESS FOR START"))
    if op1 != None:
        os.system('cls')
        bol = False
        while not bol:
            vidas = 5
            puntos = 0


            while vidas != 0:
                num = random.randint(0,9)

                if num == 0:
                    vidas -= 1
                    print(c('red',f'\n te quedan {vidas} vidas \n'))
                else: 
                    puntos +=1
                    print(c('green',f'puntos {puntos}'))
                
            op = input("Deseas volver a jugar Y/N: ")
            if op.lower() == "n":
                from menus import Menu_second
                Menu_second()
                
            else:
                os.system('cls')
                pass


