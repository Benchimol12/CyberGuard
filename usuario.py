from sistema_seguranca import SistemaSeguranca as SS

class Utilizadores:

    def iniciar_sistema(self):
        #cria uma instancia da classe SistemaSeguranca e guarda na variavel sistema_seguranca, evitando erros ao chamar a classe SistemaSeguranca diretamente
        self.sistema_seguranca = SS()
        self.controle = {}

    #Iniciar sessão de utilizadores normais e administradores, atraves do menu inicial
    def iniciar_sessao(self):
        ######Corrigir as tentativas tem de ser por utilizador
        print("\n" + "*" * 25 + " Iniciar Sessão " + "*" * 25)
        utilizador = input("Nome de Utilizador: ")
        tentativas = 0
        while True:
            if utilizador not in self.sistema_seguranca.lista_utilizadores_codigo and utilizador not in self.sistema_seguranca.admin:
                log = f"{self.sistema_seguranca.timestamp()} - Utilizador '{utilizador}' tentou entrar com uma conta que não existe!"
                print("Conta não existe!")
                self.criar_log(log)
                return "None", "None"

            else:

                #Para não pedir o utilizador outra vez na 1ª entrada
                if tentativas > 0:
                    utilizador = input("Nome de Utilizador: ")

                if self.sistema_seguranca.lista_utilizadores_estado[utilizador] == "bloqueado":
                    log = f"{self.sistema_seguranca.timestamp()} - Utilizador '{utilizador}' tentou entrar mas está bloqueado!"
                    print("Conta bloqueada! Só pode ser desbloqueada por um administrador.")
                    self.criar_log(log)
                    return "None", "None"

                #Caso o "controle" esteja vazio ou o utilizador não esteja no "controle", pede a palavra-passe e adiciona o utilizador ao "controle" com valor 0
                if self.controle == {} or utilizador not in self.controle:
                    codigo = input("Palavra-passe: ")
                    self.controle[utilizador] = 0

                #Caso o "controle" do utilizador esteja entre 0 e 3, pede a palavra-passe e incrementa o valor do "controle" em 1
                elif self.controle[utilizador] < 3 and self.controle[utilizador] >= 0:
                    codigo = input("Palavra-passe: ")

                #Autenticacao unica evitando erros ao chamar a classe SistemaSeguranca diretamente como criar logs duplos
                autenticacao = self.sistema_seguranca.autenticacao(utilizador, codigo)

                if self.controle[utilizador] < 3:
                    if autenticacao == [True, "Administrador"]:
                        self.controle[utilizador] = 0
                        return utilizador, "Administrador"

                    elif autenticacao == [True, "Utilizador"]:
                        self.controle[utilizador] = 0
                        return utilizador, "Utilizador"

                    else:
                        self.controle[utilizador] += 1
                        if self.controle[utilizador] >= 3:
                            text = f"Conta {utilizador} bloqueada e só pode ser reativada pelo administrador.\n"
                            log = f"{self.sistema_seguranca.timestamp()} - {text}"
                            self.sistema_seguranca.bloquear_utilizador(utilizador)
                            print(text)
                            self.criar_log(log)
                            return "None", "None"
                        else:
                            text = f"Nome de utilizador ou palavra-passe errada! \n{3 - self.controle[utilizador]} tentativas restantes.\n"
                            log = f"{self.sistema_seguranca.timestamp()} - Nome de utilizador '{utilizador}' ou palavra-passe errada!"
                            print(text)
                            self.criar_log(log)
                    tentativas += 1

    #Registo de utilizadores normais, atraves do menu inicial com validação de utilizadores existentes e impede que utilizadores com o nome ou codigo vazios sejam criados
    def registo_publico(self, user:str = "Publico"):
        print("\n" + "*" * 25 + " Registo de Utilizador " + "*" * 25)
        utilizador = input("Nome de Utilizador: ")
        while utilizador == "":
            utilizador = input("Nome de Utilizador: ")
        if utilizador in self.sistema_seguranca.lista_utilizadores_codigo or utilizador in self.sistema_seguranca.admin:
            print(f"\nUtilizador {utilizador} já existe.")
        else:
            codigo = input("Palavra-passe: ")
            while codigo == "":
                codigo = input("Palavra-passe: ")
            self.sistema_seguranca.criar_utilizador_publico(utilizador, codigo, user)
            print(f"\nUtilizador {utilizador} criado com sucesso.")

    #Registo de utilizadores administradores, atraves do menu de administrador
    def registo_admin(self, admin=str):
            print("\n" + "*" * 25 + " Registo de Utilizador " + "*" * 25)
            utilizador = input("Nome de Utilizador: ")
            while utilizador == "":
                utilizador = input("Nome de Utilizador: ")

            #Verificar se o utilizador já existe na lista de utilizadores ou na lista de administradores
            if utilizador in self.sistema_seguranca.admin or utilizador in self.sistema_seguranca.lista_utilizadores_codigo:
                print(f"\nUtilizador {utilizador} já existe.")
                return

            codigo = input("Palavra-passe: ")
            while codigo == "":
                codigo = input("Palavra-passe: ")
            tipo_utilizador = input("É um utilizador Administrador? (s/n): ")

            if tipo_utilizador.lower() in ["s", "si", "sim", "y", "yes", "ye", "sm"]:
                self.sistema_seguranca.criar_admin(utilizador, codigo, admin)
                print(f"\nAdministrador {utilizador} criado com sucesso.")

            elif tipo_utilizador.lower() in ["n", "no", "não", "nao", "na", "nã", "nah"]:
                self.sistema_seguranca.criar_utilizador_privado(utilizador, codigo, admin)
                print(f"\nUtilizador {utilizador} criado com sucesso.")
                
    def eliminar_conta(self, admin):
        print("\n" + "*" * 25 + " Eliminar Utilizador " + "*" * 25)
        eliminar_utilizador = input("Nome do Utilizador a ser eliminado: ")
        utilizador = admin
        codigo = input("Palavra-passe do Administrador: ")

        #Verifica se o utilizador a ser eliminado existe na lista de utilizadores ou na lista de administradores
        if eliminar_utilizador not in self.sistema_seguranca.lista_utilizadores_codigo and eliminar_utilizador not in self.sistema_seguranca.admin:
            print(f"\nUtilizador {eliminar_utilizador} não existe.")
            self.sistema_seguranca.logs.append(f"{self.sistema_seguranca.timestamp()} -'{utilizador}' tentou eliminar a conta '{eliminar_utilizador}' mas não existe.")
            return

        #Faz a autenticação do administrador antes de eliminar o utilizador
        if self.sistema_seguranca.autenticacao(utilizador, codigo) == [True, "Administrador"]:
            #Eliminia o utilizador e o estado
            self.sistema_seguranca.eliminar_utilizador(eliminar_utilizador, utilizador)
            self.sistema_seguranca.eliminar_estado_utilizador(eliminar_utilizador, utilizador)
            print(f"\nUtilizador {eliminar_utilizador} eliminado com sucesso.")
        
        else:
            print(f"\nUtilizador ou palavra-passe administrativa errada.")
            log = f"{self.sistema_seguranca.timestamp()} -'{utilizador}' tentou eliminar a conta '{eliminar_utilizador}' mas errou o utilizador ou palavra-passe de administrador."
            self.criar_log(log)

    def consultar_logs(self, user=str):
        if user not in self.sistema_seguranca.admin:
            print(f"\nUtilizador {user} não tem permissões para consultar os logs.")
            log = f"{self.sistema_seguranca.timestamp()} - Utilizador '{user}' tentou consultar os logs mas não tem permissões."
            self.criar_log(log)
            return
        print("\n" + "*" * 25 + " Logs do Sistema " + "*" * 25)
        for log in self.sistema_seguranca.logs:
            print("+ ", log)

    def criar_log(self, log):
        self.sistema_seguranca.logs.append(log)

    def ver_lista_utilizadores(self, user=str):
        print("\n" + "*" * 25 + " Lista de Utilizadores " + "*" * 25)
        print("Administradores:")
        for admin in self.sistema_seguranca.admin:
            print("+ ", admin, ": ", self.sistema_seguranca.lista_utilizadores_estado[admin])
        print("\nUtilizadores:")
        for utilizador in self.sistema_seguranca.lista_utilizadores_codigo:
            print("+ ", utilizador, ": ", self.sistema_seguranca.lista_utilizadores_estado[utilizador])
        self.criar_log(f"{self.sistema_seguranca.timestamp()} - Utilizador '{user}' consultou a lista de Utilizadores")
    
    def desbloquear(self, admin):
        utilizador = input("Nome de Utilizador a desbloquear: ")
        if utilizador not in self.sistema_seguranca.lista_utilizadores_estado:
            log = f"{self.sistema_seguranca.timestamp()} - Conta '{utilizador}' não existe."

        elif self.sistema_seguranca.lista_utilizadores_estado[utilizador] == "ativo":
            log = f"{self.sistema_seguranca.timestamp()} - Conta '{utilizador}' está ativa."

        else:
            codigo = input("Palavra-passe do Administrador: ")
            if self.sistema_seguranca.autenticacao(admin, codigo) == [True, "Administrador"]:
                print(f"\nConta {utilizador} desbloqueada com sucesso.")
                log = f"{self.sistema_seguranca.timestamp()} - Conta {utilizador} desbloqueada pelo administrador '{admin}'."
                self.sistema_seguranca.lista_utilizadores_estado[utilizador] = "ativo"
                self.controle[utilizador] = 0
            else:
                print(f"\nUtilizador ou palavra-passe administrativa errada.")
                log = f"{self.sistema_seguranca.timestamp()} - Conta '{utilizador}' não desbloqueada, utilizador ou palavra-passe administrativa errada."
        self.criar_log(log)
        print(log)