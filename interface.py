                                  ###################################################
                                  #########        Chiffrément de texte     #########
                                  #########  Aléatoire simple et efficace   #########
                                  #########           By MedyOsef           #########
                                  #########    porgomedyfaycal@gmail.com    #########
                                  ###################################################


from tkinter import *
from pyperclip import copy

def encryt():
    entree = champ_texte1.get(1.0, END)
    cle = clef_entry.get()
    sortie, i = "", 0
    for caract in entree:
        sortie = sortie + chr((ord(caract) - ord(cle[i])) % 256)
        i = i + 1
        if i > len(cle) - 1:
            i = 0
    print(sortie)


def decipher():
    entree = input()
    cle = input()
    sortie, i = "", 0
    for caract in sortie:
        sortie = sortie + chr((ord(caract) + ord(cle[i])) % 256)
        i = i + 1
        if i > len(cle) - 1:
            i = 0
        return sortie

"""
def copy():
    


def paste():


"""

window = Tk()
window.title("Crypy         by MedyOsef ")
window.geometry("955x620")
# window.maxsize(950, 665)
# window.minsize(950, 655)
# window.iconbitmap('python.ico')
window.config(background='#41B7FF')

# creer la frame principale:
frame = Frame(window)
# creation de petite frame
frame2 = Frame(window)

# creation d'image:
width = 170
height = 130
image = PhotoImage(file="lunetteEgypt.png").zoom(10).subsample(33)
canvas = Canvas(frame, width=width, height=height, background='#41B7FF', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creation d'icone
image2 = PhotoImage(file='letter.png').zoom(15).subsample(28)
canvas3 = Canvas(frame2, width=60, height=60, background='#41B7FF', bd=0, highlightthickness=0)
canvas3.create_image(30, 30, image= image2)
canvas3.pack()

# afficher la frame2
frame2.place(x=60, y=268)


# afficher la Frame
frame.place(x=770, y=230)

# creation de texte:
canvas2 = Canvas(window, width=150, height=74, background='#41B7FF', highlightthickness=0)
txt = canvas2.create_text(75, 30, text="CryPy", font=("Comic Sans MS", 40), fill="blue")
canvas2.place(x=765, y=360)

# creation de champs/entree/input
clef_entry = Entry(window, font=('Comic Sans MS', 20), bg='#16293d', fg='white', show="•")
clef_entry.place(x=110, y=280)


# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""(creation des boutons:)""""""""""""""""""""""""""""""""""
# premier bouton (Chiffrer):
bout1_chiffrer = Button(window, text="Chiffrer", font=('Helvetica', 15), bg='#16d9FF', fg='white', command=encryt)
bout1_chiffrer.pack(expand=YES)
bout1_chiffrer.place(x=800, y=50, width=120, height=43)

# creation de second bouton (Déchiffrer)
bout2_dechiffrer = Button(window, text="Déchiffrer", font=('Helvetica', 15), bg='#16d9FF', fg='white')
bout2_dechiffrer.pack(expand=YES)
bout2_dechiffrer.place(x=800, y=130, width=120, height=43)

# creation du troisième Bouton (Coller):
bout3_coller = Button(window, text="Coller", font=('Helvetica', 15), bg='#16d9FF', fg='white')
bout3_coller.pack(expand=YES)
bout3_coller.place(x=600, y=280, width=120, height=43)


# creation de quatrième bouton (Copier):
bout4_copier = Button(window, text='Copier', font=('Helvetica', 15), bg='#16D9FF', fg='white')
bout4_copier.pack(expand=YES)
bout4_copier.place(x=755, y=530, width=120, height=43)

# """""""""""""""""""""""""""""""""""""""""""""""'''(les Zones d'affichage)"""""""""""""""""""""""""""""""""""""""""""""
# Zone d'affichage 1 :
champ_texte1 = Text(window, height=9, width=73, bg='#16293d', font=('segoe print', 10), fg='light grey', wrap=WORD)
champ_texte1.grid(row=8, column=3, pady=19)
champ_texte1.place(x=10, y=50)

# Zone d'affichage 2 :
champ_texte2 = Text(window, height=9, width=73, bg='#16293d', font=('segoe print', 10), fg='light grey', wrap=WORD)
champ_texte2.grid(row=8, column=3, pady=19)
champ_texte2.place(x=10, y=360)

#champ_texte2.insert(END, "Medy")
#champ_texte2.insert(END, "hahah tu faui quoi ojdd dfvfr")
# """"""""""""""""""""""""""""""""""""""""""""""(Menu)""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# creation d'une barre de Menu
menu_bar = Menu(window)
# creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fentre pour ajouter cette menu bar
window.config(menu=menu_bar)
# """""""""""""(affichage de la fenêtre)"""""""""""""""
window.mainloop()

"""
je doit faire les command copier et coller la prochaine fois que je vien ici avec pyperclip
"""
