import json
from brain.BrainError import MemoryError
class MemorySystem:
    @staticmethod
    def load(path: str):
        try:
            with open(path, "r", encoding='utf-8') as f :
                return json.load(f)
        except FileNotFoundError:
            raise MemoryError("load",path,"FileNotFoundError")
            
    
    @staticmethod
    def save(path:str, memory_instance):
        try:
            with open(path,'w',encoding='utf-8') as f:
                json.dump(memory_instance, f,indent=4)
        except json.JSONDecodeError:
            raise MemoryError("save",path, "JSONDecodeError")
        