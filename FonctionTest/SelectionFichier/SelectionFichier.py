#Programme permettant a l'utilisateur de selectionner un ou plusieurs fichier .txt à traiter
#Il faudrait créer une fonction qui permet la création de la fenêtre, actuellement elle apparait deux fois dans le code

from tkinter import filedialog
from tkinter import *
import os

#Limite le type de fichier que peux choisir l'utilisateur à des .txt
FILETYPES = [("text files", "*.txt")]

listeFichiers = []


def choix_fichier():
    fichier = filedialog.askopenfiles(filetypes = FILETYPES,parent = fenetre1, initialdir="/", title="Séléction d'un fichier")

    print('Ajout de ' + str(len(fichier)) + ' fichier(s)') 
    
    for eachFichier in fichier:
        listeFichiers.append(eachFichier)

    print('Il y a ' + str(len(listeFichiers)) + ' fichier(s) au total')

    update_fenetre()

def creation_frame_message():
    global message
    
    message = Frame(fenetre1, borderwidth=2, relief=GROOVE,padx = 20, pady = 20)
    message.pack(fill="both", expand="yes")


#Mise a jour de l'affichage de la frame de la fenêtre
def update_fenetre():
    global message

    #On détruit la fenêtre pour la reconstruire.
    message.destroy()

    creation_frame_message()
    

    #Vérifie que la liste contient bien un fichier
    try:
        listeFichiers[0]

        # Créer un label pour chaque fichier
        for fichier in listeFichiers:
            Label(message, text = fichier.name).pack()

            
    except IndexError: # Sinon affiche qu'aucun fichier n'a été choisi
        Label(message, text="Erreur, aucun fichier choisi").pack()
        
    #Met la fenêtre à jour
    message.update()

#Création de l'interface utilisateur
fenetre1 = Tk()
bouton1 = Button(fenetre1, text="parcourir", command = choix_fichier)
bouton1.pack()
creation_frame_message()
Label(message, text="aucun fichier choisi").pack()

fenetre1.mainloop()

