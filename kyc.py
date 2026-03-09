# Create a kyc app that collect info from users
# info includes : name, surname, age, genders, state of origin, occupation, tribe

name =input ("Enter your first name: ")
laatname=input ("Enter your surname: ")
age=input("Enter your age: ")
gender=input ("Are you male or female")
state=input("Enter your stateof origin")
occupation=input("What is your occupation?: ")
tribe=input("What Nigeria tribe are you from?: ")
print()
# print ("Customer Profile:\t")
# print("\tFull Name -",name, lastname)
# print("\Age -",age)
# print("\tGender -",gender)
# print("\tState of origin -",state)
# print("\tOccupation -",occupation)
# print("\tTribe -",tribe)
print(f""" Customer Profile:\t
           ->Full Name:(name) (lastname)\try
           ->age: (age)\try
            ->Gender: (occupation)\try
            ->Tribe: (tribe)
""")