#Aujourd'hui, on va voir le function split() pour mettre le contenu 
#de string dans un list en python 

#le function// .split() -----> pour separer les objets comme dands le tableau dans 
#  double virgule ("").

#Par exemple

#Si nous voulons que chaque élément soit séparé par une virgule, 
# alors il faut utiliser la fonction split(" "). 
#le resultat est le suivent:

langages = "python Php Css Html Java JavaScript"
print(langages.split(" ")) #----> ['python', 'Php', 'Css', 'Html', 'Java', 'JavaScript']

nomDeLangages2 = "pythonPhpCssHtmlJavaJavaScript"
print(nomDeLangages2.split("p")) #----> ['', 'ythonPh', 'CssHtmlJavaJavaScri', 't']

nomDeLangages3 = "python-Php-Css-Html-Java-JavaScript"
print(nomDeLangages3.split("-")) #----> ['python', 'Php', 'Css', 'Html', 'Java', 'JavaScript']

nomDeLangages4 = "python-Php-Css-Html-Java-JavaScript"
print(nomDeLangages3.split("-",3)) #----> ['python', 'Php', 'Css', 'Html-Java-JavaScript']

#le function// .rsplit() -----> c'est le même fonctionnement de .split(), 
# mais il va partir de la droite vers la gauche.

nomDeLangages = "python-Php-Css-Html-Java-JavaScript"
print(nomDeLangages.rsplit("-", 3)) 

#-----> ['python-Php-Css', 'Html', 'Java', 'JavaScript']


#le function .join() permet de recomposer tous ces éléments d'un tableau sous
#forme de chaîne de caractères :

langages_séparés = ['Python','PHP','CSS','HTML','JAVA']

print(''.join(langages_séparés)) # ----> PythonPHPCSSHTMLJAVA
