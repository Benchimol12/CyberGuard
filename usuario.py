from sistema_seguranca import SistemaSeguranca as SS

class Utilizadores:

    def inicio_sistema(self):
        SS()

    def iniciar_sessao(self):
        ######Corrigir as tentativas tem de ser por utilizador
        utilizador = input("Nome de Utilizador: ")
        codigo = input("Palavra-passe: ")
        tentativas = 3
        while tentativas >= 1:
            if tentativas != 3:
                utilizador = input("Nome de Utilizador: ")
                codigo = input("Palavra-passe: ")
            if SS().autenticacao(utilizador, codigo)[0] == True:
                print(f"Bem Vindo {utilizador}!")
                if SS().autenticacao(utilizador, codigo)[1] == "Administrador":
                    return "Administrador"
                elif SS().autenticacao(utilizador, codigo)[1] == "Utilizador":
                    return "Utilizador"
                break
            
            else:
                tentativas -= 1
                print(f"Nome de utilizador ou palavra-passe errada! \n{tentativas} tentativas restantes.")

        if tentativas == 0:
            print(f"Conta {utilizador} bloqueada e só pode ser reativada pelo administrador.")
        elif tentativas <= 0:
            print("Erro ao ler os utilizadores.")

    #def registo(self):
     #  self.lista_utilizadores.append(str(self.utilizador))
     #   self.lista_utilizadores_codigo.insert(str(self.utilizador[str(self.codigo)]))