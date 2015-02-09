# -*- coding+: utf-8 -*-
"""
Created on Thu Feb  5 12:25:41 2015

@author: gerardo
"""
import random
import numpy as np

def signo(omegas, punto):
    resultado = omegas[1]*punto[0] + omegas[2]*punto[1] + omegas[0]
    print resultado
    return cmp(resultado, 0)
    

def solve():
    puntos = np.random.uniform(0,1, (2,2))
    A = np.array([ [puntos[0][1], 1], [puntos[1][1], 1] ])
    b = np.array([-puntos[0][0], -puntos[1][0]])
    x = np.linalg.solve(A, b)
    return x

def genera_uniforme(n):
    p = np.random.uniform(0,1, (1,2))
    for i in range(n -1):
        p = np.append(p, np.random.uniform(0,1,(1,2)), axis = 0)
    
    return p
    
def clases(puntos, omegas):
    return [signo(omegas, puntos[i]) for i in len(puntos)]


def clase(mp_omegas):
    return [1 if i > 0 else -1 if i < 0 else 0 for i in mp_omegas]


def perceptron(puntos, iteraciones):
    
    omegas = np.random.uniform(-1, 1, 3)
    matriz_puntos = np.ones((puntos.shape[0], 1))
    p = solve()
    omegas_iniciales = np.array([p[1], 1, p[0]]) 

    for i in range(len(puntos.T)):
        matriz_puntos = np.c_[matriz_puntos, puntos.T[i].reshape(-1, 1)]
    
    clase_original = clase(np.dot(matriz_puntos, omegas_iniciales))     
    
    for i in xrange(iteraciones):
    
        clase_it = clase(mp_omegas = np.dot(matriz_puntos, omegas))
        dif = np.where(clase_original != clase_it)
        
        if type(dif) is tuple:
            aux = dif[0][-1]
            dif = np.delete(dif, -1)
            dif = np.append(dif, aux)
            
        indice = random.choice(dif)
        if clase_original[indice] < 0:
            omegas -= matriz_puntos[indice]
        else:
            omegas += matriz_puntos[indice]
            
    return omegas
    
    
puntos = np.random.uniform(0,1,(1000,2))
print perceptron(puntos, 200)
    