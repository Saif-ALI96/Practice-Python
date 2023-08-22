#  execis 
#  faire les vleurs de la list en majuscule  et miniscules
# par exemple :

the_liste = ["hello", "world"]
for item in the_liste:
    new_item=str(item).upper()
    print("New Item:",new_item)

#  or

list = ['css', 'html', 'python']
for loop in range(len(list)):
    new_upper_list= list[loop].upper()
    print(new_upper_list)
