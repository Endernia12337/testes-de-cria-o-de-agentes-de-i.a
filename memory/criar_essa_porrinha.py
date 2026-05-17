from memory.MemorySystem import MemorySystem

def arrumar():
    memory = MemorySystem

    actions  = memory.load(r"data/action_vectors.json")
    keys = actions.keys()

    try:
        counts = memory.load(r"data/action_counts.json")
    except:
        counts = {}

    for i in keys:
        counts[i] = 0

    memory.save(r"data/action_counts.json",counts)
    memory.save("data/recent_actions.json", [])
    memory.save("data/user_vectors.json", {
                "aprendizado": 0.5,
                "entretenimento": 0.5,
                "musica": 0.5,
                "programacao": 0.5,
                "fps": 0.5,
                "estrategia": 0.5,
                "rock": 0.5,
                "eletronica": 0.5,
                "social": 0.5,
                "competitivo": 0.5
            })