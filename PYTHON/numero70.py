import random
import numpy as np

# random=np.random.randint(1,9)
# print (random)
arreglo=[]

def aleatorios(n):
    for x in range(n):
        arreglo.append(random.randint(1,9))
    return arreglo
def contador(contador):
    for y in arreglo:
        contador +=y
    print(contador)
aleatorios(15)
contador (0)
if contador!=70:
    print(y)
else:
    print("Nel")
    # res=arreglo[0]+arreglo[1]