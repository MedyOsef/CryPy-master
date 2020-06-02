entree = input("Chaine a traiter : ")
cle = input("Cle a utiliser : ")
sortie, i = "", 0
for caract in entree:
    sortie = sortie + chr((ord(caract) - ord(cle[i])) % 256)
    i = i + 1
    if i > len(cle) - 1:
        i = 0
print(sortie)