import sqlite3

class TagDB:
    def __init__(self, outputFile='tags.db'):
        self.db = sqlite3.connect(outputFile)
        cursor = self.db.cursor()
        cursor.execute("PRAGMA synchronous = OFF;")
        cursor.execute("PRAGMA journal_mode = MEMORY;")
        cursor.execute("""CREATE TABLE IF NOT EXISTS tags (
        location   TEXT,
        line       INT,
        column     INT,
        offset     INT,
        start_line INT,
        start_col  INT,
        end_line   INT,
        end_col    INT,
        kind_name  TEXT,
        type_name  TEXT,
        spelling   TEXT,
        display    TEXT,
        is_def     INT,
        def        TEXT,
        is_static  INT,
        is_ref     INT,
        ref        TEXT,
        usr        TEXT);""")
        self.db.commit()

    def __del__(self):
        self.db.close()

    def create_index(self):
        cursor = self.db.cursor()
        cursor.execute("CREATE INDEX IF NOT EXISTS location_index ON tags(location);")
        cursor.execute("CREATE INDEX IF NOT EXISTS location_line_index ON tags(location,line);")
        cursor.execute("CREATE INDEX IF NOT EXISTS kind_index ON tags(kind_name);")
        cursor.execute("CREATE INDEX IF NOT EXISTS type_index ON tags(type_name);")
        cursor.execute("CREATE INDEX IF NOT EXISTS spelling_index ON tags(spelling);")
        cursor.execute("CREATE INDEX IF NOT EXISTS display_index ON tags(display);")
        cursor.execute("CREATE INDEX IF NOT EXISTS is_def_index ON tags(is_def);")
        cursor.execute("CREATE INDEX IF NOT EXISTS def_index ON tags(def);")
        cursor.execute("CREATE INDEX IF NOT EXISTS is_static_index ON tags(is_static);")
        cursor.execute("CREATE INDEX IF NOT EXISTS is_ref_index ON tags(is_ref);")
        cursor.execute("CREATE INDEX IF NOT EXISTS ref_index ON tags(ref);")
        cursor.execute("CREATE INDEX IF NOT EXISTS usr_index ON tags(usr);")            
        self.db.commit()
    
    def persist(self, ast):
        cursor = self.db.cursor()
        cursor.executemany("INSERT INTO tags VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ast)
