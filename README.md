# MODIFIED-METAHEURISTIC-FOR-COMPUTATIONAL-OPTIMIZATION-AND-ITS-ENGINEERING-APPLICATIONS

ABSTRACT

In real life, we see many problems, where we have to optimize our solution. These type of problems are called Optimization Problem. In simplest terms, optimization can be considered as a maximization or minimization problem. To solve the optimization problem, efficient search or optimization algorithms are needed. Till date, there are many algorithms and approaches are discovered to solve optimization problem. In these algorithms, some have very high time complexity or some give us approximate result. Our aim is to improve this result with lesser time complexity.With a different perspective, Optimization algorithm can be classified
into classical and metaheuristic approaches. In this project our mainfocus is based on the metaheuristic algorithm which is one of the key algorithm for optimization. A metaheuristic can be considered as a "master strategy that guides and modifies other heuristics to produce solutions beyond those that are normally generated in a quest for local optimality". But before shifting to the modern solution we will first analyse the traditional and heuristic approach to solve the problem for an overall comparison with the metaheuristic approach for a complete and satisfactory result. To achieve our target, we will use a bench-mark problem THE TRAVELLING SALESMAN PROBLEM (TSP).

PREFACE

Introduction

Solving optimization problems becomes has become a central theme not only on operational research but also on several research areas like robotic, medicine, economic etc. The number of support decision problems that can be formalized as an optimization problem is growing rapidly. This study represents a literature revue of Metaheuristics optimization. Metaheuristics are applied to all kinds of combinatorial problems, and they can also be adapted to discrete problems. These approaches which include the genetic algorithms, the Ant Colony Algorithms, Particle Swarm Optimization (PSO) etc. are for both monoobjective problems and multi-objective problems. Before focusing on the multi-objective optimization, it is necessary to explain the context of the mono-objective optimization. A special attention is given to the method of Particle Swarm Optimization (PSO). To apply new algorithms and approaches we have to select a problem. In this project, we have taken the Travelling Salesman Problem (TSP). TSP is a benchmark NP-hard problem, which is suitable for apply metaheuristic approaches.

Keywords

Optimization problem, Objective function, Mono-Objective Function, Multi-Objective Function, Metaheuristics, Travelling Salesman Problem(TSP), Swarm Algorithm, Particle Swarm Optimization.

Motivation of The Project

We face many problems in day to day life where optimization is required like travelling some places, logistics etc. When we tried to solve these problems, we get stuck at some points. In our curriculum we have read many optimization techniques. But these techniques do not work for all problems. Some problems are so much complex that these techniques take too much time to solve. The inspiration for doing this project was primarily an interest in undertaking a challenging project in an interesting area of research. The opportunity to learn about a new area of computing not covered in lectures was appealing. It leads to us to explore a new and unique field of the computer science and which motivates us for learning a new aspect of solving optimization problem using different approach and algorithm. 

Basic Description of The Project

This project is based of study and implementation of different computational approach for optimization problems. As we know, there are many approaches present to solve optimization problem. For simple optimization problem these approaches work perfectly, but when we apply these approaches on highly complex problems like multi-objective optimizations or NP-hard problems, we find some issues related to those approaches. These issues are time complexity, limited computational capacity, approximation of result etc. There are two main methods of solving optimization problem, which are further classified. These two methods are Exact Method and Approximate Method. When we apply exact method, it takes too much time to solve the problem which is not possible for real time problems. Approximate Method, which is the second method, gives solution in real time, but sometimes it is too much different from exact result.

To overcome from above problems, we have tried to implement an algorithm which is nature inspired. This algorithm is known as Particle Swarm Optimization(PSO). PSO is originally attributed to Kennedy and Eberhart in 1995. It is inspired from bird flocks and fish schooling. Classical format of PSO is used to solve continuous optimization problem. But we have taken Travelling Salesman Problem as an exemplary problem which is a discrete optimization problem. To solve discrete optimization problem, we have to convert Classical PSO into Discrete PSO. To convert it into Discrete PSO, we have modified it and used concept of “Swap Operator”. To implement and analyse our algorithm we need a problem. Here we have taken Travelling Salesman Problem as an exemplary problem. In this problem, there are some cities which are connected to each other. We have to form a Hamiltonian Cycle i.e we have to find a minimal distance path which covers all the cities at most one time and return to initial position.

We have taken a dataset of 194 cities of Qatar. We have chosen Python language to write our code and implemented it on Python version 3.6/3.7.


LITERATURE RIVIEW

