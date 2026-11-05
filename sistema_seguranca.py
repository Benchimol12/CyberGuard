lista_utilizadores_codigo = {"ricardo": "1234"}  # Utilizador + codigo/palavra-passe

class SistemaSeguranca:

    def autenticacao(self, utilizador, codigo):
        if utilizador in lista_utilizadores_codigo:
            if codigo == lista_utilizadores_codigo[utilizador]:
                return True
            else:
                return False
        else:
            return None