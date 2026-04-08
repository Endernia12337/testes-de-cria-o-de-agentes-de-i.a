import win32gui
from openapp import rodar
janelas = {}
# user_input = input("oq vc gostaria de abrir? ")
def janelas_ativas (handle,extra) -> list: 
    generic = ["Microsoft Text Input Application", "Program Manager", "MSCTFIME", "Default"] 
    titulo = win32gui.GetWindowText(handle)
    if( titulo and win32gui.GetParent(handle) == 0
        and win32gui.IsWindowVisible(handle)
        and titulo not in generic 
        and win32gui.IsWindowEnabled(handle) 
        and not win32gui.IsIconic(handle) ): 
        janelas.update({titulo : handle}) 
    
def abrir_janela(program):
    janelas.clear()
    win32gui.EnumWindows(janelas_ativas,None)
    
    matches = {}
    num = 1
    for i in janelas.keys():
        if program in i.lower():
            matches.update({i : janelas[i]})
            num += 1
    #* abrir
    if len(matches) == 1:
        win32gui.SetForegroundWindow(list(matches.values())[0]) #* se for apenas 1 abre direto
    elif not matches: #* se nn existir cria nova instancia desse app
        rodar(program)
    else: #* se existir mais de 1 pergunta qual quer abrir
        for i in matches.keys():
            print(i)
        command = input("abrir qual janela?")
        for i in matches.keys():
            if command in i:
                win32gui.SetForegroundWindow(matches[i])