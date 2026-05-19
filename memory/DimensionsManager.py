from memory.MemorySystem import MemorySystem

class DimensionsManager:
    def __init__(self,user_vectors,action_vectors,count,dimensions) -> None:
        self._path_user = user_vectors
        self._path_actions = action_vectors
        self._path_count = count
        self._path_dimensions = dimensions

        self.memory = MemorySystem()

        self._user_vectors = self.memory.load(self._path_user)
        self._action_vectors = self.memory.load(self._path_actions)
        self._count = self.memory.load(self._path_count) 
        self._dimensions = self.memory.load(self._path_dimensions) 

    def _save_all(self):
        self.memory.save(self._path_actions,self._action_vectors)
        self.memory.save(self._path_count,self._count)
        self.memory.save(self._path_user,self._user_vectors)
        self.memory.save(self._path_dimensions,self._dimensions)

    def _sync_all(self):
        self.sync_dimensions()
        self.sync_actions()
    
    def sync_dimensions(self):
        for dimension in self._dimensions:
            # nos usuarios
            if dimension not in self._user_vectors.keys():
                self._user_vectors[dimension] = 0.0

            for action_data in self._action_vectors.values():
                if dimension not in action_data:
                    action_data[dimension] = 0.0
            
        self._save_all()
    
    def sync_actions(self):
        for action in self._action_vectors:
            if action not in self._count:
                self._count[action] = 0
        self._save_all()

    def update_action_weight(self,action,dimension,value:float = 0.0):
        #se na ação precisar ser atualizada, tipo apareceu uma nova dimenção e ela tem um peso nessa ação != 0

        self._action_vectors[action][dimension] = value
        self._save_all()

    def create_dimension(self,dimension_name):
        self._dimensions.append(dimension_name)
        self.sync_dimensions()
        self._save_all() #apenas como fator de segurança

    def create_action(self,action_name,dimensions : dict[str,float]):
        dimensions_pattern = {i:0.0 for i in self._dimensions}
        
        for dimension in dimensions.keys():
            if dimension not in self._dimensions:
                self.create_dimension(dimension)

        for dimension in dimensions:
            dimensions_pattern[dimension] = dimensions[dimension]
            
        self._action_vectors[action_name] = dimensions_pattern
        self._sync_all()

        self._save_all()
