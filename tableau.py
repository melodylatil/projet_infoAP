import random as rd

class Framework:
    
    def __init__(self, coté, nb_cases):
        self.coté = coté    
        self.nb_cases = nb_cases

    #on suppose que le tableau est un carré
    def afficher(self):
        for i in range(self.nb_cases):
            for j in range(self.nb_cases):
                print("[]", end="")
            print()

    def remplir(self, position, couleur, pourcentage,nb_personnes):
        #remplit une case du tableau avec une couleur donnée
        liste_positions = []        
        for i in range(self.nb_cases):
            for j in range(self.nb_cases):
                liste_positions.append([i,j]) 
        n_B=int(pourcentage * nb_personnes / 100)
        for k in range(n_B):
            numero = rd.randint(0, len(liste_positions)-1)
            x = liste_positions[numero][0]
            y = liste_positions[numero][1]
            liste_positions.pop(numero)
            self[x][y] = "B"

        for k in range(nb_personnes - n_B):
            numero = rd.randint(0, len(liste_positions)-1)
            x = liste_positions[numero][0]  
            y = liste_positions[numero][1]
            liste_positions.pop(numero)
            self[x][y] = "R"

    def vide(self):
        #renvoie la liste des cases non occupées du tableau
        liste_cases_vides = []  
        for i in range(self.nb_cases):
            for j in range(self.nb_cases):
                if self[i][j] == 0:
                    liste_cases_vides.append((i, j))