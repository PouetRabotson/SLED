from tkinter import filedialog
from tkinter import *

# Affiche le format du fichier qui sera sauvegardé 
FILETYPES = [("text files", "*.txt")]

# Appeler par le bouton réessayer
def retry():
	# Détruit la fenêtre, ce qui permet de recommencer la boucle
	global root
	root.destroy()

# Boucle tant qu'une des conditions de sorties ne sont pas bonnes 
# fichierDestination choisi ou alors fermeture du programme
while 1:
	# On crée une fenêtre qui est cachée
	root = Tk()
	root.withdraw()

	# On demande a l'utilisateur de choisir un fichier de destination. On ajoute l'extension .txt si il ne donne pas d'extension lui même!
	fichierDestination = filedialog.asksaveasfilename(filetypes = FILETYPES, defaultextension = '.txt')

	# Si un fichier de destination a été choisi
	if (fichierDestination):
		# On ouvre ce fichier et on quitte la boucle
		fichier = open(fichierDestination, 'w')
		break

	else: # Si aucun fichier de destination n'a été choisi
		# On fait réapparaitre la fenêtre au premier plan
		root.deiconify()

		# On indique un message d'erreur
		Label(root, text="Une erreur s'est produite").pack(side = TOP, pady = 20)

		# Bouton qui permet de relancer le choix d'un fichier de destination
		Button(root, text = "Réessayer", command = retry).pack(side = LEFT)

		# Bouton qui quitte le programme
		Button(root, text = "Quitter", command = sys.exit).pack(side = RIGHT)

		# Si la fenêtre est fermé d'une autre façon, quitte le programme
		root.protocol("WM_DELETE_WINDOW", sys.exit)

		# Garde la fenêtre affichée
		root.mainloop()

# Ecrit dans le fichier
fichier.write("Salut")

# Ferme le fichier
fichier.close()