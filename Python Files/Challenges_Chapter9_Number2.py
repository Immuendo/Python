import os


# ans = input("What's something you like?")
with open('ans.txt','w+') as f:
    ans = input("What's something you like?")
    f.write(ans)

"""
a = input("What's something you like?")
f = open("ans.txt","w+")
f.write(a)
f.close()
"""

with open("ans.txt","r") as v:
    print(v.read())

    
my_list = [["Top Gun", "Risky Business", "Minority Report"],
           ["Titanic","The Revenant","Inception"],
           ["Training Day","Man on Fire","Flight"]]

