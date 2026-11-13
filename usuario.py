from sistema_seguranca import SistemaSeguranca as SS

class Utilizadores:

    def iniciar_sistema(self):
        #cria uma instancia da classe SistemaSeguranca e guarda na variavel sistema_seguranca, evitando erros ao chamar a classe SistemaSeguranca diretamente
        self.sistema_seguranca = SS() 

    #Iniciar sessão de utilizadores normais e administradores, atraves do menu inicial
    def iniciar_sessao(self):
        ######Corrigir as tentativas tem de ser por utilizador
        print("\n" + "*" * 25 + " Iniciar Sessão " + "*" * 25)
        utilizador = input("Nome de Utilizador: ")
        codigo = input("Palavra-passe: ")
        tentativas = 3
        while tentativas >= 1:
            if tentativas != 3:
                utilizador = input("Nome de Utilizador: ")
                codigo = input("Palavra-passe: ")

            #Autenticacao unica evitando erros ao chamar a classe SistemaSeguranca diretamente como criar logs duplos
            autenticacao = self.sistema_seguranca.autenticacao(utilizador, codigo)

            if autenticacao == [True, "Administrador"]:
                return utilizador, "Administrador"
            
            elif autenticacao == [True, "Utilizador"]:
                return utilizador, "Utilizador"
            
            else:
                tentativas -= 1
                log = f"\nNome de utilizador ou palavra-passe errada! \n{tentativas} tentativas restantes."
                print(log)
                self.criar_log(log)

        if tentativas == 0:
            log = f"\nConta {utilizador} bloqueada e só pode ser reativada pelo administrador."
            print(log)
            self.criar_log(log)
        elif tentativas <= 0:
            log = f"\nErro ao ler os utilizadores."
            print(log)
            self.criar_log(log)

    #Registo de utilizadores normais, atraves do menu inicial
    def registo_publico(self):
        print("\n" + "*" * 25 + " Registo de Utilizador " + "*" * 25)
        utilizador = input("Nome de Utilizador: ")
        codigo = input("Palavra-passe: ")
        if utilizador in self.sistema_seguranca.lista_utilizadores_codigo:
            print(f"\nUtilizador {utilizador} já existe.")
        else:
            self.sistema_seguranca.criar_utilizador_publico(utilizador, codigo)
            print(f"\nUtilizador {utilizador} criado com sucesso.")

    #Registo de utilizadores administradores, atraves do menu de administrador
    def registo_admin(self, admin=str):
            print("\n" + "*" * 25 + " Registo de Utilizador " + "*" * 25)
            utilizador = input("Nome de Utilizador: ")
            codigo = input("Palavra-passe: ")
            tipo_utilizador = input("É um utilizador Administrador? (s/n): ")

            #Verificar se o utilizador já existe na lista de utilizadores ou na lista de administradores
            if utilizador in self.sistema_seguranca.admin or utilizador in self.sistema_seguranca.lista_utilizadores_codigo:
                print(f"\nUtilizador {utilizador} já existe.")
                return

            if tipo_utilizador.lower() in ["s", "si", "sim", "y", "yes", "ye", "sm"]:
                self.sistema_seguranca.criar_admin(utilizador, codigo, admin)
                print(f"\nAdministrador {utilizador} criado com sucesso.")

            elif tipo_utilizador.lower() in ["n", "no", "não", "nao", "na", "nã", "nah"]:
                self.sistema_seguranca.criar_utilizador_privado(utilizador, codigo, admin)
                print(f"\nUtilizador {utilizador} criado com sucesso.")
                
    def eliminar_conta(self):
        print("\n" + "*" * 25 + " Eliminar Utilizador " + "*" * 25)
        eliminar_utilizador = input("Nome do Utilizador a ser eliminado: ")
        utilizador = input("Nome de um Administrador: ")
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

    def consultar_logs(self):
        print("\n" + "*" * 25 + " Logs do Sistema " + "*" * 25)
        for log in self.sistema_seguranca.logs:
            print("+ ", log)

    def criar_log(self, log):
        self.sistema_seguranca.logs.append(log)

    def ver_lista_utilizadores(self):
        print("\n" + "*" * 25 + " Lista de Utilizadores " + "*" * 25)
        print("Administradores:")
        for admin in self.sistema_seguranca.admin:
            print("+ ", admin, ": ", self.sistema_seguranca.lista_utilizadores_estado[admin])
        print("\nUtilizadores:")
        for utilizador in self.sistema_seguranca.lista_utilizadores_codigo:
            print("+ ", utilizador, ": ", self.sistema_seguranca.lista_utilizadores_estado[utilizador])
    
    #def desbloquear(self):