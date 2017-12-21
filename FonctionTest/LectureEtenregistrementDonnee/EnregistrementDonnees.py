import numpy as np
import csv


# Création de l'objet d'une mesure
class Mesure:

	#Contient toutes les valeurs relatives à une mesure
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

	# Affiche les valeurs correspondant à la mesure
	def afficherValeurs(self):
		print ('Commentaire : ', self.nom)
		print ('Date 		: ', self.date)
		print ('Voc[V]		: ', self.voc)
		print ('Isc[mA] 	: ', self.isc)
		print ('Pm[mW] 		: ', self.pm)
		print ('Ff[%] 		: ', self.ff)
		print ('Rp[ohm] 	: ', self.rp)
		print ('Rs[ohm] 	: ', self.rs)
		print ('Vm[V] 		: ', self.vm)
		print ('Im[mA] 		: ', self.im)

	# Affiche la liste de toutes les mesures de U et I
	def afficherListeMesureUV(self):
		print(self.mesure)

	# Ajoute la mesure en cours à la liste de toutes les mesure
	def ajouterAListeMesures(self):
		listeMesures.append(self)


# Contient la liste de tous les fichiers à traiter
listeFichiers = ['fichierTest1.txt', 'fichierTest2.txt']

# Contient les différentes mesures décomposées de chaques fichiers
listeMesures = []

for fichier in listeFichiers:
	# Ouvre le fichier, puis l'utilise comme un csv
	with open(fichier, newline='') as csvfile:
		fichiercsv = csv.reader(csvfile, delimiter='\t')
		
		while 1:
			try:
				# Charge le contenu des deux premières lignes
				ligne1 = next(fichiercsv)
				ligne2 = next(fichiercsv)

				# Initialise des listes vides puis les remplies avec les mesures UI
				mesuresU = []
				mesuresI = []

				m = 10
				while (m < len(ligne1) - 1):
					mesuresU.append(ligne1[m])
					mesuresI.append(ligne2[m])
					m += 1
				del m 
				
				# Initialise l'objet mesure avec toutes les informations nécessaires
				ma_mesure = Mesure(ligne2[0], ligne2[1], ligne2[2], ligne2[3], \
					ligne2[4], ligne2[5], ligne2[6], ligne2[7], ligne2[8], ligne2[9], mesuresU, mesuresI)

				# 
				ma_mesure.ajouterAListeMesures()

			except StopIteration:
				break

print (len(listeMesures))
listeMesures[1].afficherValeurs()

