def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

import random
lista=["Aeroport","Acadele","oaie","balena","cuvant","potrivit","python"]
# above you have to insert a few words that are chosen random to be guessed by the player
i=random.randint(0,len(lista)-1)
cuvant=lista[i]
print("The word has {} letters".format(len(cuvant)))
cuvant_de_ghicit=''
for i in range(len(cuvant)):
    cuvant_de_ghicit=cuvant_de_ghicit+'_'
greseli=0
while '_' in cuvant_de_ghicit and greseli<8:
    print(cuvant_de_ghicit)
    litera=input("Insert a character:")
    if litera not in cuvant:
        greseli+=1
        if 8-greseli !=0:
            print("You have {} lives".format(8-greseli))
    else:
        while litera in cuvant.lower():
            pozitie=cuvant.lower().find(litera)
            cuvant=change_char(cuvant,pozitie,"_")
            cuvant_de_ghicit=change_char(cuvant_de_ghicit,pozitie,litera)
if greseli==8:
    print("You didn't guess the word")
else:
    print("Well done, you guessed the word")


