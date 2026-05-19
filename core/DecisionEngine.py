from brain.LearningBrain import LearningBrain
from memory.MemorySystem import MemorySystem
from brain.DecisionBrain import DecisionBrain
from brain.BrainError import InvalidActionError, LearningError


class DecisionEngine:
    def __init__(self, user_vectors_path: str):
        self.user_vectors_path = user_vectors_path
        self.actions_vectors_path = r"data\action_vectors.json"
        self.dimesions_path = r"data\dimensions.json"

        self.actions_vectors = MemorySystem.load(self.actions_vectors_path)
        self.user_profile = MemorySystem.load(self.user_vectors_path)
        self.dimesions = MemorySystem.load(self.dimesions_path)
        
        self.learning_brain = LearningBrain(self.actions_vectors,self.user_profile, self.dimesions)
        self.decision_brain = DecisionBrain(self.actions_vectors,self.user_profile,self.dimesions)
    
    def decide_action(self): 
        try:
            return self.decision_brain.decide_action()
        except InvalidActionError as e:
            print(e)
            return ""

    def learning(self, action_name: str, feedback: int, learning_rate=0.5, decay=True, decay_rate=0.02): 
        if action_name == "":
            return
        try:
            new_value = self.learning_brain.learning_by_feedback(action_name, feedback, learning_rate, decay, decay_rate)
            MemorySystem.save(path = self.user_vectors_path, memory_instance = new_value)
        except LearningError as e:
            print(e)
            return
        except TypeError as e:
            print(e)
            return
