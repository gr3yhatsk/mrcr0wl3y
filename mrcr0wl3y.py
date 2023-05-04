# coded by: gr3yhat

# < ----------------- Black Dragon Hacker Team Brazil ---------------------->

#calling them

import requests as r
import os



def banner():
    print("           Welcome to the mrcr0wl3y admin page founder!  ::  Bem vindo ao localizador de paginas administrativas mrcr0wl3y\n\n")
    print("                                < ----------------- Black Dragon Hacker Team Brazil ----------------- >\n")
    print("                                         Somos aqueles que tudo veem, mas não podem ser vistos!\n\n")
    print("                                            Coded by: gr3yhat || Programado por: gr3yhat\n\n\n")

    let_the_game_begin()


def let_the_game_begin():
    pages_baby = open('admin-pages.txt', 'r')

    site = input("Type in the target :: Digite o site (ex:https://hackme.com)>")

    for page in pages_baby:
        print(site + "/" + page.strip())
        raw_response = r.get(site + "/" + page.strip())

        #lets filter the responses

        if raw_response.status_code == 200:
            print("Found Admin page! " + site + "/" + page)
            exit()

        else:
            if os.name == 'nt':  # windows
                os.system('cls')
                pass

            else:  # linux
                os.system('clear')
                pass



if __name__ == "__main__":
    #checking which os is running
    if os.name == 'nt': #windows
        os.system('cls')

    else: #linux
        os.system('clear')

    banner()