Researchers from various fields such as biology, physics,
mathematics, artificial intelligence, and many other fields are
devoting themselves to solve the Travelling Salesman Problem (TSP)
in much more efficient manner so as to develop much more efficient
algorithms than the pre-existing ones.
Some algorithms that have been developed are ant colony
optimization (ACO) , neural networks , genetic algorithm (GA) [10],
particle swarm optimization (PSO) , memetic computing , simulated
annealing (SA) etc.
Travelling Salesman Problem (TSP) is one such problem which has a
huge number and variety of real-world applications, vehicle routing,
data traffic routing in networking, finding the sequence for drilling
in printed circuit boards, DNA sequencing, pattern recognition in
image processing, transportation and logistics industry being some
of them.
In computational intelligence, swarm intelligence is a heavily
researched topic. Population being the attribute which simulates the
behaviour of animals in the real world. There are numerous swarm
intelligence algorithms that have been developed, ant colony
optimization, fish-warm algorithm, bee colony algorithm being some
of them.
Particle Swarm Optimization has become the most popular as it is
the easiest to implement due to its simple concept and mainly
because it has been applied in a variety of fields. Particle Swarm
xiii
Optimization (PSO) was developed by its developers to solve the
travelling salesman problem.
Review for Related Works
Angeline P. Evolutionary Optimization versus Particle Swarm
Optimization: Philosophy and Performance Difference. The 7th Annual
Conference. On Evolutionary Programming, San Diego, USA, 1998.
Kang-Ping Wang, lan Huang, Chun-Guang Zhou, Wei Pang, “ Particle
Swarm Optimization For Travelling Salesman Problem”, IEEE 2003.
Kennedy J, and Spears W. Matching algorithms to Problems: An
Experimental Test of the Particle Swarm and Some Genetic Algorithms
on the Multimodal Problem Generator. IEEE International Conference
on Evolutionary Computation, Anchorage, Alaska, USA, 1998
RELATED THEORIES AND ALGORITHMS
Related Theories Underlying the Work
Optimization Problem
In mathematics and computer science, an optimization problem is
the problem of finding the best solution from all feasible solutions.
Optimization problems can be divided into two categories depending on
whether the variables are continuous or discrete. An optimization
problem with discrete variables is known as a discrete optimization.
In a discrete optimization problem, we are looking for an object such as
an integer, permutation or graph from a countable set. Problems
with continuous variables include constrained problems and
multimodal problems.
Multi-Objective Optimization
Multi-objective optimization is an area of multiple criteria decision
making that is concerned with mathematical optimization problems
involving more than one objective function to be optimized
simultaneously. Multi-objective optimization has been applied in many
fields of science, including engineering, economics and logistics where
optimal decisions need to be taken in the presence of tradeoffs between two or more conflicting objectives.
Metaheuristics
In computer science and mathematical optimization, a
metaheuristic is a higher level procedure or heuristic designed to find,
generate, or select a heuristic (partial search algorithm) that may
provide a sufficiently good solution to an optimization problem,
especially with incomplete or imperfect information or limited
computation capacity.
Genetic Algorithms
A genetic algorithm (GA) is a metaheuristic inspired by the process
of natural selection that belongs to the larger class of Evolutionary
Algorithms (EA). Genetic algorithms are commonly used to generate
high-quality solutions to optimization and search problems by
relying on bio-inspired operators such as mutation, crossover and
selection.

Swarm Algorithms
Swarm Intelligence (SI) is the collective behaviour of decentralized,
self-organized systems, natural or artificial. The concept is employed
in work on artificial intelligence. SI systems consist typically of a
population of simple agents or birds interacting locally with one
another and with their environment. The inspiration often comes from
nature, especially biological systems. The agents follow very simple
rules, and although there is no centralized control structure dictating
how individual agents should behave, local, and to a certain degree
random, interactions between such agents lead to the emergence of
"intelligent" global behaviour, unknown to the individual agents.
Some important Swarm Algorithms are
1. Ant Colony Optimization
2. Particle Swarm Optimization
3. Artificial Swarm Intelligence
Particle Swarm Optimization (PSO)
PSO is computational method that optimizes a problem by iteratively
trying to improve a candidate solution with regard to given measure
of quality. It solves a problem by having a population of candidate
solutions, here called Particles, and moving these particles around in
search-space according to simple mathematical formulae over the
particle’s position and velocity. Each particle’s movement is influenced
by its local best-known position, but is also guided toward the bestknown positions in the search-space, which are updated as better
positions are found by other particles. This is expected to move the
swarm towards the best solution.
PSO converges quickly relative to other population-based optimization
algorithms such as Genetic Algorithms (GA) and also offering good
quality solution. 

