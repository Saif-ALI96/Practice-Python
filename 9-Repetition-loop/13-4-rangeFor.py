#nous allons voir le range avec le loop for en python
# par exemple

for i in range(10):
    print(i)
# ---->   0
         #1
         #2
         #3
         #4
         #5
         #6
         #7
         #8
         #9
# ca va nous faire une bocle sans prendre le dernier chiffre en compte
#, ici on aura donc un rang de 0 à 9.

#on peut aussi utiliser le range() avec deux chiffres dans les parentheses

for test2 in range(4,10 ):
    print(test2)
#--->  4, 5 ,6,7 ,8 ,9   

#On peut aussi l'utiliser pour des calculs mathématiques:

a = [1,2,3]
b = []
for x in a :
    b.append (x*2 )
    print(b)
#----->[2] [2,4,],[2,4,6],...

# nous pouvons utiliser len() avec le range() pour afficher le contenu d'un list ou bien plus

namesOfLanguages = ['html', 'css' , 'js' , 'python']
# print(len(namesOfLanguages)) #----> 4
len(namesOfLanguages)
for test in range(len(namesOfLanguages)):
    print("The language is ", namesOfLanguages[test])
# The language is  html
# The language is  css
# The language is  js
# The language is  python
    


