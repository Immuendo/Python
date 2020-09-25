num = [17,19,3,11,40,61,74,13,95]
n = input("Guess a number")

while n != "q":
    n = int(n)
    if n in num:
        print("You got one right,but there's still more.")
    else:
        print("Poor Fool, your debt is due!")
    n = input("Guess a number")
    