Classical PSO Algorithm
The concept of PSO roots from the social behaviour of organism such as
bird flocking and fish schooling. Through cooperation between
individuals, the group often can achieve their goal more efficiently in
a effective manner. PSO simulates this social behaviour as an
optimization tool to solve some optimization issues. In a PSO system,
each particle having two properties of position and velocity represents
a candidate solution which is expressed by the objective function. In the
iterations, the objective function is finding out to establish the fitness
value of each particle using position as input. Fitness value indicates,
which position is better. Each particle flies in search-space with a
velocity which is dynamically adjusted based on its flying experience
and its companions’ flying experience.
PSO can be describe in mathematical terms as follows. Suppose that the
search space is of d-dimension and the number of particles is n. The [i]th
particle is represented by d-dimension vector X[i]=(X[i][1],
X[i][2],…X[i][D];
Pbest[i]=(P[1], P[2],…..P[D]) denotes the best position searched by the
[i]th particle and the Gbest=(G[1], G[2],…..,G[D]) is the best position
searched by the whole swarm up-to now.
Each particle updates it velocity and position according to following
equations:
v[i][d] = w*v[i][d] + c1*rand()*(Pbest[i][d]-X[i][d]) + c2*rand()*
(Gbest[i][d] - X[i][d])………….(1)
X[i][d] = X[i][d] +v[i][d]………………………………….. ……………………….(2)
Where w is an inertia coefficient which is chosen constant in interval
[0,1], c1 is a cognitive coefficient (self confidence factor), c2 is social
coefficient (neighbour confidence factor), rand() is random value in
interval [0,1].

Travelling Salesman Problem
The travelling salesman problem asks the following question: "Given a
list of cities and the distances between each pair of cities, what is the
shortest possible route that visits each city and returns to the origin
city?" It is an NP-hard problem in combinatorial optimization,
important in operations research and theoretical computer science.
As A Graph Problem
TSP can be modelled as an undirected weighted graph, such that
cities are the graph's vertices, paths are the graph's edges, and a
path's distance is the edge's weight. It is a minimization problem
starting and finishing at a specified vertex after having visited each
other vertex exactly once.







Symmetric & Asymmetric
In the symmetric TSP, the distance between two cities is the same in
each opposite direction, forming an undirected graph. This symmetry
halves the number of possible solutions. In the asymmetric TSP, paths
may not exist in both directions or the distances might be different,
forming a directed graph.
Integer Linear Programming Formulation
The TSP can be formulated as an integer linear program. Several
formulations are known. Two notable formulations are the Miller-
xviii
Tucker-Zemlin (MTZ) formulation and the Dantzig-Fulkerson-Johnson
(DFJ) formulation.
Miller-Tucker-Zemlin Formulation
Label the cities with the numbers 1, …, n and define:

For i = 1, …, n, let u[i] be a dummy variable, and finally take c[i][j] to
be the distance from city i to city j. Then TSP can be written as the
following integer linear programming problem:

The first set of equalities requires that each city is arrived at from
exactly one other city, and the second set of equalities requires that
from each city there is a departure to exactly one other city. The last
constraints enforce that there is only a single tour covering all cities,
and not two or more disjointed tours that only collectively cover all
cities.
To prove that every feasible solution contains only one closed sequence
of cities, it suffices to show that every subtour in a feasible solution
passes through city 1 (noting that the equalities ensure there can only
be one such tour). For if we sum all the inequalities corresponding 
xix
to xij=1 for any subtour of k steps not passing through city 1, we
obtain:
which is a contradiction.
It now must be shown that for every single tour covering all cities,
there are values for the dummy variables u[i] that satisfy the
constraints.
Without loss of generality, define the tour as originating (and ending)
at city 1. Choose u[i]=t if city i is visited in step t (i, t = 1, 2, ..., n).
Then
since u[i] can be no greater than n and u[j] can be no less than 1;
hence the constraints are satisfied whenever u[i]=0. For u[j]=1, we
have:

satisfy the constraint.

Dantzig-Fulkerson-Johnson Formulation
Label the cities with the numbers 1, …, n and define:


Take c[i][j] to be the distance from city i to city j. Then TSP can be
written as the following integer linear programming problem:

The last constraint of the DFJ formulation ensures that there are no
sub-tours among the non-starting vertices, so the solution returned is
a single tour and not the union of smaller tours.
Computing a Solution
Exact Algorithm
The most direct solution would be to try all permutations (ordered
combinations) and see which one is cheapest (using brute-force search).
The running time for this approach lies within a polynomial factor
of O(n!).
Some exact algorithms are
1. Brute Force Algorithm
2. Branch and Bound Algorithm

Heuristic Algorithm
Various heuristics and approximation algorithms, which quickly
yield good solutions have been devised. Modern methods can find
solutions for extremely large problems (millions of cities) within a
reasonable time which are with a high probability just 2–3% away from
the optimal solution.
Some heuristics algorithms are
1. Greedy Algorithm
2. Christofides Algorithm


Metaheuristic Algorithm
The above described metaheuristic approach is classical approach
which is suitable for problems of continuous quantities. It can not
applied directly to problem of discrete quantities. To solve this kind of
problem based on PSO, we will introduce “Swapping Operator”.

Concept of Swap Operator
Take a solution sequence of TSP problem with n nodes, M = (L[i]),
i=1,2,..,n
MO(i[1], i[2]) can be defined as exchanging node L[i][1] and L[i][2] in
solution M. Then M’ = M + MO(i[1], i[2]) can be defined as a new solution
on which operator MO(i[1], i[2]) acts.
Eg:
Suppose there is a Travelling Salesman Problem with 5 nodes,
solution M = (6, 7, 8, 9, 10). The swap operator is MO(3, 4), then
M’ = M+MO(3, 4)
 =(6, 7, 8, 9, 10) + (3, 4)
 =(6, 7, 9, 8, 10)
Sequence of Swap
A sequence of swap having one or more Swap Operators. MM = (MO[1],
MO[2], ……………,MO[n]), where MO[1], MO[2],………,MO[n] are Swap
Operators.
Swap Sequence acting on a solution can be called as all the Swap
Operators of the swap sequence act on a solution in order. This can be
described by following formula:
M’ = M + MM
 = M + (MO[1], MO[2],……….,MO[n])
 = ((((M + MO[1]) + MO[2])……..+ MO[n])
Various swap sequence acting on a same solution may create the same
new solution. All these Swap Sequences are called the equivalent set of
Swap Sequences. In the equivalent set, the sequence which having the
least number of swap operator is called Basic Swap Sequence of set.

Basic Sequence of Swap Creation
Suppose there is two Solution A and B, and our task is to create Basic
Swap Sequence MM which can act on B to get solution A, we define 
xxii
MM = A - B.
Eg:
Two solutions are:
A = (1, 2, 3, 4, 5) and B = (2, 3, 1, 5, 4)
Since A[1] = B[3] = 1, so the first swap operator is MO(1, 3),
B[1] = B + MO(1, 3), then following result can be get:
B[1]: (1, 3, 2, 5, 4)
Since A[2] = B[1][3] = 2, so the second swap operator is MO(2, 3),
B[2] = B[1] + MO(2, 3) and B[2] = (1, 2, 3, 5, 4)
The third operator is MO(4, 5), then B[3] = A. Finally we get
Basic Swap Sequence MM = A – B =(MO(1, 3), MO(2, 3), MO(4, 5).

Modified Velocity Update Equation
The velocity update equation of classical PSO is not suitable for the TSP
problem. It can be updated as follow:
v[i][d] = v[i][d]  *(Pbest[i][d] – X[i][d])  *(Gbest[i][d] – X[i][d])
where  and  are random numbers between 0 and 1. *(Pbest[i][d] –
X[i][d]) means all swap operator in Basic Swap Sequence (Pbest[i][d] –
X[i][d]) should be maintained with probability of . *(Gbest[i][d] –
X[i][d])
means all swap operator in Basic Swap Sequence (Gbest[i][d] – X[i][d])
should be maintained with probability of .

Fundamental Algorithms
Branch and Bound Algorithm
1) Get upper bound.
2) Solve the problem as an assignment problem (without constraint that
tour be connected).
3) (BOUNDING, I) Each time an assignment problem has been solved
and gives a cost worse than the current upper bound, terminate that
branch.
4) (BRANCHING) If a solved problem doesn’t give a valid tour, pick
one cycle in the tour (usually the shortest), and create branches, one for
each edge in the cycle. At the end of each branch, solve the assignment
problem corresponding to the parent problem together with the
additional constraint that the associated edge is forbidden from the
solution. (To forbid an edge, set its cost to ∞).
5) (BOUNDING PART II) If a solved problem yields a valid tour, with
cost (z ?, say) that is less than the current upper bound, then replace the
current upper bound with z ? then terminate all branches whose
objective value is worse than z ? .
6) Stop when only one branch survives. This solves the TSP.
Greedy Algorithm
1) Initialize all vertices as unvisited.
2) Select an arbitrary vertex, set it as the current vertex u.
Mark u as visited.
3) Find out the shortest edge connecting the current vertex u and an
unvisited vertex v.
4) Set v as the current vertex u. Mark v as visited.
5) If all the vertices in the domain are visited, then terminate. Else, go
to step 3.

