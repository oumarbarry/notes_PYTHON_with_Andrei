""" TOUS LES TYPES DE DONNEES EN PYTHON:
    #numbers
    #boolean
    #none
    #string
    #list
    #dict
    #tuple
    #set
    #creer nos propres classes
    #utiliser les classes crees par les autres 
"""
##############################################################################
#numbers
    #int, float
#les operateurs arithmetiques de bases
print(f"add {type(2+4)}")
print(f"sous {type(2-4)}")
print(f"mult {type(2*4)}")
print(f"div {type(2/4)}")
#les autres operateurs arithmetiques
print(f"puiss {type(2**4)}")
print(f"div entiere {type(2//4)}")
print(f"modulo {type(2%4)}")
#les autres operateurs : +=, -=, *=, /=, **=, //=, %=
num = 50
num += 1
print(f"num {num}")

#la priorite des operateurs
#expression vs declaration
   
#conversion binaire-entier
print( bin(4) )
print( int('0b10111', base=2) )
#complex
salimatou = complex(3, 4)
print(salimatou)

#les fonctions mathematiques en Python
import math
abs(-1)
pow(20, 3)
math.sqrt(5)
math.log10(8)
