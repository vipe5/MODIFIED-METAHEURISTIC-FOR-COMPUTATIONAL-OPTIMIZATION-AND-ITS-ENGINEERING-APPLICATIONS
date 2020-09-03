#Fianl Yaer Project
#Group No.: 09

'''
    Particle Swarm Optimization(PSO) for a Fitness Function

    Fitness Function : x1^2 + X2^2 + (sin(x1))^2 + (sin(x2))^2

    References:
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.258.7026&rep=rep1&type=pdf
    https://www.intechopen.com/books/traveling_salesman_problem/particle_swarm_optimization_algorithm_for_the_traveling_salesman_problem

'''

import math
import random
from operator import attrgetter

population_size = 15  #total number of particles
max_dim = 2  #function has two dimension x1 and x2
w = .4  #inertia factor for velocity
c1 = 2.0  #cognitive coefficient [self confidence factor] [2.0-4.0]
c2 = 2.0  #social coefficient [neighbour confidence factor] [2.0-4.0]
tolerance = .000001  #stopping condition
max_iterations = 50  #maximun number of iterations


class Particle:
    '''
        Class that represents particles.
        It has some getter and setter methods to get and set the values of particles specifications

    '''

    def __init__(self, pno):
        self.particle_number = pno + 1
        self.current_coordinate = []
        self.current_velocity = []
        self.fitness = 0.0
        self.pbest = 0.0
        self.pbest_coord = []


    #returns position of particle
    def getCurrentCoordinate(self):
        return self.current_coordinate


    #set position of particle
    def setCurrentCoordinate(self, coordinates):
        self.current_coordinate = coordinates


    #returns velocity of particle
    def getCurrentVelocity(self):
        return self.current_velocity


    #set velocity of particle
    def setCurrentVelocity(self, velocity):
        self.current_velocity = velocity


    #returns fitness of particle
    def getCurrentFitness(self):
        return self.fitness


    #set fitness of particle
    def setCurrentFitness(self, fitness):
        self.fitness = fitness


    #returns personal best of particle
    def getPbest(self):
        return self.pbest


    #set personal best of particle
    def setPbest(self, pbest):
        self.pbest = pbest


    #returns personal best coordinate of particle
    def getPbestCoord(self):
        return self.pbest_coord


    #set personal best coordinates of particle
    def setPbestCoord(self, coordinates):
        self.pbest_coord =  coordinates


    #print values related to particle
    def print(self):
        print(self.particle_number, end="  ")
        print(self.current_coordinate, end="         ")
        print(self.current_velocity,end="         ")
        print(self.fitness, end="         ")
        print(self.pbest, end="         ")
        print(self.pbest_coord)


class Pso:


    def __init__(self, max_dimension, iterations, population_size, w, c1, c2, tolerance):
        self.particles = []
        self.max_dimension = max_dimension
        self.max_iterations = iterations
        self.population_size = population_size
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.tolerance = tolerance

        for p in range(self.population_size):
            particle = Particle(p)
            self.particles.append(particle)

        for particle in self.particles:
            coordinates = []
            x , y = random.uniform(-5,5), random.uniform(-5,5)
            coordinates.append(x)
            coordinates.append(y)
            particle.setCurrentCoordinate(coordinates)
            particle.setPbestCoord(coordinates)
            particle.setCurrentFitness(self.calculateFitness(particle))
            particle.setPbest(particle.getCurrentFitness())

        for particle in self.particles:
            velocity = []
            x_vel, y_vel = random.uniform(-5,5), random.uniform(-5,5)
            velocity.append(x_vel)
            velocity.append(y_vel)
            particle.setCurrentVelocity(velocity)
            particle.print()


    #return value of global best
    def getGbest(self):
        return self.gbest


    #set value of global best
    def setGbest(self, gbest):
        self.gbest = gbest


    #calulates fitness value for particle
    def calculateFitness(self, particle):
        x1 = particle.getCurrentCoordinate()[0]
        x2 = particle.getCurrentCoordinate()[1]
        a = math.sin(x1)
        b = math.sin(x2)
        fitness = pow(x1,2) + pow(x2,2) + pow(a,2) + pow(b,2)

        return fitness


    #calculate velocity of particles
    def calculateVelocity(self, particle, temp_velocity1, temp_velocity2):
        p = random.random()
        q = random.random()
        temp_velocity = []
        current_velocity = particle.getCurrentVelocity()
        pbest_coord = particle.getPbest()
        current_coordinate = particle.getCurrentCoordinate()
        for i in range(self.max_dimension):
            temp = (self.w * current_velocity[i]) + (self.c1 * p *(pbest_coord - current_coordinate[i])) + (self.c2 * q *(self.gbest.current_coordinate[i] - current_coordinate[i]))
            temp_velocity.append(temp)

        return temp_velocity


    #update position of particle
    def updateCoordinate(self,particle):
        current_coordinate = particle.getCurrentCoordinate()
        current_velocity = particle.getCurrentVelocity()
        temp_coord = []
        for i in range(self.max_dimension):
            temp = current_coordinate[i] + current_velocity[i]
            temp_coord.append(temp)

        return temp_coord

    def run(self):
        for iter in range(self.max_iterations):
            self.gbest = min(self.particles, key = attrgetter("pbest"))
            if iter != 0:
                if self.gbest.pbest <= self.gbest_fitness:
                    self.gbest_fitness  = self.gbest.pbest
                    self.gbest_coordinate  = self.gbest.pbest_coord
            self.gbest_coordinate = self.gbest.getPbestCoord()
            self.gbest_fitness = self.gbest.getPbest()
            print("Global Best Coordinate--------->",self.gbest_coordinate)
            print("Global best Fitness--------->" ,self.gbest_fitness)
            print("-----------------------------------------Iteration No.[%d]-------------------------------------" %iter)
            if(self.gbest_fitness<= self.tolerance):
                break

            for particle in self.particles:
                temp_velocity1 = []
                temp_velocity2 = []

                #generates (pbest-current_velocity)
                for i in range(self.max_dimension):
                    temp = particle.pbest_coord[i] - particle.current_velocity[i]
                    temp = ('%.8f' %temp)
                    temp_velocity1.append(temp)

                #generates (gbest-current_velocity)
                for i in range(self.max_dimension):
                    temp = self.gbest_coordinate[i] - particle.current_velocity[i]
                    temp_velocity2.append(temp)

                particle.setCurrentVelocity(self.calculateVelocity(particle, temp_velocity1, temp_velocity2))

                particle.setCurrentCoordinate(self.updateCoordinate(particle))

                particle.setCurrentFitness(self.calculateFitness(particle))

                if particle.pbest > particle.fitness:
                    particle.setPbest(particle.fitness)
                    particle.setPbestCoord(particle.current_coordinate)

                particle.print()


pso = Pso(max_dimension = max_dim, iterations = max_iterations, population_size = population_size, w = w, c1 = c1, c2 = c2, tolerance = tolerance)
pso.run()
