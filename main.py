from core.DecisionEngine import DecisionEngine
from core.AgenteEnginer import AgentEnginer

#mudar depois para configuraçoes padroes
from memory.criar_essa_porrinha import arrumar


import random
user_profile = r"data/user_vectors.json"
# MemorySystem.save(user_profile, {
#             "aprendizado": 0.5,
#             "entretenimento": 0.5,
#             "musica": 0.5,
#             "programacao": 0.5,
#             "fps": 0.5,
#             "estrategia": 0.5,
#             "rock": 0.5,
#             "eletronica": 0.5,
#             "social": 0.5,
#             "competitivo": 0.5
#         })
# arrumar()

users = 1
interacoes = 1
i = 1

while i <= users:
    arrumar() # reset para a proxima interação nn afetar a anterior
    print(f"=============================================")
    user1 = DecisionEngine(user_profile)
    print(f"user number {i}")
    stop = interacoes
    j = 1

    while j <= stop:
        action = user1.decide_action()
        user1.learning(action, feedback=random.choice([-1, 1]))
        print(action)
        j += 1

    print("=======================================")
    i += 1