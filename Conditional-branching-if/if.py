# ajourd'hui nous allons voir conditional if in python
#En Python, l'instruction 'if' est utilisée pour exécuter du code de manière conditionnelle.
# Elle vous permet de spécifier une condition, et si cette condition est vraie, 
#le bloc de code associé à l'instruction 'if' sera exécuté. 
#Si la condition est fausse, le bloc de code sera ignoré.
#La syntaxe d’une instruction ‘if’ se présente comme suit :

# if , elif , else

x = 5 #on prend un entier en entrée
y= 10
if x < y:
    print('y is greater than x') 
    #------> y is greater than x

test = True
if test == True:
    print("test is correct")
    #---> test is correct

if test: # une maniere in python te dire c'est vrai 
    print ("test is true ")
    #---> test is true

test2 = False  
if not test2: # une maniere te dire que la variable est False
    print ('test is false ')
    #---> test is false


age = int(input("enter your age: "))
if age >= 6 and age <=9:
    print("Age between six to nine years old.")

elif age >=10 and age <=15:
    print("your are not a child!, you are a teenager")
else:
    print("you're an adult!")



