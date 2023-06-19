# Comparisons in Python
## Comparison Operators
### Equal to (==) Operator
#```python
a = 10
b = "Python"
c = True
d = False
e = None # Null value
f = []    # Empty list
g = {}    # Empty dictionary
h = ()    # Empty tuple
i = set() # Empty Set
j = range(5,2,-3)   # Range object with start and stop values. Step is optional parameter
k = [1,"two",True]

# on peut tres bien utiliser un if dans une fonction ou l'inverse 

def names(Saif, Johan ,Hassan):
    if Saif > Johan and Saif > Hassan:
        print('Saif has the best result :')
        return Saif
    
    elif Johan> Saif and Johan > Hassan :

        print('Johan has the best result :')
        return Johan
    
    else:
     
     print('Hassan has the best result :')
    return Hassan

print(names(97,95,80))
