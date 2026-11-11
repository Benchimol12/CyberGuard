from datetime import datetime as dt

segundos = dt().now().second

class SistemaSeguranca:
    #chamado uma unica vez quando incializa o sistema
    def __init__(self): 
        self.lista_utilizadores_codigo = {}
        self.admin = {"ricardo": "1234"}  # Utilizador + codigo/palavra-passe
        self.logs = ["Inicio do Sistema."]

    #dia-mes-ano hora:minuto:segundo
    def timestamp(self):
        return dt.now().strftime("%d-%m-%Y %H:%M:%S") 
    
    def autenticacao(self, utilizador, codigo):
        timestamp = self.timestamp()

        #Autenticação de utilizadores normais
        if utilizador in self.lista_utilizadores_codigo: 
            if codigo == self.lista_utilizadores_codigo[utilizador]:
                self.logs.append(f"{timestamp} - Utilizador '{utilizador}' iniciou sessão com sucesso.")
                return [True, "Utilizador"]
            else:
                self.logs.append(f"{timestamp} - Utilizador '{utilizador}' tentou iniciar sessão mas falhou.")
                return [False, "Utilizador"]

        #Autenticação de administradores
        elif utilizador in self.admin: 
            if codigo == self.admin[utilizador]:
                self.logs.append(f"{timestamp} - Administrador '{utilizador}' iniciou sessão com sucesso.")
                return [True, "Administrador"]
            else:
                self.logs.append(f"{timestamp} - Administrador '{utilizador}' tentou iniciar sessão mas falhou.")
                return [False, "Administrador"]
        
        #Quando o utilizador não existe
        else:
            self.logs.append(f"{timestamp} - Utilizador '{utilizador}' tentou iniciar sessão mas não existe.")
            return [None, None]