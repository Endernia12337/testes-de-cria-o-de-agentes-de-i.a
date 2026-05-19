from memory.MemorySystem import MemorySystem
from brain.BrainError import InvalidActionError,MemoryError,ActionTrackerError,ValidationError

class ActionTracker:
    def __init__(self) -> None:
        self.count_file = r"data/action_counts.json" # ela define pois esses arquivos são usados so por ela, se eu senti necessario depois programo outra forma dela acessar 
        self.historic_file = r"data/recent_actions.json"

        self.error_count = None 
        self.error_historic = None

        self.memory = MemorySystem()
        self._load_memory()
        self._validate_memory()
    
    def _load_memory(self): #mudar nome futuramente
        try:
            self.count = self.memory.load( self.count_file)
        except MemoryError as e: 
            self.count = {}
            self.error_count = e 
            print(e)
        except Exception as e:
            print(e)
            self.error_count = e 

        try:
            self.historic = self.memory.load(self.historic_file)
        except MemoryError as e:
            self.historic = []
            self.error_historic = e
            print(e)
        except Exception as e:
            print(e)
            self.error_historic = e
        
    def _validate_memory(self):
        if not isinstance(self.count, dict):
            self.error_count = ValidationError(
                field="count",
                expected="dict",
                received=type(self.count).__name__,
                operation="_validate_memory"
            )

            print(self.error_count)
            self.count = {}

        if not isinstance(self.historic, list):
            self.error_historic = ValidationError(
                field="historic",
                expected="list",
                received=type(self.historic).__name__,
                operation="_validate_memory"
            )

            print(self.error_historic)
            self.historic = []
        
    def get_count(self, action_name):
        if self.error_count:
            raise ActionTrackerError(f"erro count :{self.error_count}","get_count") # temporario, so para debug proovavelmente aq vai um actionTracker ou so um return
        try:
            return self.count[action_name]
        except KeyError:
            raise InvalidActionError(action_name,"ActionTracker/get_count")

    def upgrade_window(self,action_name):
        if self.error_historic:
            raise ActionTrackerError(f"historic : {self.error_historic}","get_count")
        if self.error_count:
            raise ActionTrackerError(f"count : {self.error_count}","get_count")
    
        try:
            self.historic.insert(0,action_name)
            self.count[action_name] += 1
        except KeyError:
            raise InvalidActionError(action_name,"ActionTracker/upgrade_window")
            
        if len(self.historic) >  50:
            last_iten = self.historic[-1]
            self.count[last_iten] -= 1
            self.historic.pop()

        self.memory.save(self.historic_file,self.historic)
        self.memory.save( self.count_file, self.count)

if __name__ == '__main__':
    actiontracker = ActionTracker()
    try:
        print(actiontracker.get_count("jogar_valorant"))
    except Exception as e:
        print(e) 
        