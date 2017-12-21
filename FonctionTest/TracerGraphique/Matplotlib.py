import numpy as np
import csv

import matplotlib.pyplot as plt

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


# FONCTIONS QUI PERMETTENT DE LIRE ET D'ECRIRE LES DONNES DES FICHIERS CHOISIS DANS UNE LISTE D'OBJET CORRESPONDANT AUX MESURES:

# fonction qui lit et recupere les donnes des fichiers choisis
def recuperation_donnees():
	global listeMesures

	# Pour chaque fichiers envoyés par l'utilisateur
	for fichier in listeFichiers:
		# Ouvre le fichier est indique que les valeurs sont séparées par des tabulations
		with open(fichier, newline = '') as csvfile:
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
						compteur = 11
						while (compteur < len(ligne1) - 2):
							mesuresU.append(float(ligne1[compteur]))
							mesuresI.append(float(ligne2[compteur]))
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




# liste qui contiendra tous les choix de l'utilisateur
listeFichiers = ['test.txt', 'test2.txt']


# Liste qui contient toutes les mesures séléctionnés par l'utilisateur
listeMesures = []

# Envoie à la fonction qui va lire les fichiers et créer des objets contenant toutes les informations de nos mesures
recuperation_donnees()

# LES DONNES SONT RECUPEREES ET PRETE A ETRE UTILISEE
#-------------------------------------------------------------------------

maxX = 0
minY = 0

for mesure in listeMesures:

	plt.plot(mesure.mesure[0], mesure.mesure[1], label = mesure.nom)

	plt.xlabel('Tension [V]')
	plt.ylabel('Courant [mA]')

	plt.legend()

plt.gca().invert_yaxis()
plt.grid(axis='both')
plt.show()


for mesure in listeMesures:
	puissance = mesure.mesure[0] * (mesure.mesure[1]/1000)


	newMinY = min(puissance)
	if (newMinY < minY):
		minY = newMinY

	plt.plot(mesure.mesure[0], puissance, label = mesure.nom)

	plt.xlabel('Tension [V]')
	plt.ylabel('Puissance [W]')

	plt.legend()

plt.gca().invert_yaxis()
axes = plt.gca()
axes.set_ylim([0, minY - 0.001])
plt.grid(axis='both')
plt.show()

