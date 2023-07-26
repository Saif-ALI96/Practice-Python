#La liste d'une maniere simple, c'est la possibilité d'ajouter et de stocker un nombre illimité de données

tableau = ['python','Php','Css','Html','Java','JavaScript',[1,2,3,4,5,['France','Irak', 'Italy']]]

print(tableau[2])  #On utilise le numéro pour acceder
#----> Css
#print(tableau[-1][-1])   #on peut aussi utiliser les indices negatifs
#------> ['France', 'Irak', 'Italy']

print(tableau[6][5][1]) #-----> on peut aussi cibler un tableau dans un autre tableau qui est aussi dans un autre
#---> Irak


#nous avons la possiblilte de remplacer un objet par un autre 
#par exemple:

#tableau2 = ['python','Php','Css','Html']
#tableau2[3] ='C++'
#print(tableau2) #----> # ['python', 'Php', 'Css', 'C++']



#Pour supprimer un élément nous allons utiliser la fonction del()
#par exemple:

#tableau3 = ['python','Php','Css','Html','java']
#del tableau3[2]
#print(tableau3) #-----> il va nous elever (Php) dans le tableau ['python', 'Php', 'Html', 'java']



#Si vous voulez voir si un element existe dans votre listes vous pouvez faire :
#par exemple :

#tableau4 = ['python','Php','Css','Html','java']
#if "java" in tableau4:
#    print("Oui")


#Vous avez maintenant compris comment créer une liste. Nous allons apprendre à manipuler ces listes avec différent
#méthodes.
# Pour commencer, nous allons afficher tous nos elements grâce au for loop
#par exemple :

tableau5 = ['python','Php','Css','Html','java']

for i in range(len(tableau5)):
 print(i,"-",tableau5[i])


