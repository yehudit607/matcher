import Model as m


def menu():
    """
    Function to display the user menu
    """
    menu = {}
    menu['1'] = "Add Job."
    menu['2'] = "Add Candidate."
    menu['3'] = "Add Skill."
    menu['4'] = "View jobs"
    menu['5'] = "view candidates"
    menu['6'] = "view skills"
    menu['7'] = "Find a candidate"
    menu['8'] = "Exit"
    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])
        selection = input("Please Select:")

        if selection == '1':
            skillID = input("enter ID ")
            jobTitle = input("enter job title ")
            m.insert_job(jobTitle, skillID)

        elif selection == '2':
            candidateID = input("enter ID ")
            candiateTitle = input("enter candidate title ")
            candidateName = input("enter candidate name")
            skills = []
            not_done = True
            while not_done:
                inp = input('enter skills, type end to finish: ')
                if inp.lower() != 'end':
                    skills.append(inp)
                else:
                    break
            print(skills)
            m.insert_candidate(candidateID, candidateName, candiateTitle)
            if skills:
                m.insert_skills_candidate(candidateID, skills)

        elif selection == '3':
            skillName = input("enter Skill name ")
            m.insert_skill(skillName)

        elif selection == '4':
            print(m.view_job())

        elif selection == '5':
            print(m.view_candidate())

        elif selection == '6':
            print(m.view_skill())

        elif selection == '7':
            jobID = input("enter Job Id")
            m.candidate_finder(jobID)

        elif selection == '8':
            break
        else:
            print("Unknown Option Selected!")
