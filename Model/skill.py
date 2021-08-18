import sqlite3


def insert_skill(skill_name):

    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO SKILL (NAME) VALUES (?)", (skill_name,))
    conn.commit()
    conn.close()


def view_skill():
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM SKILL ")
    rows = cur.fetchall()
    conn.close()
    return rows
