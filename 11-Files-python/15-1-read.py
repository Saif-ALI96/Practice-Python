# en python on peut acceder aux autre fichers pour lire ou ecrire etc...

files = open('files-in-python/read.txt','r')
#ouverture du fichier read.txt en mode lecture (r) et stockage dans la variable text
# print (files.readable()) -----> True 


#.readline()   #lecture d'une ligne seulement avec readline(), puis
#stockage dans une nouvelle variable line
'''
#print(files.readlines()) #lecture de toutes les lignes du fichiers
# ------> #['hello world \n', 'i am here for learning python\n', 'number \n', 'string\n', 'boolean']
'''
#  .read()     # lecture de fichier tel qu'il est 

# pour avoir le resultat l'un apres l'autre , on peut utiliser le loop for 
#par exemple:

for loop in files.readlines():
    print(loop)
    # -----> hello world 

# i am here for learning python

# number 

# string

# boolean

files.close()


