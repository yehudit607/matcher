import sqlite3


def createDB():
    connection = sqlite3.connect('matcher.db')
    print("Opened database successfully")
    cursor = connection.cursor()

    create_table_skill = '''CREATE TABLE IF NOT EXISTS  SKILL
            (SKILL_ID INTEGER PRIMARY KEY ,
             NAME     TEXT            NOT NULL);'''
    cursor.execute(create_table_skill)

    create_table_job = '''CREATE TABLE IF NOT EXISTS JOB
            (ID        INTEGER PRIMARY KEY,
             TITLE     TEXT            NOT NULL,
             SKILL_ID  INT             NOT NULL,
             FOREIGN KEY(SKILL_ID) REFERENCES SKILL(ID));'''
    cursor.execute(create_table_job)

    create_table_candidate = '''CREATE TABLE IF NOT EXISTS CANDIDATE
            (ID        INT PRIMARY KEY NOT NULL,
             NAME     TEXT            NOT NULL,
             TITLE     TEXT            NOT NULL);'''
    cursor.execute(create_table_candidate)

    create_table_skill2candidate = '''CREATE TABLE IF NOT EXISTS SKILL_TO_CANDIDATE
            (CANDIDATE_ID        INT  NOT NULL,
             SKILL_ID  INT             NOT NULL,
             FOREIGN KEY(Skill_ID) REFERENCES SKILL(SKILL_ID),
             FOREIGN KEY(CANDIDATE_ID) REFERENCES Skills(CANDIDATE_ID));'''
    cursor.execute(create_table_skill2candidate
                   )
    print("Table created successfully")
    connection.close()
