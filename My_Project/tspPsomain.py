
from matplotlib import pyplot as plt
import random
import sys
import pandas as pd
import numpy as np
from userScript import tsp_file_path
from Graph import  createGraph
from operator import attrgetter
import copy


#class that represents particle
class Particle:


    def __init__(self, solution, cost):
        self.current_solution = solution
        self.cost_current_solution = cost
        self.pbest_solution = solution
        self.pbest_solution_cost = cost
        self.velocity = []


    #updates current solution of particle
    def setCurrentSolution(self, new_solution):
        self.current_solution = new_solution


    #returns cost of current solution
    def getCurrentSolution(self):
        return self.current_solution


    #updates cost of current solution
    def setCostCurrentSolution(self, new_cost):
        self.cost_current_solution = new_cost


    #returns cost of current solution
    def getCostCurrentSolution(self):
        return self.cost_current_solution


    #updates new pbest solution
    def setPbestSolution(self, new_pbest_solution):
        self.pbest_solution = new_pbest_solution


    #returns pbest solution
    def getPbestSolution(self):
        return self.pbest_solution


    #updates cost of pbest solution
    def setCostPBestSolution(self, new_cost):
        self.pbest_solution_cost = new_cost


    #returns cost of pbest solution
    def getCostPbestSolution(self):
        return self.pbest_solution_cost


    #clears the velocity of particle
    def clearVelocity(self):
        del self.velocity[:]


#PSO algorithm
class PSO:


    def __init__(self, graph, iterations, max_population, alpha = 1, beta = 1):
        self.graph = graph  #the graph
        self.max_iterations = iterations  #total number of iterations
        self.population_size = max_population  #total number of particles
        self.particles = []  #list that contains all the particles
        self.alpha = alpha  #cognitive coefficient [self confidence factor]
        self.beta = beta  #social coefficient [neighbour confidence factor]

        #creates random solutions for particles
        solutions = self.graph.getRandomPaths(self.population_size)

        #checks if exits any solution
        if not solutions:
            print("Initial population empty! Run the algorithm again")
            sys.exit(1)

        #creates particles and initialization of swap sequences in all the particles
        for solution in solutions:
            particle = Particle(solution = solution, cost = self.graph.calculateCostPath(solution))
            self.particles.append(particle)

        #updates number of particles
        self.population_size = len(self.particles)


    #updates gbest solution
    def setGbest(self, new_solution):
        self.gbest = new_solution


    #returns gbest solution
    def getGbest(self):
        return self.gbest


    #shows the info of particles
    def showParticles(self):

        print("*****************************************************************Showing Particle**********************************************************************")
        for particle in self.particles:
            print("Pbest: %s  \nCost of Pbest: %d\n Current Solution: %s\n\nCost of Current Solution: %d" %(particle.getPbestSolution(), particle.getCostPbestSolution(), particle.getCurrentSolution(), particle.getCostCurrentSolution()))

        
        
         
        


    def run(self,f):
        #file = open("map.txt","r+")
        #file.truncate(0)
        #file1 = open("map1.txt","r+")
        #file1.truncate(0)
        
        for iter in range(self.max_iterations):
            self.gbest = min(self.particles, key = attrgetter("pbest_solution_cost"))  #updates  gbest
            solution_gbest = copy.copy(self.gbest.getPbestSolution()) #copy of solution of gbest
           #taking inputs in text file
           # f=open("map.txt","a")
            str1=str(iter)
            str2=str(self.gbest.getCostCurrentSolution())
            f.write(str1+","+str2+'\n')
           # f.close()
            
           
           

            

            #for each particle in swarm
            for particle in self.particles:

                particle.clearVelocity()  #clean the velocity of particle
                temp_velocity = []
                solution_pbest = copy.copy(particle.getPbestSolution())  #copy of pbest solution of particle
                solution_particle = copy.copy(particle.getCurrentSolution())  #copy of current solution of particle

                #generate all swap operator using pbest and current solution [pbest-current_solution]
                for i in range(self.graph.amount_vertices):
                    if solution_pbest[i] != solution_particle[i]:
                        swap_operator = (i, solution_pbest.index(solution_particle[i]), self.alpha)  #generates swap operator
                        temp_velocity.append(swap_operator)  #appends swap operator in the list of velocity

                #generate all swap operator using gbest and current solution [gbest-current_solution]
                for i in range(self.graph.amount_vertices):
                    if solution_gbest[i] != solution_particle[i]:
                        swap_operator = (i, solution_gbest.index(solution_particle[i]), self.beta)  #generates swap operator
                        temp_velocity.append(swap_operator)  #appends swap operator in the list of velocity

                particle.velocity = temp_velocity  #updates velocity of particle

                #generates new solution of particle
                for swap_operator in temp_velocity:
                    if random.random() < swap_operator[2]:
                        #makes the swap
                        aux = solution_particle[swap_operator[0]]
                        solution_particle[swap_operator[0]] = solution_particle[swap_operator[1]]
                        solution_particle[swap_operator[1]] = aux

                particle.setCurrentSolution(solution_particle)  #updates current solutio of particle

                particle.setCostCurrentSolution(self.graph.calculateCostPath(solution_particle))  #updates cost of current solution of particle

                #checks whether current solution is better than pbest solution
                if particle.cost_current_solution < particle.pbest_solution_cost:
                    particle.pbest_solution = particle.current_solution  #updates pbest solution
                    particle.pbest_solution_cost = particle.cost_current_solution  #updates cost of pbest solution



if __name__ == "__main__":

    graph = createGraph(tsp_file_path)
    pso = PSO(graph, iterations = 100, max_population = 10, alpha = .85, beta = .85)
    file = open("map.txt","r+")
    file.truncate(0)
        
    f=open("map.txt","a")
    pso.run(f)
    f.close()
    pso.showParticles()
    print(pso.gbest.getPbestSolution())
    print(pso.gbest.getCostPbestSolution())

    pso1 = PSO(graph, iterations = 100, max_population = 10, alpha = .85, beta = .85)
    file1 = open("map1.txt","r+")
    file1.truncate(0)
    f1=open("map1.txt","a")
    pso1.run(f1)
    f1.close()
    pso1.showParticles()
    print(pso1.gbest.getPbestSolution())
    print(pso1.gbest.getCostPbestSolution())

    #PRINTING 1ST GRAPH
    x, y = np.loadtxt('map.txt',delimiter=',',unpack=True) 
    plt.plot(x,y, color='green', label="first plot")

    # Set the x axis label of the current axis.
    plt.xlabel('ITERATIONS')
    # Set the y axis label of the current axis.
    plt.ylabel('GLOBAL_BEST')
    # Set a title 
    plt.title('GRAPH BETWEN ITERATIONS VS GBEST')
    
    #printing 2nd graph
    k,m = np.loadtxt('map1.txt',delimiter=',',unpack=True) 
    plt.plot(k,m, color='olive',label="second plot")

    # Set the x axis label of the current axis.
    #plt.xlabel('iterations')
    # Set the y axis label of the current axis.
    #plt.ylabel('Global_best')
    # Set a title 
    #plt.title('GRAPH BETWEN ITERATIONS VS GBEST')
    
    # Display the figure.
    plt.legend()#LABELLING EXISTING PLOT ELEMENTS
    plt.show()#DISPLAY THE GRAPH

    
    
