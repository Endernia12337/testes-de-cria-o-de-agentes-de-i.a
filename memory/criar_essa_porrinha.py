from memory.MemorySystem import MemorySystem

def arrumar():
    memory = MemorySystem

    actions  = memory.load("action_vectors.json")
    keys = actions.keys()

    try:
        counts = memory.load("action_counts.json")
    except:
        counts = {}

    for i in keys:
        counts[i] = 0

    memory.save("action_counts.json",counts)
    memory.save("recent_actions.json", [])
    memory.save("user_vectors.json", {
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