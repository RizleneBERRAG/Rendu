chaine = input("Saisissez une chaîne : ")

nb_lettres = 0
nb_chiffres = 0

for char in chaine:
    if char.isalpha():     
        nb_lettres += 1
    elif char.isdigit(): 
        nb_chiffres += 1

print("Lettres", nb_lettres)
print("Chiffres", nb_chiffres)
