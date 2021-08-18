import Model as m


def insert_initalData():

    m.insert_job("backend developer", 1)
    m.insert_job("backend developer", 2)
    m.insert_job("fullstack developer", 4)
    m.insert_job("software developer", 6)
    m.insert_job("software engineer", 6)

    m.insert_skill("python")
    m.insert_skill("react")
    m.insert_skill("vue.js")
    m.insert_skill("node.js")
    m.insert_skill("machine learning")

    m.insert_candidate(222, "Jhon", "software developer")
    m.insert_candidate(333, "Ben", "software engineer")
    m.insert_candidate(444, "Dana", "product manager")

    m.insert_skills_candidate(111, ["python"])
    m.insert_skills_candidate(111, 2)
    m.insert_candidate(333, 1)
    m.insert_candidate(444, 2)
