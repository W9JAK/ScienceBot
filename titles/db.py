import psycopg2
from config import DATABASE_URL

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS JobTitles (
        JobTitle TEXT
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_job_titles(job_titles):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.executemany('''
    INSERT INTO JobTitles (JobTitle) VALUES (%s)
    ''', [(title,) for title in job_titles])
    conn.commit()
    cursor.close()
    conn.close()

def delete_all_job_titles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM JobTitles')
    conn.commit()
    cursor.close()
    conn.close()
