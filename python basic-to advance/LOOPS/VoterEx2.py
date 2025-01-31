#VoterEx2.py
while(True):
    age=int(input("Enter Age of Citizen:"))
    if(age>=18):
        print("{} Years Citizen is Eligible to Vote:".format(age))
        break
    else:
        print("\t{} Years Citizen is Not Eligible to Vote:".format(age))
