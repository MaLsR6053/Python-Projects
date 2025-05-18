#We will ask for an age
age = input("How old are you? Please enter your age: ")
if age:
    age = int(age)
    if age >=18 and age < 21:
        #18-21 needs a wristband
        print("You can enter, however you will need a wristband.")
    elif age >= 21:
        #21 and over can drink, and normal entry
        print("You are good to go, have a nice night.")
    else:
        #You are too young to be here
        print("You are too young to be here, sorry. :*(")
else:
    print("What the hell, give me a fucking input you jerk. Not how this works.")