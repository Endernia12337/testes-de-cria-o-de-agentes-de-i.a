from .MemorySystem import MemorySystem
import sqlite3 as sql

# TODO fazer timestamps
# TODO fazer response ser um text de errors
# TODO Get context retorna dict para escalonar

class ContextManager:
    def __init__(self) -> None:
        self.conn = sql.connect(r"data\context.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS current_context(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            current_app TEXT NOT NULL,
            current_command TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS event_history(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            app TEXT NOT NULL,
            command TEXT NOT NULL,
            response BOOLEAN NOT NULL
        )
        """)

        self.conn.commit()
# TODO melhorar nomes
# apenas para testes , deletar depois
        
    def _clear_historic(self):
        self.cursor.execute("DELETE FROM event_history")

        self.cursor.execute("""
            DELETE FROM sqlite_sequence
            WHERE name='event_history'
        """)

        self.conn.commit()
        self.conn.close()
# ---------------------


    def current_context_get_app(self):
        self.cursor.execute(
        """
        SELECT current_app FROM current_context
        """
        )
        current_app =  self.cursor.fetchone()
        self.conn.close()
        return current_app 
    
    def current_context_get_command(self):
        self.cursor.execute(
        """
        SELECT current_command FROM current_context
        """
        )
        current_command =  self.cursor.fetchone()
        self.conn.close()
        return current_command 

    def current_context_update(self,app,comamnd):
        self.cursor.execute(
        """
            UPDATE current_context
            SET current_app = (?), current_command = (?)
        """, (app,comamnd))
        self.conn.commit()
        self.conn.close()
        return [app,comamnd]

    def event_history_get_history_by_app(self,app):
        
        self.cursor.execute(
            """
            SELECT * FROM event_history
            WHERE app == (?)
            """,(app,)
        )
        app = self.cursor.fetchall()
        self.conn.close()
        return app        

    def event_history_get_historic(self):
        self.cursor.execute(
            """
            SELECT * FROM  event_history
            ORDER BY id DESC LIMIT 5
            """
        )
        historic = self.cursor.fetchall()
        self.conn.close()
        return historic
    
    def event_history_add_event(self,app = None, command = None, response = None):
        #apenas para testes apagar depois
        if not app:
            app = "chrome"
        if not command:
            command = "open"
        if not response:
            response = True
        #--------------
        self.cursor.execute(
            """
            INSERT INTO event_history (app, command, response)
            VALUES (?, ?,?)
            """, (app,command, response))
        self.conn.commit()
        self.conn.close()