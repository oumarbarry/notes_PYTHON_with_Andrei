nom = 'barry '
prenom = "oumar"

reponse_html = """ 
    <html>
        <body>
            <h1>Ceci est le html renvoye par le serveur comme reponse au navigateur</h1>
        </body>
    </html>
"""
print("bonjour je m'appelle: {} ".format(prenom)) #concatenation
print("bammom "*4)
print(f"bonjour je le serveur et voici le html que je renvoie : {reponse_html}")

soleil = '\tc\'est une magnifique journee de janvier \\ que nous avons aujourd\'hui\n\n\n'

#les strings sont IMMUTABLES, c-a-d
    # mot_de_passe = '012345'
    # mot_de_passe[4]= '@' //erreur: impossible car les strings sont IMMUTABLES
    # mot_de_passe = '0123@5' //OK


#LE DECOUPAGE [position_debut : position_fin : saut]
numero_bancaire = '0123456789'
print(numero_bancaire)
print( numero_bancaire[:] )
print( numero_bancaire[2:6] )
print( numero_bancaire[:5] )
print( numero_bancaire[4:] )
print( numero_bancaire[-1:-5] )
print( numero_bancaire[::-1] )
print( numero_bancaire[::-2] )

#conversion de type
age = int( input("Quel est ton annee de naissance ? ") )
print( f"tu es donc agé de {2020-age} ans" )

print( str(58) )
print( float(9) )
print( int('1998') )
print( int(3.2) )

#les fonctions et methodes propres aux strings
print( len('abcdefghijk') )
soleil.capitalize()
soleil.upper()

phrase = "BONJOUR ici et là et ici"
phrase.lower()
phrase.find('ici')
phrase.replace("là", "ici")