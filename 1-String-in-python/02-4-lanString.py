# on va voir la contionnalité de la fonction .lan()
#lan == lenght 

country = "France Irak Sweden Italy Spain"

print(len(country)) # 30 caractères, donc 
#.len(country) == 30 (car le \n est compté comme un charatère).


country3 = "France Irak Sweden Italy Spain"
print(country3.index("S")) #----> 12 //

# pour afficher la place de l'element dans le tableau
#mais en chiffre(number) Comme dans l'exemple ci-dessus 
# s'il y a deux S,  cela nous renvoie le premier indice du mot 'Sweden'.

country4 = "Sweden Italy Spain"
print(country4.index("Italy")) #-----> est (7)


#######$$$$$$$$$$$#########$$$$$$$$$$$$$###########$$$$$$$$$$$$$######

#le function  .replace() permet d'effectuer une remplacement des lettres par les autres:

country5 = "Germany Ireland Portugal Greece Turkey"
print(country5.replace('I', 'i')) #--->  ireland 
print(country.replace('Ireland', 'Irak')) # ----> France Irak Sweden Italy Spain