Classical PSO Algorithm
1. Initialize a population of particle.
2. do
1. for each particle p with x[p] do
1. if (x[p] is better than pbest[p]) then
1. Pbest[p]  x[p]
2. end if
2. end for
3. Define gbest as the best position found so far by any of p’s
neighbors
4. for each particle p do
1. v[p]  compute_velocity(x[p], pbest[p], gbest)
2. x[p]  update_position(x[p], v[p])
5. end for
3. while (a stop criterion is not satisfied)

PROPOSED MODEL/ALGORITHM
Proposed Algorithm
Discrete PSO Algorithm
Step 1:
Each of the particles gets a random solution and a random Swap
Sequence, namely velocity.
Step 2:
If the algorithms are ended, go to step 5.
Step 3:
For all the particles in position X[i][d], calculating the next
position X[i][d’].
3.1 Calculating difference between P[i][d] and X[i][d],
according to the method that has been Shown above,
A=Pbest[i][d]-X[i][d], where A is a basic sequence.
3.2 Calculating B = Gbest[i][d] - X[i][d], B is also a basic
sequence.
3.3 Calculating velocity V[i][d] and then transform swap
Sequence V[i][d] to a basic Swap Sequence.
3.4 Calculating new solution
X[i][d] = X[i][d] +V[i][d]
 means that Swap Sequence V[i][d] acts on solution X[i][d]
