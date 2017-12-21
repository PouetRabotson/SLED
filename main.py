# Programme permettant de traiter les données obtenues a l'aide du SLED Simulator
# Version brut et sans option
# A améliorer en ajoutant des fonctions au programme au fur et à mesure

#Tous les imports nécessaire au programme
from tkinter import filedialog
from tkinter import *
import os

import numpy as np
import csv

# Objet contenant toutes les informations relatives à une mesure
class Mesure:

	def __init__(self, nom, date, voc, isc, pm, ff, rp, rs, vm, im, mesuresU, mesuresI):
		self.nom = nom
		self.date = date
		self.voc = float (voc)
		self.isc = float (isc)
		self.pm = float (pm)
		self.ff = float (ff)
		self.rp = float (rp)
		self.rs = float (rs)
		self.vm = float (vm)
		self.im = float (im)
		self.mesure = np.array((mesuresU, mesuresI))

	def ajouterAListeMesures(self):
		listeMesures.append(self)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# FONCTIONS RELATIVES A LA SELECTION DE FICHIER PAR L'UTILISATEUR

# Création de la fenêtre utilisateur pour la séléction des fichiers
def creation_fenetreChoixFichier():
	global fenetreChoixFichier

	# Créer une fenêtre Tkinter
	fenetreChoixFichier = Tk()

	# Création de la frame qui indiquera les fichiers séléctionnés
	creation_frame_message()
	Label(message, text = "Séléctionner les fichiers").pack(side = RIGHT)

	# Création de la Frame qui contiendra les boutons d'actions
	bouton = Frame(fenetreChoixFichier, borderwidth = 5, padx = 20, pady = 20)
	bouton.pack(fill = "both", expand = "yes", side = LEFT)

	# Bouton qui permet de séléctionner les fichiers désirés
	boutonParcourir = Button(bouton, text = "Parcourir", command = choix_fichier)
	boutonParcourir.grid(row = 1, column = 1, pady = 5, padx = 5)

	# Bouton qui permet de Reset la séléction des fichiers
	boutonReset = Button(bouton, text = "Reset", command = reset_choixFichier)
	boutonReset.grid(row = 1, column = 2, pady = 5)

	# Bouton qui permet d'envoyer les résultats pour la suite du programme
	boutonEnvoyer = Button(bouton, text = "Envoyer", command = envoyer_fichiers)
	boutonEnvoyer.grid(row = 2, column = 1, columnspan = 2)

	# Si la fen^tre est fermée, termine le programme
	fenetreChoixFichier.protocol("WM_DELETE_WINDOW", sys.exit)

	# Affiche la fenetre de selection des fichiers tant qu'elle n'est pas fermée par une action de l'utilisateur
	fenetreChoixFichier.mainloop()

# Fonction qui gère le choix des fichiers par l'utilisateur
def choix_fichier():
	global listeFichiers

	# Enregistre les fichiers choisis par l'utilisateur dans une liste 
	choixFichier = filedialog.askopenfiles(filetypes = FILETYPES, parent = fenetreChoixFichier, title = "Séléction d'un fichier")

	print ('Ajout de ' + str(len(choixFichier)) + ' fichier(s)')

	# Ajoute le contenu de choixFichier dans la liste listeFichiers
	listeFichiers.extend(choixFichier)

	print ('Il y a ' + str(len(listeFichiers)) + ' fichier(s) au total')

	# Appelle la fonction pour mettre à jour la fenêtre
	update_fenetre()

# Fonction permettant de mettre à jour la fenêtre de séléction des fichiers
def update_fenetre():
	# détruit la frame du message, puis la recré
	message.destroy()
	creation_frame_message()

	# Si la liste des fichiers contient quelques chose
	if (listeFichiers):
		# Affiche le nom de tous les fichiers séléctionnés
		for fichier in listeFichiers:
			Label(message, text = fichier.name).pack()
	else : # Si la liste des fichiers est vide
		Label(message, text = "Erreur, aucun fichier choisi").pack()

	# Met le message à jour
	message.update()

# Création de la frame qui contiendra les messages des fichiers séléctionnés
def creation_frame_message():
	global message

	# Créer la Frame contenant le message, et la place dans notre fenêtre
	message = Frame(fenetreChoixFichier, borderwidth = 2, relief = GROOVE, padx = 20, pady = 20)
	message.pack(fill = "both", expand = "yes", side = RIGHT)

# Fonction qui permet de reset les choix de fichiers par l'utilisateur
def reset_choixFichier():
	global listeFichiers, message

	# Efface le contenu de la listeFichiers
	listeFichiers = []

	# Détruit le message, puis en recrée un pour annoncer le reset
	message.destroy()
	creation_frame_message()
	Label(message, text = "Reset, Séléctionner les fichiers").pack()

	# Met le message à jour
	message.update()

# Gère l'envoie des fichiers pour la suite du programme
def envoyer_fichiers():
	# Si listeFichiers contient quelques chose
	if (listeFichiers):
		fenetreChoixFichier.destroy() # Ferme la fenêtre de séléction de fichier et continue le programme
	else: # Si listeFichiers est vide, mais la fenêtre à jour
		update_fenetre()

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# FONCTIONS QUI PERMETTENT DE LIRE ET D'ECRIRE LES DONNES DES FICHIERS CHOISIS DANS UNE LISTE D'OBJET CORRESPONDANT AUX MESURES:

