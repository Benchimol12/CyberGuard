from datetime import datetime as dt

class SistemaSeguranca:

    #chamado uma unica vez quando incializa o sistema
    def __init__(self): 
        self.lista_utilizadores_codigo = {}
        self.lista_utilizadores_estado = {"ricardo": "ativo"}
        self.admin = {"ricardo": "1234"}  # Utilizador + codigo/palavra-passe
        self.logs = [f"{self.timestamp()} - Inicio do Sistema."]

    #dia-mes-ano hora:minuto:segundo
    def timestamp(self):
        return dt.now().strftime("%d-%m-%Y %H:%M:%S") 

    #Cria um utilizador normal atraves do menu inicial, sem estar logado no sistema
    def criar_utilizador_publico(self, utilizador=str, codigo=str):
        self.lista_utilizadores_codigo[utilizador] = codigo
        self.lista_utilizadores_estado[utilizador] = "ativo"
        self.logs.append(f"{self.timestamp()} - nova conta utilizador '{utilizador}' criada no menu inicial .")

    #Cria um utilizador normal atraves do menu de administrador, estando logado no sistema
    def criar_utilizador_privado(self, criar_utilizador=str, codigo=str, utilizador=str):
            self.lista_utilizadores_codigo[criar_utilizador] = codigo
            self.lista_utilizadores_estado[criar_utilizador] = "ativo"
            self.logs.append(f"{self.timestamp()} -'{utilizador}' criou uma nova conta '{criar_utilizador}'.")
    
    #Criar um administrador atraves do menu de administrador, estando logado no sistema
    def criar_admin(self, criar_admin=str, codigo=str, utilizador=str):
        self.admin[criar_admin] = codigo
        self.lista_utilizadores_estado[criar_admin] = "ativo"
        self.logs.append(f"{self.timestamp()} -'{utilizador}' criou uma nova conta de Administrador '{criar_admin}'.")

    #Eliminar um utilizador normal atraves do menu de administrador, estando logado no sistema
    def eliminar_utilizador(self, utilizador=str, admin=str):
        try:
            del self.lista_utilizadores_codigo[utilizador]
        except ValueError:
            del self.admin[utilizador]
        self.logs.append(f"{self.timestamp()} -'{admin}' eliminou a conta de '{utilizador}'.")

    #Eliminar o estado de um utilizador normal atraves do menu de administrador, estando logado no sistema
    def eliminar_estado_utilizador(self, utilizador=str, admin=str):
        del self.lista_utilizadores_estado[utilizador]
        self.logs.append(f"{self.timestamp()} -'{admin}' eliminou o estado da conta de '{utilizador}'.")

    #Autenticação de utilizadores normais e administradores        
    def autenticacao(self, utilizador, codigo):
        timestamp = self.timestamp()

        #Autenticação de utilizadores normais
        if utilizador in self.lista_utilizadores_codigo: 
            if codigo == self.lista_utilizadores_codigo[utilizador] and self.lista_utilizadores_estado[utilizador] == "ativo":
                self.logs.append(f"{timestamp} - Utilizador '{utilizador}' iniciou sessão com sucesso.")
                return [True, "Utilizador"]

            elif codigo == self.lista_utilizadores_codigo[utilizador] and self.lista_utilizadores_estado[utilizador] == "bloqueado":
                self.logs.append(f"{timestamp} - Utilizador '{utilizador}' tentou iniciar sessão mas está bloqueado.")
                return [False, "Utilizador"]
            
            else:
                self.logs.append(f"{timestamp} - Utilizador '{utilizador}' tentou iniciar sessão mas falhou.")
                return [False, "Utilizador"]

        #Autenticação de administradores
        elif utilizador in self.admin: 
            if codigo == self.admin[utilizador]and self.lista_utilizadores_estado[utilizador] == "ativo":
                self.logs.append(f"{timestamp} - Administrador '{utilizador}' iniciou sessão com sucesso.")
                return [True, "Administrador"]
            
            elif codigo == self.admin[utilizador] and self.lista_utilizadores_estado[utilizador] == "bloqueado":
                self.logs.append(f"{timestamp} - Administrador '{utilizador}' tentou iniciar sessão mas está bloqueado.")
                return [False, "Administrador"]
            
            else:
                self.logs.append(f"{timestamp} - Administrador '{utilizador}' tentou iniciar sessão mas falhou.")
                return [False, "Administrador"]
        
        #Quando o utilizador não existe
        else:
            self.logs.append(f"{timestamp} - Utilizador '{utilizador}' tentou iniciar sessão mas não existe.")
            return [None, None]