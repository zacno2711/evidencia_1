from colorama import  init,Fore, Style

def color(color,obj):
    try:
        if color == "green":
            return f"{Fore.LIGHTGREEN_EX}{obj}{Style.RESET_ALL}"
        elif color == "red":
            return f"{Fore.LIGHTRED_EX}{obj}{Style.RESET_ALL}"
        elif color == "yellow":
            return f"{Fore.LIGHTYELLOW_EX}{obj}{Style.RESET_ALL}"
        elif color == "cyan":
            return f"{Fore.LIGHTCYAN_EX}{obj}{Style.RESET_ALL}"
        elif color == "white":
            return f"{Fore.LIGHTWHITE_EX}{obj}{Style.RESET_ALL}"
    except ValueError as e:
        print (f"error de conversion = {e}")