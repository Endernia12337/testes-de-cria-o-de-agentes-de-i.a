import random
from wind import abrir_janela

context = {
    "ultimo_app" : None,
}


def abrir (target):
    abrir_janela(target)
    context["ultimo_app"] = target
def fechar (target):
    print (f"fechando {target}")
    context["ultimo_app"] = target
def mover (target, local, new_local):
    print (f"{target} movido de {local}, para {new_local}")

comprimentar = ["ok senhor", "com certeza"]


comandos = {
    "abri" : abrir,
    "abrir" : abrir,
    "iniciar" : abrir,
    "fechar" : fechar,
    "mover" : mover,
}


user_input = input("oq vc gostaria de fazer? ")
# user_input = "abrir vscode, chrome"

ignorar = ("o","a")
conectores = ("e", )

cmd = user_input.lower().split()

cmd = [i.replace(",", "") for i in cmd if i not in ignorar]


def exe(commands: list):
    print(random.choice(comprimentar))

    for i in commands:
        comandos[i[0]](i[1])
    


def separador(cmd) -> list:
    executar = []
    comando_atual = None
    for i in cmd:
        if i in comandos: #* i é um comandos
            comando_atual = i
            continue

        #* i é um conector
        if i in conectores:
            continue

        else: #* i é um app
            if comando_atual:
                executar.append((comando_atual, i))

    print (executar)

exe(separador(cmd))