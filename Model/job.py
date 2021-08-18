import sqlite3


def insert_job(title, skill):
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO JOB (TITLE, SKILL_ID) VALUES ( ?,?)",
                (title, skill))
    conn.commit()
    conn.close()


def view_job():
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM JOB ")
    rows = cur.fetchall()
    conn.close()
    return rows
