musicians = ["J.Cole","Eminem","Drake",
             "Childish Gambino","Joyner Lucas","Jaden"]
places = [(40.222,52.335,56.552,13.533)]
mundo = {"Height":"5ft 7","Favorite Color":"Black",
             "Favorite Animal":"Wolf","Weight":"195"}

a = input("""For you I have a riddle. If you can guess my favorite color,
          favorite animal, or favorite musican I will grant you clemency.
          Which will you choose? 1, 2, or 3?""")
a = int(a)
if a == 1:
    g = input("Well then, what's my favorite color?")
    if g == mundo["Favorite Color"]:
        print("Well done maggot. May you remain among gravel til death")
    else:
        print("Fool!")
elif a == 2:
    g = input("Which of these fleshy organisms is the least sufferable to be among?")
    if g == mundo["Favorite Animal"]:
        print("""How often do you sneak gazes upon me? Perverse!
                Take this and begone...deviant""")
    else:
        print("Fool!")
elif a == 3:
    g = input("Whose sounds ring truth and delight in my ears?")
    if g in musicians:
        print("You share a similar spirit. May these aid you in your trials")
    else:
        print("Fool!")
else:
    print("You answered wrong and shall suffer greatly for it")
