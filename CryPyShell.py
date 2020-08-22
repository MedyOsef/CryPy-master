# conding: utf-8


print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ ")
print("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌")
print("▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌")
print("▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌")
print("▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌")
print("▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
print("▐░▌          ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ")
print("▐░▌          ▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌     ")
print("▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌      ▐░▌     ▐░▌               ▐░▌     ")
print("▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌     ")
print(" ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀                 ▀ ")
# """"""""""""""""""""""""""""""""""""""""""""#
#                                             #
#                                             #
#   Ce le Programme sans interface graphique #
#                                             #
#                                             #
#"""""""""""""""""""""""""""""""""""""""""""""#

while True:

    entree = input("Chaine a traiter : ")

    cle = input("Cle a utiliser : ")
    operation = input("Coder / decoder ? (1/2)")
    sortie = ""
    i = 0
    for caract in entree:  # parcours de la chaîne à traiter / route of the chain to be treated
        if operation == "1":  # chiffrement / # encryption
            sortie = sortie + chr((ord(caract) + ord(cle[i])) % 256)
            i = i + 1  # parcours de la clé / key path
            if i > len(cle) - 1:
                i = 0  # fin de clé atteinte, on repart au début /  end of key reached, we start at the beginning
        elif operation == "2":  # déchiffrement / decryption
            sortie = sortie + chr((ord(caract) - ord(cle[i])) % 256)
            i = i + 1
            if i > len(cle) - 1:
                i = 0
    print(sortie)
