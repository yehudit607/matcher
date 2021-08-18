import Model as m
import os


if __name__ == '__main__':
    print(m.view_skills_candidate())
    if not os.path.isfile('matcher.db'):
        m.createDB()
        m.insert_initalData()
    print(m.view_job())
    print(m.view_candidate())
    print(m.view_skill())
    print(m.view_skills_candidate())
    m.menu()
