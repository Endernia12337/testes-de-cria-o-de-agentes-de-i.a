import subprocess
from groq import Groq
import os
import dotenv
dotenv.load_dotenv(".env")
# Configuração mínima
API = os.getenv("CHAVE_API")
client = Groq(api_key=API)

class AppLaucher:
    def __init__(self):
        pass

    def _ia_aswer(self, texto):
        prompt = """Você é um tradutor de linguagem natural para comandos de terminal Windows (CMD/PowerShell).
    REGRAS CRÍTICAS:
    1. Responda EXCLUSIVAMENTE com o comando.
    2. NUNCA use blocos de código (Markdown), explicações ou pontuação extra.
    3. Se o usuário pedir para abrir algo, use 'start' seguido do nome do executável ou caminho.
    4. Use caminhos de sistema comuns (ex: notepad, calc, explorer).

    Exemplos:
    User: abrir calculadora
    AI: calc
    User: listar arquivos da pasta atual
    AI: dir
    User: abrir o google
    AI: start chrome www.google.com
    """

        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": texto}
            ],
            temperature=0
        )

        return resp.choices[0].message.content.strip()

    def start_app(self, program):
        comando = self._ia_aswer(f"start {program}")
        
        print(f"Executando: {comando}")
        if not comando.startswith(("start", "calc", "notepad", "code")):
            print("comando suspeito")
            return
        subprocess.run(comando, shell=True)
