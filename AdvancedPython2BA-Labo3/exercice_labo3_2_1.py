''''
Définir une fonction call qui reçoit en paramètre une fonction sans paramètres qui ne renvoie pas de valeur et qui l’appelle. 
On doit, par exemple, pouvoir écrire le code suivant :
# À compléter ...
def hello(): print(’hello’)
call(hello)

# Affiche ’hello’
'''
def hello(): 
    print('hello')
                   
def call(fct):
    return fct

call(hello())