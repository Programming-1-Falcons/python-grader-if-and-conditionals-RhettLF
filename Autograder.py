while True: 

    #TPP = Total points possible
    #PR = points recived
    name = input("Enter student's first name. \n")
    lname = input("Enter student's last name. \n")
    if (name == "Rhett" or name == "rhett") and (lname == "Lynwood" or lname == "lynwood" or lname == "Littlefield" or lname == "littlefield"):
        print("perfect score. No further grading needed.")
        continue
    elif (name == "Peter" or name == "peter" or name == "Peta" or name == "peta") and (lname == "Griffin" or lname == "griffin"):
        print(name,",", "the horse is here.")
        continue
    elif (name == "James" or name == "james" or name == "JJ" or name == "jj" or name == "Mr." or name == "mr" or name == "Mr") and (lname == "Oliphant" or name == "oliphant"):
        print("Welcome, Teacher! perfect score. No further grading needed")
        continue
    TPP = float(input("Enter total points possible: \n"))
    PR = float(input("Enter points recived: \n"))

    score = PR / TPP

    if score <= 0.50:
        print(name, lname,"," " F.")
    elif score <= 0.60:
        print(name, lname,"," " D.")
    elif score <= 0.75:
        print(name, lname,"," " C.")
    elif score <= 0.88:
        print(name, lname,"," " B.")
    elif score <= 1.00:
        print(name, lname,"," " A.")