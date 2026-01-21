from tableau import Framework
from human import Human

tableau=Framework(10)
tableau.remplir(pourcentage = 50, nb_personnes=10)
print(tableau.tableau)