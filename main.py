import random
from windows_manage import WindowsManager

#TODO fazer uma classe onde os metodos são  todos os possiveis erros que nn são nativos do python, por exemplo que o agente não conseguiu encontrar a função escolhida pelo usuario. e implementar-la onde precisar

class agent:
    def __init__(self):
        self.context = {
            "ultimo_app" : None,
        }

        self.Wm = WindowsManager() #criando o objeto que modifica o windows

        # criando condicionais para separação correta da frase
        self.comprimentar = ["ok senhor", "com certeza"]
        self.conectores = ("e", "depois", "em seguida")
        self.ignorar = ("o", "a")

        #criando memoria e comandos
        self.memory = {
            "lass_command" : None,
            "lass_app" : None,
        }
        self.comandos = {
        "abri" : self.abrir,
        "abrir" : self.abrir,
        "iniciar" : self.abrir,
        "fechar" : self.fechar,
        "mover" : self.mover,
        }

    def abrir (self,target:list):
        self.Wm.open_window(program=target)
    def fechar (self,target):
        print (f"fechando {target}")
        self.context["ultimo_app"] = target
    def mover (self,target_local_new: list):
        print (f"{target_local_new[0]} movido de {target_local_new[1]}, para {target_local_new[2]}")

    def exe(self,command : str, args : list[str]) -> None:
        print(random.choice(self.comprimentar))

        if len(args) < 1: # se args estiver vazio ele retorna 
            print("ERRO: parametros nn estabelecidos")
            return
        if len(args) == 1:
            self.comandos[command](args[0])

        if len(args) > 1:
            for i in args:
                self.comandos[command](i)
                # print(type(i))
        

    def separador(self,cmd) -> list:
        cmd = [i.replace(",", "") for i in cmd if i not in self.ignorar]
        command = None
        args = [] 

        for i in cmd:
            if i in self.comandos: #* i é um comandos
                if self.memory["lass_command"]:
                    command = self.memory["lass_command"]
                else:
                    command = i
                    self.memory["lass_command"] = i
                continue

            #* i é um conector
            if i in self.conectores:
                continue

            else: #* i é um app
                if self.memory["lass_command"]:
                    args.append(i)
                    self.memory["lass_app"] = i

        print(f"{cmd=}, {command=}, {args=}")
        return command, args
    

Agent = agent()


# user_input = input("oq vc gostaria de fazer? ")
user_input = "abrir o chrome"
cmd = user_input.lower().split()

# Agent.separador(cmd)
Agent.exe(*Agent.separador(cmd))