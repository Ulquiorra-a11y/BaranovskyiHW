import pymysql



db_name = "notes_app_121225_ptm_Baranovskyi"
class DB:

    def __init__(self):
        self.__config = {
        'host': 'ich-edit.edu.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'cursorclass': pymysql.cursors.DictCursor
      }
        print(self.__config)

    def __enter__(self):
        self.__conn = pymysql.connect(**self.__config)
        self.__cursor = self.__conn.cursor()
        print("Connection successful!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__conn.close()
        print("__exit__")
        return False

    def _execute(self, sql, params=None):
        self.__cursor.execute(sql, params)
        self.__conn.commit()
        return self.__cursor.fetchall()

    def db_create(self):
        self._execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        return f"Database '{db_name}' created or already exists"
    def db_use(self):
        self._execute(f"USE {db_name}")


    def table_create(self):
        self._execute("""CREATE TABLE IF NOT EXISTS notes (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                                                  title varchar(100) NOT NULL,
                                                  content varchar(100) NOT NULL)""")
        return f"Table 'notes' created or already exists"

    def insert_note(self, title, content):
        self._execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s)",
            (title, content)
        )
        return f"Note added: {title}"

    def get_all_notes(self):
        return self._execute("SELECT * FROM notes")



with DB() as db:
    print(db.db_create())
    db.db_use()
    print(db.table_create())
    # print(db.insert_note("Shopping list", "apple, banana, milk"))
    print(db.get_all_notes())

