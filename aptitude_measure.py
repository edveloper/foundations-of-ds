def aptitude():
    age = int(input("How old are you?: "))
    experience = int(input("How long were you at your previous job, in months?: "))
    score = int(input("What did you score in the competency test?: "))
    competence = (age + experience) * score

    if competence > 200:
        print("Candidate is competent enough")
    if competence < 200:
        print("Candidate is not competent")

aptitude()
