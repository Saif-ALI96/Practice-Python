# le return dans la function


def operationOfMaht(num1,num2):
    return num1 + num2
# le return sera le dernier a mettre dans la fonction pour pouvoir excuter l'operation indiquer dans notre  fonction

print("The result is : ",operationOfMaht(30,5))  #-----> The result is :  35



def sum(num2,num3):
    print('the number of the first parameter',num2) #-----> the number of the first parameter 47896
    print('the number of the second parameter',num3) #-----> the number of the second parameter 65432
    return (num2+num3)
#return est un mot clé qui permet de retourner une valeur à partir du code.
print ("the value returned by this funtion",sum(47896,65432))
#------->  the value returned by this funtion 113328



#exercis 1

'''def calecDay(age):
    return str(age * 365)
print(calecDay(26)) 
# -----> 9490'''

#exercice 2-1
def calcuHours(age):
    return 'your age in hour is : ' + str(age * 365 * 24) + ' hours'
#print(calcuHours(26))
# -------> your age in hour is : 227760 hours
print(calcuHours(int(input('entre your age : '))))
# on a mis le int pour avoir le resultat en integer number car on est bien d'accord tout ce qu'il sort de l'input 
# c'est un string. c'est pour cela la function int() nous aide a l'a faire 

#exercice 2-1

age = input('entre your age : ')
ageday = int(age)*365
print('your age in day is : ' + str(ageday) + ' days')
#-----> your age in day is : 12410 days


# exercice 3
def calculMonth(year):
    return str(year/12)
print(calculMonth(26))
# --------> 0.2








