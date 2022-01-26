#intro
ma_liste = [1,3,'a','x',True, None]
print( ma_liste[5] )
ma_liste[4] = False

#le decoupage de listes
ordinateurs = ['lenovo', 'hp', 'dell', 'asus', 'mac']
print( ordinateurs[3:] )

#le depaquetage de listes
a, b, c, *other, d = [1,2,3,4,5,6,7,8,9]

#les matrices et plus encore
matrice = [['a', 'b', 'c'], [1, 2, 3]]
print( matrice[0][2] )


#les methodes des listes
#ajout
ordinateurs.append() #ajoute a la fin de la liste
#ordinateurs.insert(3, 'samsung') #ajoute a la position specifié
ordinateurs.extend(['test1', 'test2']) #pour ajouter une liste a la fin de la liste appelante
				
#suppression
ordinateurs.pop() #supprime le dernier element de la liste
    #contrairement aux autres methodes de liste, 
        # pop() renvoie une valeur, celle de l'element supprimé
ordinateurs.pop(0) #supprimer a la position specifié
ordinateurs.remove('hp') #supprimer la premiere valeur correspondante rencontree
ordinateurs.clear() #effacer tout le contenu de la liste

#bonus
print( 'hp' in ordinateurs ) #lle mot-cle 'in' permet de verifier si 'ordinateurs' contient 'hp'
ordinateurs.sort(reverse=False) #trie la liste et modifie la variable appelante
sorted(ordinateurs) #cette fonction trie aussi mais renvoie une copie de la liste 
ordinateurs.copy() #copie la liste appelante et renvoie une nouvelle liste
