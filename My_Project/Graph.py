#Final Year Project: 2016-20
#Group No.: 09

#Encoding: UTF-8

'''
         Solution for Travelling Salesaman Problem(Tsp) using PSO(Particle Swarm Optimization)
         Descrete PSO for PSO

         References:
         http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.258.7026&rep=rep1&type=pdf
         https://www.intechopen.com/books/traveling_salesman_problem/particle_swarm_optimization_algorithm_for_the_traveling_salesman_problem

'''

import random
import sys
import math
import pandas as pd
import numpy as np
from inputoutput import read_tsp

#Class that represents the Graph
class Graph:

    def __init__(self, amount_vertices):
        self.edges = {}  #Dictinoary to store edges and their costs
        self.vertices = set()  #Set of vertices
        self.amount_vertices = amount_vertices  #Total number of vertices


    #Adds edges with "src" and "dest" with their cost
    def addEdge(self, src, dest, cost = 0):
        if not self.existsEdge(src,dest):
            self.edges[(src, dest)] = cost
            self.vertices.add(src)
            self.vertices.add(dest)


    #Checks if exists a edge linking "src" and "dest"
    def existsEdge(self, src, dest):
        return(True if(src, dest) in self.edges else False)


    #Shows all links of graph
    def showGraph(self):
        print("Showing graph: \n")
        for edge in self.edges:
            print("%s is linked with %s with cost %s" %(edge[0], edge[1], self.edges[edge]))


    #Calculates cost of paths
    def calculateCostPath(self, path):
        total_cost = 0
        for i in range(self.amount_vertices-1):
            total_cost += self.edges[(path[i],path[i+1])]

        total_cost += self.edges[(path[self.amount_vertices-1], path[0])]
        return total_cost


    #Gets random unique paths - return a list of lists of paths
    def getRandomPaths(self, max_size):

        random_paths, list_vertices = [], list(self.vertices)

        initial_vertice = random.choice(list_vertices)

        #checks whether initial vertice present in list oif vertices or not
        if initial_vertice not in list_vertices:
            print("Error: initial vertice %d does not exists." %(initial_vertice))
            sys.exit(1)

        list_vertices.remove(initial_vertice)
        list_vertices.insert(0, initial_vertice)
        for i in range(max_size):
            temp_list = list_vertices[1:]
            random.shuffle(temp_list)
            temp_list.insert(0,initial_vertice)

            if temp_list not in random_paths:
                random_paths.append(temp_list)
        return random_paths


#Class presents a complete graph
class completegraph:

    def generate(self):
        for i in range(self.amount_vertices):
            for j in range(self.amount_vertices):
                if i != j:
                    cost = random.randint(1, 10)
                    self.addEdge(i, j, cost)



#Calculates cost between two vertices
def calculatecost(df1, df2, k):
    xcost = df1['x'].iloc[k] - df2['x2'].iloc[k]
    ycost = df1['y'].iloc[k] - df2['y2'].iloc[k]

    distance = round(math.sqrt(xcost**2 + ycost**2))

    return distance


def createGraph(tsp_file_path):

    problem = read_tsp(tsp_file_path)

    points = problem[['city', 'x', 'y']]

    vertices = len(points.index)

    graph = Graph(amount_vertices = vertices)

    columns = ['city1', 'city2']
    df_new = pd.DataFrame(columns = columns)

    items = range(1, vertices)
    for i in items:
        points2 = pd.DataFrame(np.roll(points, i, axis = 0))
        points2.columns = ['city', 'x2', 'y2']
        for j in range(0, vertices):
            x1 = calculatecost(points, points2, j)
            df_new = df_new.append({'city1' : points['city'].iloc[j], 'city2' : points2['city'].iloc[j], 'cost' : x1}, ignore_index = True)


    new_list = df_new.values.tolist()

    tsp_list = set(tuple(x) for x in new_list)

    for value1, value2, key in tsp_list:
        graph.addEdge(value1, value2, key)

    print("Added all the edges.")
    #graph.showGraph()

    return graph
