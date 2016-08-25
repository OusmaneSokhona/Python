#ce programme permet de dessiner 2cercle(a,b) qui partant du milieux grand a chaque fois
#en cliquant dessus
from upemtk import *
cree_fenetre(400,400)
#dessine un cercle a 
r=1
while r <200 :
	a=cercle(200,200,r)
	attente_clic()
	efface(a)#efface le premier cercle pour
	mise_a_jour()#voir le resultat
	r+=10
r+=10
#dessine un cercle b plus grand que le cercle a 
while r >=1 :
	b=cercle(200,200,r)#dessine un 2e cercle a la place du premier
	attente_clic()
	efface(b)#efface le 2e cercle
	mise_a_jour()#voir le resultat
	r-=10
#j'ai une erreur avec ce programme qui met qu'une fenetre est deja crée lorsque je le teste
#alors qu'il n'avait aucune fenetre d'ouverte	

#au debut je voulait mettre un minuteur pour que le cercle 's'anime' seul sans
	#que l'on soit obligé de cliquer dessus; mais je n'ai pas reussi
	
