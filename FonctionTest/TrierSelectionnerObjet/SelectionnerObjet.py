from tkinter import *

#Création d'une classe
class Mesure:
	def __init__(self, nom, valeur):
		self.nom = nom
		self.valeur = valeur

		# Sers a savoir si l'objet est voulu ou non
		self.active = False

# Se déroule lorsque l'on clique sur le bouton envoyer
def send():	
	# Passe tous les objets
	a = 0
	while (a < len(listeObjet)):
		# Modifie la valeur de active de tous les objets en fonctions du choix de l'utilisateur
		listeObjet[a].active = bool(listeVar[a].get())
		a += 1
	del a

	# Ferme la fenêtre
	fenetre.destroy()

# Création de 3 objets fictifs
test = Mesure('test', 12)
test2 = Mesure ('patate', 142)
test3 = Mesure("Pantaoufle", 0)

listeObjet = [test, test2, test3]

# Contient la liste des éléments nécessaires aux checksbutton
listeVar = []
listeBouton = []

#Création de la fenêtre graphique
fenetre = Tk()


# Pour tous les objets
a = 0
for objet in listeObjet:
	# Créer un booléen qu'on ajoute dans notre liste
	var = BooleanVar() 
	listeVar.append(var)

	# Création des éléments du bouton, renvoie les Booléens True ou False en fonction du choix de l'utilisateur
	listeBouton.append(Checkbutton(fenetre, text = objet.nom, variable = listeVar[a] , offvalue = False, onvalue = True))
	listeBouton[a].select() #Case cochée au départ
	listeBouton[a].pack()
	a += 1
del a


# Bouton qui sert à envoyer les choix sélectionnés
boutonEnvoyer = Button(fenetre, text= "Envoyer", command = send)
boutonEnvoyer.pack()

#Bouton pour quitter la fenêtre
boutonQuitter = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
boutonQuitter.pack()

fenetre = mainloop()

# Affiche tous les objets séléctionnés
for objet in listeObjet:
	if (objet.active):
		print (objet.nom)
