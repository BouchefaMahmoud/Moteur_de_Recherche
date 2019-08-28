import numpy 

lignes =  eval(open('lines.txt','r').read())
colonnes =  eval(open('colonnes.txt','r').read())

nblignes = len(lignes.values())
nbcolonnes = 1471

matrix = numpy.zeros((nblignes,nbcolonnes))

for fichier,x in lignes.items() : 
   
    f = open("CorpusPreproc/"+fichier, encoding="utf-8").read()
    for mot,y in colonnes.items() : 
        nb = f.count(mot)
        matrix[int(x)-1][int(y)-1]= nb 
    

from scipy.spatial import distance
print(distance.cosine(matrix[5,:],matrix[6,:]))






    






