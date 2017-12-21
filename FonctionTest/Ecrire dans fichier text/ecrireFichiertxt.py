import numpy as np
import csv

# Définit l'objet d'une mesure
class Mesure:
	def __init__(self, nom, date, Umax, valeurU, valeurI):
		self.nom = nom
		self.date = date
		self.Umax = float(Umax)

		self.mesure = np.array((valeurU, valeurI))

valeurU = [i for i in np.arange(0,10,0.5)]
valeurI = [i for i in np.arange(10, 110, 5)]

listeMesures = []

ma_mesure = Mesure("patate", "12.12.2017", '153', valeurU, valeurI)

valeurU = [i for i in np.arange(10,20,0.5)]
valeurI = [i for i in np.arange(100, 210, 5)]

listeMesures.append(ma_mesure)

ma_mesure2 = Mesure('Tartine', '05.11.2918', '12', valeurU, valeurI)
listeMesures.append(ma_mesure2)


# Ouvre le fichier ou l'on veut écrire notre nouveau dossier
with open('test.txt', 'w', newline = '') as csvfile:
			fichiercsv = csv.writer(csvfile,delimiter='\t')

			for ma_mesure in listeMesures:
				# Créer une liste contenant toutes les infos de la ligne 1
				ligne1 = ['Nom', 'Date', 'Umax']
				ligne1.extend(ma_mesure.mesure[0])

				# Même chose pour la ligne 2
				ligne2 = [ma_mesure.nom, ma_mesure.date, ma_mesure.Umax]
				ligne2.extend(ma_mesure.mesure[1])

				# On écrit nos deux lignes
				fichiercsv.writerow(ligne1)
				fichiercsv.writerow(ligne2)
 



