from .BrainError import ActionTrackerError, LearningError

from memory.MemorySystem import MemorySystem
from memory.ActionTracker import ActionTracker


class LearningBrain:
    def __init__(self,actions_vectors, user_profile:dict, dimensions:list):
        self.actions_vectors = actions_vectors
        self.user_profile = user_profile
        self.dimensions = dimensions

        self.memorysystem = MemorySystem
        self.tracker = ActionTracker()


    def learning_by_feedback(self, action_name: str, feedback: int, learning_rate=0.5, decay=True, decay_rate=0.02):
        if not decay:
            decay_rate = 0.0

        action_vector = self.actions_vectors[action_name]
        try:
            count = self.tracker.get_count(action_name)
        except  ActionTrackerError as e:
            raise LearningError(action_name,operation="learning_by_feedback",error=e)
        
        penality = count/100 
        if penality <= 0.02:
            penality = 0.03
            
        decay_rate = decay_rate - count/100
        for dimension in self.dimensions:
            try:
                current_value = self.user_profile[dimension]
            except KeyError:
                raise LearningError(action_name,operation="learning_by_feedback", dimension=dimension,error=f"dimension does not exist in user profile")
            try:
                kn = action_vector[dimension]
            except KeyError:
                raise LearningError(action_name,operation="learning_by_feedback", dimension=dimension,error="dimension does not exist in action_vectors")
            new_value = round(((1 - decay_rate) * current_value+ learning_rate *(1 - current_value) * (kn * feedback)),2)
            new_value = max(0.0, min(1.0, new_value))

            self.user_profile[dimension] = new_value
        
        self.tracker.upgrade_window(action_name)

        return self.user_profile