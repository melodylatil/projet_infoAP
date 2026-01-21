import numpy as np
import random as rd

class Human:
    def __init__(self):
        self.position=(0,0)
        self.color="blue"
        

    def get_neighbours(self, tableau, n):
        nb_blues=0
        nb_reds=0
        for i in range (self.position[0]-n, self.position[0]+n+1):
            for j in range (self.position[1]-n, self.position[1]+n+1):
                if tableau[i][j]=="B":
                    nb_blues+=1
                if tableau[i][j]=="R":
                    nb_reds+=1


    #si on a une méthode tableau.vide qui donne une liste de positions vide
    def move(self, tableau):
        n=rd.randint(0,len(tableau.vide()))
        self.position=tableau.vide()[n]