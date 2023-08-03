#Un nouvel exemple de type construit est le dictionnaire.

#Les éléments d’une liste ou d’un tuple sont ordonnés et on accéde
# à un élément grâce à sa position en utilisant un numéro qu’on appelle l’indice de l’élément.
#Un dictionnaire en Python va aussi permettre de rassembler des éléments mais ceux-ci seront identifiés par une clé. 
#On peut faire l’analogie avec un dictionnaire de français où on accède à une définition avec un mot.

#Contrairement aux listes qui sont délimitées par des crochets, on utilise des accolades pour les dictionnaires.

#$$$$$#@#######$$$$$$$$$$$##########$$$$$$$$$$#############

# on utilise des accolades {} pour les dictionnaires.

#La syntaxe du dictionnaire se présente comme suit : {clé1:valeur1, clé2:valeur2,...}.

#Le premier élément de la ligne est la clé, suivi d’un deux-points (:), puis de la valeur.

#Lorsqu’on crée un dictionnaire, tout les éléments y compris les clés doivent être uniques.

#Si vous essayez de placer deux éléments ayant la même clé, vous obtenez une erreur.

#Dans le cas contraire, vous pouvez obtenir l’élément à partir de sa clé.

#Voici quelques exemples :

#dico={
 #  "nom":"<NAME>",
#   "prenoms" :("Jean", "Pierre"),
#    }
#print(dico["nom"]) #----> <NAME>

#print(dico["prenoms"]) # ----> ('Jean', 'Pierre')

#On peut aussi accéder directement à la liste en utilisant la notation [] et non ()

#print(dico["prenoms"][1]) # -----> Pierre

####################################################


#########@@@@@@@@@@@@@@@@#######################@@@@@@@@@@@

# On note que la valeur associée à chaque clé doit être séparée de celle précédente

#dans le même style (avec deux points) ; il n'y a pas de virgule entre les paires clé/valeur. 

#Il existe plusieurs manières différentes de créer un dictionnaire dans python.

dico2 = {'nom':'<NAME>', 'age':30} #dictionaire simple

#print(dico2['nom']) #accès au nom via son indice

#print(dico2[('nom')]) #même chose mais cette fois ci nous avons passer une chaîne de caract

print(dico2.get('id', 'not found')) #fonction get permet de récupérer une donnée si elle existe.
#sinon renvoit --None--- ou ecrire le message que vous souhaitez l'afficher comme l'exemple ci-dessus('not found')


#Pour ajouter un nouveau couple clé / valeur dans notre dictionnaire, on fait simplement :

dico2['ville']='Paris'
print(dico2) # -----> {'nom': '<NAME>', 'age': 30, 'ville': 'Paris'}


#Si vous souhaitez supprimer un élément d’un dictionnaire, vous pouvez utiliser la méthode pop()

del dico2['nom']
print(dico2) # ----> {'age': 30, 'ville': 'Paris'}

#Vous pouvez également vouloir retenir seulement certains éléments d’un dictionnaire sans changer celui là entier.
# # قد ترغب أيضًا في الاحتفاظ بعناصر معينة فقط من القاموس دون تغيير المعجم بأكمله.

# Pour cela, vous pouvez utiliser la fonction dict.fromkeys(). 
# Cette fonction prend trois arguments :
# 1-la première correspond à votre dictionnaire initial,
# 2-la deuxième à vos valeurs initiales et 
# 3-la troisième à votre clefs initiales. 

# Elle retourne un autre dictionnaire contenant uniquement ces éléments spécifiques.

dict_test=dico2.fromkeys(['a','b'],5)
print(dict_test)  # ----> {'a': 5, 'b': 5}

#Enfin, vous avez probablement constaté que lorsque vous créez un dictionnaire, tous ses éléments ont été

#initialisés مهيأ sur None. Si vous ne savez pas comment modifier certaines valeurs après avoir définies le dictionnaire,

#vous pouvez toujours utiliser la méthode update(), qui accepte un argument de type dictionnaire.
#Cet argument devra contenir les modifications dont vous souhaitez effectuer.
dico3={'nom':'<NAME>'}

dico3.update({'age':47})
print(dico3) # ----> {'nom': '<NAME>', 'age': 47}
'''
Une autre possibilité consiste à utiliser la méthode setdefault() 
qui sert à mettre à jour un élément existant
dans un dictionnaire ou à insérer un nouvel élément s’il n’existe pas encore. 
La signature de cette méthode ressemble à ceci :
'''

dico3.setdefault('age',69)
print(dico3)

#Dans cet exemple, si age existe déjà dans le dictionnaire, alors la valeur actuelle sera remplace par 80.
#  Sinon, la valeur 80 sera ajoutée à la fin du dictionnaire.

dico4={}
dico4.setdefault('age',69)
print(dico4)
