from random import random as rand
import numpy as np



class MarkovChain:
    def __init__(self,initial_distribuition,prob_matrix):
        """initial_distribuition need to be a <<vertical>> vector"""
        self.__dist = np.matrix(initial_distribuition)
        self.__prob = np.matrix(prob_matrix)
        self.__n = max(self.__dist.shape[0],self.__dist.shape[1])
        if self.__prob.shape[0] != self.__prob.shape[1]:
            raise ValueError("Matrix needs to be square!")
        if min(self.__dist.shape[0],self.__dist.shape[1]) != 1:
            raise ValueError("Distribution needs to be a vector!")
        if self.__n != self.__prob.shape[0]:
            raise ValueError("Distribution needs to have the same number of states thand the matrix!")
        
        if self.__dist.shape[1] == 1:
            self.__dist = self.__dist/self.__dist.sum()
        else:
            self.__dist = self.__dist.T/self.__dist.sum()
        Prob = []
        for row in range(self.__n):
            aux = self.__prob[row,:].copy()
            lin = aux/aux.sum()
            lin = lin.tolist()[0]
            Prob.append(lin)
        self.__prob = np.matrix(Prob)
            

    def __cumsum(self,vector):
        ls = [0]
        if vector.shape[1] != 1:
            vector = vector.T
            
        for i in range(self.__n):
            ls.append(vector.item(i) + ls[-1])
        ls = np.matrix(ls[1:])
        return ls.T

    def __choose(self,distribution):
        r = rand()
        __cumsum = self.__cumsum(distribution)
        if r <= __cumsum[0]:
            return 0
        for i in range(1,self.__n):
            if __cumsum[i] <= r and r <= __cumsum[i+1]:
                return i
        return self.__n
    
    def get(self,name='dist'):
        """name = [distribution] or [probability_matrix] or its initial letter"""
        if name.lower().startswith('d'):
            return self.__dist
        elif name.lower().startswith('p'):
            return self.__prob
        

    def export(self,horizont):
        ls = [self.__choose(self.__dist)]
        dist = self.__dist.copy()
        for i in range(horizont):
            dist = self.__prob.T @ dist
            dist = dist/dist.sum()
            ls.append(self.__choose(dist))
        return ls
        