# fonction qui lit et recupere les donnes des fichiers choisis
def recuperation_donnees():
	global listeMesures

	# Pour chaque fichiers envoyés par l'utilisateur
	for fichier in listeFichiers:
		# Ouvre le fichier est indique que les valeurs sont séparées par des tabulations
		with open(fichier.name, newline = '') as csvfile:
			fichiercsv = csv.reader(csvfile, delimiter='\t')

			# Lance une boucle qui s'arrête quand l'erreur StopIteration intervient
			while 1:
				# Regarde si la ligne suivant existe
				try: 
					ligne1 = next(fichiercsv)
					ligne2 = next(fichiercsv)

					# Vérifie que les deux lignes ont le même problèmes
					if (len(ligne1) == len(ligne2)):
						# On initialise les listes qui contiendront toutes les valeurs mesurée de nos tensions et courants
						mesuresU = []
						mesuresI = []

						# Ajoute toutes les valeurs des mesures de tensions et courant dans nos listes dédiées à cet usage
						compteur = 10
						while (compteur < len(ligne1) - 1):
							mesuresU.append(ligne1[compteur])
							mesuresI.append(ligne2[compteur])
							compteur += 1
						del compteur
						
						# Initialise l'objet mesure avec toutes les informations nécessaires
						ma_mesure = Mesure(ligne2[0], ligne2[1], ligne2[2], ligne2[3], \
							ligne2[4], ligne2[5], ligne2[6], ligne2[7], ligne2[8], ligne2[9], mesuresU, mesuresI)

						# Ajoute la mesure traitée à la listes des mesures
						ma_mesure.ajouterAListeMesures()

					else: # Si les deux lignes n'ont pas le même nombre de termes
						print ("ERROR")

				except StopIteration: # Si la prochaine ligne testée est vide, on quitte la boucle
					break

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# FONCTIONS SUR LE CHOIX DU FICHIER DE DESTINATION PAR L'UTILISATEUR

# Fonction gérant le choix du fichier ou l'on souhaite enregistrer les données
def retry():
	global fenetreDestination
	fenetreDestination.destroy()

def choix_destination():
	global fichierDestination

	# Boucle tant qu'une des conditions de sorties ne sont pas bonnes 
	# fichierDestination choisi ou alors fermeture du programme
	while 1:
		# On crée une fenêtre qui est cachée
		fenetreDestination = Tk()
		fenetreDestination.withdraw()

		# On demande a l'utilisateur de choisir un fichier de destination. On ajoute l'extension .txt si il ne donne pas d'extension lui même!
		fichierDestination = filedialog.asksaveasfilename(filetypes = FILETYPES, defaultextension = '.txt')

		# Si un fichier de destination a été choisi
		if (fichierDestination):
			# On ouvre ce fichier et on quitte la boucle
			fichier = open(fichierDestination, 'w')
			break

		else: # Si aucun fichier de destination n'a été choisi
			# On fait réapparaitre la fenêtre au premier plan
			fenetreDestination.deiconify()

			# On indique un message d'erreur
			Label(fenetreDestination, text="Une erreur s'est produite").pack(side = TOP, pady = 20)

			# Bouton qui permet de relancer le choix d'un fichier de destination
			Button(fenetreDestination, text = "Réessayer", command = retry).pack(side = LEFT)

			# Bouton qui quitte le programme
			Button(fenetreDestination, text = "Quitter", command = sys.exit).pack(side = RIGHT)

			# Si la fenêtre est fermé d'une autre façon, quitte le programme
			fenetreDestination.protocol("WM_DELETE_WINDOW", sys.exit)

			# Garde la fenêtre affichée
			fenetreDestination.mainloop()
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# FONCTIONS PERMETTANT DE RECRIRE LES DONNES DANS UN FICHIER TXT.

def ecrire_txt():
	# Ouvre le fichier ou l'on veut écrire notre nouveau dossier
	with open(fichierDestination, 'w', newline = '') as csvfile:
		fichiercsv = csv.writer(csvfile,delimiter='\t')

		for mesure in listeMesures:	
			ligne1 = ['comment', 'date time', 'Voc(V)', 'Isc(mA)', 'Pm(mW)', 'FF(%)', 'Rp(Ohm)', 'Rs(Ohm)', 'Vm(V)', 'Im(mA)']
			ligne1.extend(mesure.mesure[0])

			ligne2 = [mesure.nom, mesure.date, mesure.voc, mesure.isc, mesure.pm, mesure.ff, mesure.rp, mesure.rs, mesure.vm, mesure.im]
			ligne2.extend(mesure.mesure[1])

			# On écrit nos deux lignes
			fichiercsv.writerow(ligne1)
			fichiercsv.writerow(ligne2)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# CORPS DU PROGRAMME

# Permet de choisir le type de fichier que l'utilisateur peut séléctionner
FILETYPES = [("text files", "*.txt")]

# liste qui contiendra tous les choix de l'utilisateur
listeFichiers = []


# Envoie a la suite de fonctions qui permettent a l'utilisateur de séléctionner des fichiers à traiter
creation_fenetreChoixFichier()

# L'UTILISATEUR A SELECTIONNER TOUS LES FICHIERS A TRAITES
#-------------------------------------------------------------------------

# Liste qui contient toutes les mesures séléctionnés par l'utilisateur
listeMesures = []

# Envoie à la fonction qui va lire les fichiers et créer des objets contenant toutes les informations de nos mesures
recuperation_donnees()

# LES DONNES SONT RECUPEREES ET PRETE A ETRE UTILISEE
#-------------------------------------------------------------------------

choix_destination()


ecrire_txt()
