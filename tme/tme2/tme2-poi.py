from Prediction import histogramme , noyau_parzen
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle


    
    
    
    
plt.ion()
parismap = mpimg.imread('data/paris-48.806-2.23--48.916-2.48.jpg')

## coordonnees GPS de la carte
xmin,xmax = 2.23,2.48   ## coord_x min et max
ymin,ymax = 48.806,48.916 ## coord_y min et max

def show_map():
    plt.imshow(parismap,extent=[xmin,xmax,ymin,ymax],aspect=1.5)
    ## extent pour controler l'echelle du plan

poidata = pickle.load(open("data/poi-paris.pkl","rb"))
## liste des types de point of interest (poi)
print("Liste des types de POI" , ", ".join(poidata.keys()))

## Choix d'un poi
typepoi = "atm"

## Creation de la matrice des coordonnees des POI
geo_mat = np.zeros((len(poidata[typepoi]),2))
for i,(k,v) in enumerate(poidata[typepoi].items()):
    geo_mat[i,:]=v[0]

## Affichage brut des poi
show_map()
## alpha permet de regler la transparence, s la taille
plt.scatter(geo_mat[:,1],geo_mat[:,0],alpha=0.8,s=3)


###################################################

# discretisation pour l'affichage des modeles d'estimation de densite
steps = 10
xx,yy = np.meshgrid(np.linspace(xmin,xmax,steps),np.linspace(ymin,ymax,steps))
grid = np.c_[xx.ravel(),yy.ravel()]

# A remplacer par res = monModele.predict(grid).reshape(steps,steps)
#res = histogramme(poidata).fit("restaurant",[2.23,2.48],[48.806,48.916]).reshape(steps,steps)
#res = np.random.random((steps,steps))
#H = histogramme(poidata)
#res = H.fit(typepoi,[xmin,xmax],[ymin,ymax],steps)
#H.predict((48.850,2.32))
parzen = noyau_parzen(poidata,[xmin,xmax],[ymin,ymax],typepoi)
res = parzen.estimation_parzen(0.015)


plt.figure()
show_map()
plt.imshow(res,extent=[xmin,xmax,ymin,ymax],interpolation='none',alpha=0.3,origin = "lower")
plt.colorbar()
plt.scatter(geo_mat[:,0],geo_mat[:,1],extent=[xmin,xmax,ymin,ymax],alpha=0.3)



