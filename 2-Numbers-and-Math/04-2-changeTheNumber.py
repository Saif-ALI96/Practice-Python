# Nous allons voir comment peut on changer les numbres vers string ou l'inverse.

#function float() -----> return number float 
#function str() ----> return "string"
#function int()  ----> return number integer 
#function type() ----> savoir le type de l'objet 


changeNumber = (7+7)
'''print(changeTheNumber + "years old" ) #------>TypeError: unsupported operand type(s) for +: 'int' and 'str'
nous pouvons pas faire cete operation entre un strign et Number. pour resoudre ce problem 
on va mettre le mot (str)deveant le variable pour excuter cette operation 
'''

print(str(changeNumber) + " " + "years old") #---> 14 years old
#le plus (+) dans le print s'appelle concaténation ou (concatenation --> en anglais)  

# on peut changer les nombres type integer (عدد صحيح) a nombres type folat ( رقم عشري)

print(type(15)) # --->  <class 'int'>

print(float(15)) #----> nous aurons le float number (15.0)

# on peut tres bien faire l'inverse que l'exemple ci-dessus
# Par exemple]

print(int(15.6)) # -----> nous aurons le integer number (15)



