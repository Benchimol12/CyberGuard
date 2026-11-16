from usuario import Utilizadores

#cria uma instancia da classe SistemaSeguranca e guarda na variavel sistema_seguranca, evitando erros ao chamar a classe SistemaSeguranca diretamente
Ut = Utilizadores()
exit = False
def menu_inicial():
    global exit
    print("\n" + "*" * 5 + "Bem Vindo ao Sistema de Segurança CyberGuard!" + "*" * 5)
    print("Selecione um dos menus abaixo:")
    print("1 - Iniciar sessão")
    print("2 - Criar Utilizador")
    print("3 - Terminar Programa")
    menu = input("Introduza o numero do menu: ")

    if menu == "1":
        utilizador, tipo_utilizador = Ut.iniciar_sessao()
        if utilizador != "None":
            menus_em_sessao(utilizador, tipo_utilizador)
    elif menu == "2":
        Ut.registo_publico()
    elif menu == "3":
        print("\nPrograma terminado.")
        exit = True

def menus_em_sessao(utilizador, tipo_utilizador):
    while True:
        print("\n" + "*" * 25 + f"Sessão iniciada como {utilizador}. " + "*" * 25)
        if tipo_utilizador == "Administrador":
            print("Selecione um dos menus abaixo:")
            print("1 - Criar Utilizador")
            print("2 - Ver lista de utilizadores")
            print("3 - Desbloquear Utilizador")
            print("4 - Eliminar Utilizador")
            print("5 - Logs")
            print("6 - Terminar sessão")
            menu = input("Introduza o numero do menu: ")
            if menu == "1":
                Ut.registo_admin(utilizador)
            elif menu == "2":
                Ut.ver_lista_utilizadores(utilizador)
            elif menu == "3":
                Ut.desbloquear(utilizador)
            elif menu == "4":
                Ut.eliminar_conta(utilizador)
            elif menu == "5":
                Ut.consultar_logs(utilizador)
            elif menu == "6":
                log = f"{Ut.sistema_seguranca.timestamp()} - Administrador '{utilizador}' terminou sessão."
                Ut.criar_log(log)
                break

        elif tipo_utilizador == "Utilizador":
            print("Selecione um dos menus abaixo:")
            print("1 - Testar sessão (A ser feito)")
            print("2 - Criar Utilizador")
            print("3 - Consultar logs ")
            print("4 - Terminar sessão")
            menu = input("Introduza o numero do menu: ")
            
            if menu == "1":
                log = f"{Ut.sistema_seguranca.timestamp()} - Utilizador '{utilizador}' testou a sessão."
                Ut.criar_log(log)
                pass
            elif menu == "2":
                Ut.registo_publico(utilizador)
            elif menu == "3":
                Ut.consultar_logs(utilizador)
            elif menu == "4":
                log = f"{Ut.sistema_seguranca.timestamp()} - Utilizador '{utilizador}' terminou sessão."
                Ut.criar_log(log)
                break

        else:
            log = f"\nErro ao ler o tipo de utilizador que iniciou sessão."
            print(log)
            Ut.criar_log(log)
            break
            
#Inicializa o sistema de segurança e define o o administrador
Ut.iniciar_sistema()
while not exit:
    menu_inicial()
