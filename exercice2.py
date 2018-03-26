#Andy Dinga
#Exercice 2
# Exercice 2

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
                            #1)

#prix = Y : cout de la maintenance annuel exprimé en centaine d'euros
prix_vehicule=[48, 43, 77, 89, 50, 40, 56, 62, 100, 47, 71, 58, 102, 35, 60]

#age = X : age du vehicule exprimé en mois 
age_vehicule=[15, 8, 36, 41, 16, 8, 21, 21, 53, 10, 32, 17, 58, 6, 20]

                            #2)

numero=0
a=0
b=0

for i in range(0,10):
    numero+=( prix_vehicule[i]-np.mean(prix_vehicule) )* ( age_vehicule[i]-np.mean(age_vehicule))
    a+= (prix_vehicule[i]-np.mean(prix_vehicule))**2
    b+= (age_vehicule[i]-np.mean(age_vehicule))**2

#B1 : pente de la droite de regression, et variation moyenne de Y si X augmente d'une unité
B1=numero/a

#B0 : valeur moyenne des observations Yi quand xi=0    
B0=np.mean(age_vehicule) - B1* np.mean(prix_vehicule)


print("La valeur du paramètre B1 est :",B1)
print("La valeur du paramètre B0 est :",B0)
x=np.linspace(0,110);

reglin=B1*x+B0

plt.plot(prix_vehicule,age_vehicule,'x')
plt.plot(x,reglin)                                    
plt.show()

                            #4)

r=numero/(sqrt(a)*sqrt(b))
print("La valeur du coeffiecient corrélation de Pearson est :", r)

          
