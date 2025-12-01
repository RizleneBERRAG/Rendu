temp = input("Saisissez la température que vous souhaitez convertir ? (ex: 45F, 102C etc.) : ")

valeur = int(temp[:-1])

unite = temp[-1].upper()

if unite == "F":
    celsius = (valeur - 32) * 5/9
    print("La température en Celsius est de", round(celsius), "degrés.")

elif unite == "C":
    fahrenheit = (valeur * 9/5) + 32
    print("La température en Fahrenheit est de", round(fahrenheit), "degrés.")

else:
    print("Unité inconnue. Utilisez C ou F.")
