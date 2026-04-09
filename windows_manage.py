import win32gui
from app_laucher import AppLaucher

class WindowsManager:
    """
    controle do windons como um todo, podendo abrir abas e trazendo paginas abertas ja para sua tela
    """
    def __init__(self):
        self.windows = {}
        self.num = 0
        self.Al = AppLaucher()
        pass
    
    def _windows_update(self,handle, extra) -> None:
        generic = ["Microsoft Text Input Application", "Program Manager", "MSCTFIME", "Default"] 
        title =     win32gui.GetWindowText(handle)
        if( title and win32gui.GetParent(handle) == 0
        and win32gui.IsWindowVisible(handle)
        and title not in generic 
        and win32gui.IsWindowEnabled(handle) 
        and not win32gui.IsIconic(handle)):
            self.windows[self.num] = (title, handle)
            self.num += 1
    
    @property
    def windows_on(self) -> dict:
        """
        return list of windows open at the moment
        """
        self.windows.clear()
        self.num = 0
        win32gui.EnumWindows(self._windows_update,None)
        return self.windows
    
    def open_window(self, program : str) -> None:
        """
        **ARGS****
            `program`  name of window or program to be open
        """
        windows = self.windows_on

        matches = {}

        for titulo, handle in windows.values():
            if program.lower() in titulo.lower():
                matches[titulo] = handle
        
        if len(matches) == 1:
            win32gui.SetForegroundWindow(list(matches.values())[0]) #* se for apenas 1 abre direto

        elif not matches: #* se nn existir cria nova instancia desse app
            self.Al.start_app(program)

        else: #* se existir mais de 1 pergunta qual quer abrir
            print("==================================================== ")
            for i in matches.keys():
                print(i)
            print("==================================================== ")
            op = False
            while not op:
                command = input("abrir qual janela? ")
                for i in matches.keys():
                    if command in i.lower():
                        win32gui.SetForegroundWindow(matches[i])
                        return
                print("não entendi poderia repetir?")