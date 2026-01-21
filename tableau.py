class Framework:
    def __init__(tableau, coté, nb_cases):
        tableau.coté = coté    
        tableau.nb_cases = nb_cases

    #on suppose que le tableau est un carré
    def afficher(tableau):
        for i in range(tableau.nb_cases):
            for j in range(tableau.nb_cases):
                print("[]", end="")
            print()
    def remplir(tableau, position, couleur):
        #remplit une case du tableau avec une couleur donnée
        x, y = position 
        tableau[x][y] = couleur
        #remplit le tableau avec les valeurs de la liste
        index = 0
        

    def vide(tableau):
        #renvoie la liste des cases non occupées du tableau
        liste_cases_vides = []  
        for i in range(tableau.nb_cases):
            for j in range(tableau.nb_cases):
                if (i,j) == 0:
                    liste_cases_vides.append((i, j))