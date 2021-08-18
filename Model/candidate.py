import sqlite3


def insert_candidate(id, name, title):
    """
    a function for insert new candidate to DB
    :param id(int):candidate id
    :param name(string):candidate name
    :param title:candidate title
    """
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO CANDIDATE (ID,NAME, TITLE) VALUES (?, ?, ?)",
                (id, name, title))
    conn.commit()
    conn.close()


def view_candidate():
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM CANDIDATE ")
    rows = cur.fetchall()
    conn.close()
    return rows
