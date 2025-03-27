''''
Modifier maintenant votre fonction call de sorte qu’elle puisse appeler une fonction qui prend des paramètres positionnels et qui renvoie une valeur. 
On doit, par exemple, pouvoir écrire le code suivant :
# À compléter ...
def add(a, b): return a + b
print(call(add, 2, 9))
# Affiche ’11’
'''

def add(a, b): 
    return a + b

def call(fct, *args):
    return fct

print(call(add, 2, 9))