def test_distinct(sequence):
    return len(sequence) == len(set(sequence))

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))


#Écrivez une fonction Python qui prend une séquence de nombres et détermine si tous les nombres sont différents les uns des autres.
#print(test_distinct([1, 5, 7, 9]))
#print(test_distinct([2, 4, 5, 5, 7, 9]))
#>>True
#>>False

#set -> enlève les doublons automatiquement
#def test_distinct(sequence) -> création de la fonction "test_distinct" qui reçois une sequence(liste)
#set(sequence) retire les doublons de la liste
#len(sequence) donne le nombre d'éléments avant le set 
#len(set(sequence)) donne le nombre d'éléments après le set
#== Compare les deux résultats