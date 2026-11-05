from sistema_seguranca import SistemaSeguranca as SS

class Utilizadores:

    def iniciar_sessao(self):
        ######Corrigir as tentativas tem de ser por utilizador
        tentativas = 3
        while tentativas >= 1:
            utilizador = input("Nome de Utilizador: ")
            codigo = input("Palavra-passe: ")
            if SS().autenticacao(utilizador, codigo):
                print(f"Bem Vindo {utilizador}!")
                break
            else:
                tentativas -= 1
                print(f"Nome de utilizador ou palavra-passe errada! \n{tentativas} tentativas restantes.")

        if tentativas == 0:
            print("Conta Bloqueada e só pode ser reativada pelo administrador.")
        elif tentativas <= 0:
            print("Erro ao ler os utilizadores.")
        return None

    #def registo(self):
     #  self.lista_utilizadores.append(str(self.utilizador))
     #   self.lista_utilizadores_codigo.insert(str(self.utilizador[str(self.codigo)]))