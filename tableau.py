import random as rd

class Framework():
    
    def __init__(self, cote):
        self.cote = cote    
        self.nb_cases = cote^2
        self.tableau = [[0 for _ in range(cote)] for _ in range(cote)]

    #on suppose que le tableau est un carré
    def afficher(self):
        for i in range(self.cote):
            for j in range(self.cote):
                print("[]", end="")
            print()

    def remplir(self, pourcentage,nb_personnes):
        #remplit une case du tableau avec une couleur donnée
        liste_positions = []        
        for i in range(self.cote):
            for j in range(self.cote):
                liste_positions.append([i,j]) 

        n_B=int(pourcentage * nb_personnes / 100)
        for k in range(n_B):
            numero = rd.randint(0, len(liste_positions)-1)
            x = liste_positions[numero][0]
            y = liste_positions[numero][1]
            liste_positions.pop(numero)
            print(x)
            self.tableau[x][y] = "B"

        for k in range(nb_personnes - n_B):
            numero = rd.randint(0, len(liste_positions)-1)
            x = liste_positions[numero][0]  
            y = liste_positions[numero][1]
            liste_positions.pop(numero)
            self.tableau[x][y] = "R"

    def vide(self):
        #renvoie la liste des cases non occupées du tableau
        liste_cases_vides = []  
        for i in range(self.nb_cases):
            for j in range(self.nb_cases):
                if self.tableau[i][j] == 0:
                    liste_cases_vides.append((i, j))