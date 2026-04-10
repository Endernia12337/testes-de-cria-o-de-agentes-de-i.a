import random
from windows_manage import WindowsManager

#TODO fazer uma classe onde os metodos são  todos os possiveis erros que nn são nativos do python, por execute_commandmplo que o agente não conseguiu encontrar a função escolhida pelo usuario. e implementar-la onde precisar
class Agent:  
    def __init__(self):
        self.Wm = WindowsManager() #criando o objeto que modifica o windows

        # criando condicionais para separação correta da frase
        self.greet = ["ok senhor", "com certeza"]
        self.conect = ("e", "depois", "em seguida")
        self.ignore = ("o", "a")

        #criando memoria e comandos
        self.memory = {
            "last_command" : None,
            "last_app" : None,
        }
        self.context = {
            "ele" : self.memory["last_app"]

        }
        self.commands = {
        "abri" : self.open_app,
        "abrir" : self.open_app,
        "iniciar" : self.open_app,
        "fechar" : self.close_app,
        "mover" : self.move_item,
        }

    def open_app (self,target):
        self.Wm.open_window(target)
        self.memory["last_app"] = target
    def close_app (self,target):
        # self.Wm.close_window(target)
        print (f"fechando {target}")
    def move_item (self,target, local, new):
        print (f"{target} movido de {local}, para {new}")


    def execute_command(self,execute) -> None:
        print(random.choice(self.greet))

        if len(execute) < 1 or execute == None: # se args estiver vazio ele retorna 
            print("ERRO: parametros nn estabelecidos")
            return
        
        for i in execute: # exemple -> [('abrir', 'chrome'),('fechar', 'spotify')] -> i == ('abrir', 'chrome')
            self.commands[i[0]](i[1]) #exemple -> self.commands['abrir']('chrome') -> open_app(target='chrome')
        

    def parser_input(self,cmd) -> list:
        corrent_command = None
        cmd = [i.replace(",", "") for i in cmd if i not in self.ignore]
        list_commands = []

        for i in cmd:
            if i in self.commands: #* i é um comandos
                corrent_command = i
                continue
            #* i é um conector
            elif i in self.conect:
                continue

            else: #* i é um app
                if corrent_command:
                    list_commands.append((corrent_command, i))
                else:
                    continue
                    


        return  list_commands
    

agent = Agent()


user_input = input("oq vc gostaria de fazer? ")
cmd = user_input.lower().split()

agent.execute_command(agent.parser_input(cmd))
# print(agent.parser_input(cmd))