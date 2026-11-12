from sistema_seguranca import SistemaSeguranca as SS

class Utilizadores:

    def iniciar_sistema(self):
        #cria uma instancia da classe SistemaSeguranca e guarda na variavel sistema_seguranca, evitando erros ao chamar a classe SistemaSeguranca diretamente
        self.sistema_seguranca = SS() 

    def iniciar_sessao(self):
        ######Corrigir as tentativas tem de ser por utilizador
        utilizador = input("Nome de Utilizador: ")
        codigo = input("Palavra-passe: ")
        tentativas = 3
        while tentativas >= 1:
            if tentativas != 3:
                utilizador = input("Nome de Utilizador: ")
                codigo = input("Palavra-passe: ")
            if self.sistema_seguranca.autenticacao(utilizador, codigo)[0] == True:
                print(f"Bem Vindo {utilizador}!")
                if self.sistema_seguranca.autenticacao(utilizador, codigo)[1] == "Administrador":
                    return "Administrador"
                elif self.sistema_seguranca.autenticacao(utilizador, codigo)[1] == "Utilizador":
                    return "Utilizador"
                break
            
            else:
                tentativas -= 1
                print(f"Nome de utilizador ou palavra-passe errada! \n{tentativas} tentativas restantes.")

        if tentativas == 0:
            print(f"Conta {utilizador} bloqueada e só pode ser reativada pelo administrador.")
        elif tentativas <= 0:
            print("Erro ao ler os utilizadores.")

    def registo(self):
        utilizador = input("Nome de Utilizador: ")
        codigo = input("Palavra-passe: ")
        if utilizador in self.sistema_seguranca.lista_utilizadores_codigo:
            print(f"Utilizador {utilizador} já existe.")
        else:
            self.sistema_seguranca.criar_utilizador(utilizador, codigo)
            print(f"Utilizador {utilizador} criado com sucesso.")
            print(self.sistema_seguranca.lista_utilizadores_codigo)

    def consultar_logs(self):
        for log in self.sistema_seguranca.logs:
            print(log)