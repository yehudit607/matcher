import sqlite3
from collections import Counter
import numpy as np


def candidate_finder(job):
    """
     a function that given a Job, pulls all the Candidates
     from the DB, and returns the best ones for the Job.
    :param job: job ID
    """
    conn = sqlite3.connect("matcher.db")
    cur = conn.cursor()
    jobquery = 'select * from JOB where JOB.ID = (?)'
    cur.execute(jobquery, (job,))
    job = cur.fetchall()
    if not len(job):
        print("Job doesn't appear, press 1 to add")
        return()

    jobTitle = job[0][1]
    cur.execute('''SELECT C.* ,C_S.skill_id
                from CANDIDATE C  
                LEFT JOIN
                (select CANDIDATE_ID, group_concat
                   (CAST(SKILL_ID AS SIGNED))as skill_id
                     from  SKILL_TO_CANDIDATE S2
               group by CANDIDATE_ID)AS C_S
               ON C.ID = C_S.CANDIDATE_ID
    '''
                )
    candidates = cur.fetchall()
    print(candidates)
    candidates_dict = []
    keys = ['id', 'name', 'title', 'skill']
    for c in candidates:
        candidate_dict = dict()
        for ind in range(len(keys)):
            key, value = keys[ind], c[ind]
            candidate_dict[key] = value
        candidates_dict.append(candidate_dict)
    score_list = np.zeros(len(candidates_dict))
    for ind, candidate in enumerate(candidates_dict):
        jobTitle_words = set(jobTitle.split())
        score_list[ind] = search(jobTitle_words, candidate.get("title"))
        if score_list[ind]:
            skill = candidate.get("skill")
            if skill is not None:
                score_list[ind] += search_skill(job[0][2], skill)

    max = np.max(score_list)
    if not max:
        print("Sorry, no found match ")
        return
    bestScore = [i for i, x in enumerate(score_list) if x == max]  # => [1, 3]
    for b in bestScore:
        print("bestCandidate:", candidates_dict[b])


def search_skill(job_skill, candidate_skill):
    """
   A function that checks whether a candidate has
    the qualifications required for the position
    :param job_skill(str):job skill
    :param candidate_skill(list):list of skill's candidate
    :return(bool): 1 if found, else 0
    """
    candidate_skill_list = list(eval(candidate_skill))
    if job_skill in candidate_skill_list:
        return 1
    return 0


def search(words, candidate_title):
    """
    A function that checks a how many words from
    the job title appears in the candidate title
    :param words(list):words of job title
    :param candidate_title(string)
    :return count_common(int):Number of words in a sentence
    """
    latest_counted = Counter(candidate_title.strip().split())
    common_words = words.intersection(latest_counted)
    count_common = sum(latest_counted[wrd] for wrd in common_words)
    return count_common
