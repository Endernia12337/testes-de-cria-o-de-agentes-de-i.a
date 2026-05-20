from core.DecisionEngine import DecisionEngine
from core.AgenteEnginer import AgentEnginer

#mudar depois para configuraçoes padroes
from memory.criar_essa_porrinha import arrumar
from memory.MemorySystem import MemorySystem
from memory.ContextManager import ContextManager
from memory.DimensionsManager import DimensionsManager

if __name__ == '__main__':
    context = ContextManager()

    # context._clear_historic()
    # context._create_row_historic()

    # app = context.event_history_get_historic()
    new = context.current_context_update("discord","open")
    app = context.current_context_get_app()
    print(app)

    context.event_history_add_event(new[0],new[1],True)