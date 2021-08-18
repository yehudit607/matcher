import sqlite3
import Model as m


def insert_skills_candidate(candidate_id, skills_name):
    """
    a function to insert skills of candidate to DB
    :param candidate_id
    :param skills_name
    """
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    for skill in skills_name:
        query = 'SELECT SKILL_ID FROM SKILL WHERE NAME=(?)'
        cur.execute(query, (skill,))
        rows = cur.fetchall()
        if not rows:
            conn.commit()
            conn.close()
            conn = sqlite3.connect("matcher.db")
            cur = conn.cursor()
            m.insert_skill(skill)
            cur.execute(query, (skill,))
            rows = cur.fetchall()
        skill_id = rows[0][0]
        cur.execute('''INSERT INTO SKILL_TO_CANDIDATE (CANDIDATE_ID, SKILL_ID)
                    VALUES ( ?,?)''',
                    (candidate_id, skill_id))
    conn.commit()
    conn.close()


def view_skills_candidate():
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM SKILL_TO_CANDIDATE ")
    rows = cur.fetchall()
    conn.close()
    return rows
