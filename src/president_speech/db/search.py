from president_speech.db.connection_manager import ConnectionManager


def title(keyword: str):
    cm = ConnectionManager()
    conn = cm.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT 
            date, 
            title 
        FROM president_speeches 
        WHERE title LIKE '%{keyword}%'
        """)

    for row in cursor:
        print(row)


def speech(keyword: str):
    cm = ConnectionManager()
    conn = cm.get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT 
            date, 
            title 
        FROM president_speeches 
        WHERE speech_text LIKE '%{keyword}%'
        """)

    for row in cursor:
        print(row)