to get a new solution.
3.5 If the new solution is superior to Pbest[i][d] then update
Pbest[i][d].
Step 4:
If there is new best solution; which is Superior to Pbest[i][d] then
update Pbest[i][d] . Go to step 2.
Step 5:
Draw the global best solution.

SIMULATION RESULT
Experimental Result
Iteration vs Cost Graph
Above graph shows cost of travelling in each iteration. In this
graph we can see that travelling cost is decreasing with number of
iterations. That means our algorithm is trying to find less travelling
cost in each iteration.
To make a comparison we run the algorithm twice, and plotted their
result in same graph, which is shown by green line. When we compare
both the result, we find that our proposed algorithm give different
values for same alpha() and beta(),due to the random function used in
the algorithm.

Table 1.  Tour Best Distance Value for Particular Simulation Run 

Run No.  Tour Best Value  Run No.  Tour Best Value
1 89075.0 11 84101.0
2 87627.0 12 84101.0
3 84749.0 13 84101.0
4 84749.0 14 84101.0
5 84749.0 15 84101.0
6 84749.0 16 84101.0
7 84526.0 17 81242.0
8 84526.0 18 81242.0
9 84526.0 19 81242.0
10 84101.0 20 81242.0


DISCUSSION AND CONCLUSION

Discussion

After completion of project we have found many interesting things, which are very necessary to be discussed. We implemented to modify previously exist algorithm, which is working fine. We have got that our proposed algorithm solves the problem in lesser time and with high accuracy. In our program, we use different constants and some random numbers, there scope is fixed throughout the program. We run our program many times by changing the value of alpha() and beta() and found some interesting results .We found that value of alpha() , beta() near to .85 give more accurate results than the other values. In our algorithm we use “ rand() ” functions to generate some random number between 0 and 1. This random number is used as probability. For different random numbers, program behaves differently, and give some new result.

Future Work

In our project, we have made some changes in basic PSO algorithm, that works very well. There are also many metaheuristic algorithms that are present. We can say that if we’ll research and try to modify and merge these algorithms, there will be higher possibility that we find even a more better solution for highly complex optimization problems. We can further try to modify PSO and get a better solution with lesser time complexity.

Conclusion

We tried to analyse optimization problem with classical and heuristic approaches. In classical approach, result was exact but execution time was very high. In heuristic approaches, we had taken some assumption. Due to these assumptions, result was not exact, but time complexity was less. We also tried to understand the metaheuristic approaches and evolutionary algorithm. We modified a metaheuristic algorithm called Particle Swarm Optimization (PSO). We proposed discrete PSO algorithm to solve Travelling Salesman Problem. Our proposed algorithms solved the TSP problem and generated more precise result and in less computational cost and time.

REFERENCES

www.google.com

www.wikepedia.com

www.github.com

www.intechopen.com

www.linkspringer.com

www.geeksforgeeks.com

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.258.7026&rep
=rep1&type=pdf
