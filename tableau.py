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