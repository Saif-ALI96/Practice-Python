#Ajourd'hui, on va apprendre les Numbres en python.

# - Les numbres sont des objets de type `int` عدد صحيح
# ou `float` ارقام عشريه comme (10.05) et complex comme .
#Que nous pouvons appliquer toutes les opérations mathématiques telles que:
#l'addition, la soustraction, la division , la multiplication et le module %
#Exemple :

print(type(5)) #----> <class 'int'>

print(type(5.5))#-----><class 'float'>

print(type(1+2j)) #-----><class 'complex'> 


test = 2
print(test)

test2 = (3+3)
print(test2) #--> 6

test3 = (2*3 + 4*5)
print(test3)# --> 26

test4=((12-8)*5)/10
print(test4)# --> 2.0

test5 = (15%2)
print(test5)# --> 1


def operation(operator,num1,num2):
    if operator == '+' :
        return num1 + num2
    elif operator=='-' :
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else :
        num1 / num2
print (operation('*', 3,6)) # sortie ----> 18
    
    
    