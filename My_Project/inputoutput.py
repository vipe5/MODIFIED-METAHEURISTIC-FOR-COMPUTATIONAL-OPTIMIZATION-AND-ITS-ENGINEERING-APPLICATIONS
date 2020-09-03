#Fianl Yaer Project
#Group No.: 09

'''
    Solving Travelling Salesman Problem(TSP) using PSO(Particle Swarm Optimization)
    Discrete PSO for PSO

    References:
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.258.7026&rep=rep1&type=pdf

'''


import pandas as pd
import numpy as np

def read_tsp(filename):

    '''
       Read a .tsp file into a pandas DataFrame

       The .tsp files can be found in the TSPLIB project. Currently, the library
       only considers the possibility of a 2D map.
    '''

    with open(filename) as f:

        dimension = None
        node_coord_start = None
        lines = f.readlines()

        i = 0
        while not dimension or not node_coord_start:
            line = lines[i]
            if line.startswith('DIMENSION :'):
                dimension = int(line.split()[-1])
            if line.startswith('NODE_COORD_SECTION'):
                node_coord_start = i
            i += 1

        f.seek(0)

        cities = pd.read_csv(f, skiprows = node_coord_start + 1,
                sep = ' ', names = ['city', 'x', 'y'],
                dtype = {'city': str ,'x': np.float64, 'y': np.float64},
                header = None, nrows = dimension)

        return cities
