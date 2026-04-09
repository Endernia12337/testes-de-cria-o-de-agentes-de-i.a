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
        print (f"fechando {target}")
        self.context["last_app"] = target
    def move_item (self,target_local_new: list):
        print (f"{target_local_new[0]} movido de {target_local_new[1]}, para {target_local_new[2]}")



    def execute_command(self,execute : dict) -> None:
        print(random.choice(self.greet))

        if len(execute) < 1: # se args estiver vazio ele retorna 
            print("ERRO: parametros nn estabelecidos")
            return
        
        for i in execute:
            print(self.commands[i], execute[i])
        

    def parser_input(self,cmd) -> list:
        cmd = [i.replace(",", "") for i in cmd if i not in self.ignore]
        command = []
        args = []


        for idx, i in enumerate(cmd):
            if i in self.commands: #* i é um comandos
                command.append(i)
                self.memory["last_command"] = i
                continue

            elif not command and self.memory["last_command"]:
                command.append(self.memory["last_command"])
                continue
            #* i é um conector
            elif i in self.conect:
                continue

            else: #* i é um app
                if  self.memory["last_command"]:
                    command.append(self.memory["last_command"])
                    args.append(i)
                    self.memory["last_app"] = i


        execute = dict(zip(command,args)) #! corrigir erro, so volta o ultimo comando e ultimo argumento -> possivel falha: ele roda o codigo e limpa a lista  de command e args
                                           #? testar coloco command e args no __init__ ou/e o execute
        print(execute)
        return execute
    

agent = Agent()


# user_input = input("oq vc gostaria de fazer? ")
user_input = "abrir o chrome e vscode e depois spotify"
cmd = user_input.lower().split()

# agent.execute_command(*agent.parser_input(cmd))
agent.parser_input(cmd)