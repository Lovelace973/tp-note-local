#Andy Dinga
#Exercice 1
import matplotlib.pyplot as plt
import numpy as np
                                    #1)

annee=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
effectif_h=[3386,3663,4763,3848,3466,3971,3934,4158,4558,4564,3915,4693,4655,4573,4496]
effectif_f=[3628,3753,3506,3813,3811,3484,4866,4863,4174,3911,4241,4834,4972,4699,4276]

plt.hist([effectif_f,effectif_h], range = (3300, 5500), bins = 20, color = ['orange','purple'],
            edgecolor = 'black',label = ['effectif Feminin', 'effectif Masculin'])

plt.title("Effectif des étudiant masculin et feminin entre 2001 et 2005")
plt.xlabel("Effectifs")
plt.ylabel("Flux")
plt.legend()


plt.show()
#Je n'arrive pas a inserer l'année dans le graphe

                                    #3)

moyenne_feminin=np.mean(effectif_f)
ecartype_feminin=np.std(effectif_f)

                                    #4)

def courbe_loi_normal() :
    
    mu, sigma = (moyenne_feminin, ecartype_feminin)
    
    loi_norm=np.random.normal(mu, sigma, 1000)

    count, bins, ignored = plt.hist(loi_norm, 50, normed=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=1, color='orange')
    plt.title("Moyenne et écart type des effectifs feminins")
    plt.xlabel("Effectifs feminin entre 2001 et 2005")
    plt.ylabel("Courbe de la loi normal")
    plt.legend()

    plt.show()       


courbe_loi_normal()


