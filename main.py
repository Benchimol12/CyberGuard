from usuario import Utilizadores as Ut

utilizador_teste = {"ricardo": "1234"} #Utilizador + codigo/palavra-passe

def menus():
    print("Selecione um dos menus abaixo:")
    print("1 - Iniciar sessão")
    print("2 - Criar Utilizador")
    menu = input("Introduza o numero do menu: ")

    if menu == "1":
        Ut().iniciar_sessao()
    elif menu == "2":
        Ut.registo()

def menus_em_sessao():
    print("Selecione um dos menus abaixo:")

menus()