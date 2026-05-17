import random
from .BrainError import InvalidActionError
class DecisionBrain:
    def __init__(self,actions_vectors: dict, user_profile:dict, dimensions:list):
        self.actions_vectors = actions_vectors
        self.user_profile = user_profile
        self.dimensions = dimensions

        
    def _calc_score(self):
        best_actions = []
        for i in range(5):
            best_actions.append(("action",float("-inf")))
        can_pass = False
        while not can_pass:
        
            for action in self.actions_vectors.keys():
                action_vector = self.actions_vectors[action]
                score = 0.0
            
                for dimension in self.dimensions:
                    score += action_vector[dimension] * self.user_profile[dimension]  


                for idx, i in enumerate(best_actions):
                    if score > i[1]:
                        if action in list(self.actions_vectors.keys()):
                            best_actions.insert(idx,(action,score))
                            break
                best_actions = best_actions[:5]
            can_pass = True
            for i in best_actions:
                if i[0] == "action" or i[1] == float("-inf"):
                    best_actions.remove(i)
                    can_pass = False    

        return best_actions
        # return [("action",0.1),("action",0.1),("action",0.1),("action",0.1),("action",0.1)]

    def decide_action(self) -> str:
        best_actions = self._calc_score()
        best_scores = [i[1] for i in best_actions]

        for i in best_actions:
            if i[0] == "action" or i[1] == float("-inf"):
                raise  InvalidActionError(i[0],"deside_action")
        sum_best_scores = sum(best_scores)
        if sum_best_scores <= 0:
            best_action = random.choice([i[0] for i in best_actions])
            return best_action
        probabilits = []

        for action in best_actions:
            probabilits.append([action[0], action[1] / sum_best_scores])
         
        for idx, action in enumerate(probabilits):
            if idx > 0:
                probabilits[idx][1] += probabilits[idx -1][1]
        
        number = random.random()
        best_action = None
        for i in probabilits:
            if number < i[1]:
                best_action = i[0]
                break

        if best_action == None:
            best_action = random.choice([i[0] for i in best_actions])
        return best_action
    