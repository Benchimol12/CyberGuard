from usuario import Utilizadores as Ut

utilizador_teste = {"ricardo": "1234"} #Utilizador + codigo/palavra-passe

def menu_inicial():
    print("Selecione um dos menus abaixo:")
    print("1 - Iniciar sessão")
    print("2 - Criar Utilizador")
    menu = input("Introduza o numero do menu: ")

    if menu == "1":
        tipo_utilizador = Ut().iniciar_sessao()
        menus_em_sessao(tipo_utilizador)
    elif menu == "2":
        Ut.registo()

def menus_em_sessao(tipo_utilizador):

    if tipo_utilizador == "Administrador":
        print("Selecione um dos menus abaixo:")
        print("1 - Criar Utilizador")
        print("2 - Desbloquear Utilizador")
        print("3 - Eliminar Utilizador")
        print("4 - Logs")
        print("5 - Terminar sessão")
        menu = input("Introduza o numero do menu: ")
        if menu == "1":
            Ut.registo()
        elif menu == "2":
            Ut.desbloquear()
        elif menu == "3":
           Ut.eliminar()
        elif menu == "4":
           Ut.consultar_logs()
        elif menu == "5":
           menu_inicial()

    elif tipo_utilizador == "Utilizador":
        print("Selecione um dos menus abaixo:")
        print("1 - ")
        print("2 - Terminar sessão")
        menu = input("Introduza o numero do menu: ")
        
        if menu == "1":
            pass
        elif menu == "2":
            menu_inicial()

    else:
        print("Erro ao ler o tipo de utilizador.")
        menu_inicial()
            
#Inicializa o sistema de segurança e defineo o administrador
Ut().inicio_sistema()
while True:
    menu_inicial()