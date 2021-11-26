# AISearchAlgorithm
Search Divides into two type, one is about having information about the goal and the other is not having information about the goals. so we have 
1. Uninformed Search
2. Informed Search

#### Before Start
 - The process of deciding what actions and states to consider is Problem Formulation
   - States of the world
   - Actions are transmission between states
 - The process of deciding what the next goal to be is Goal Formulation
 - Search is the process of looking for solution and a search consist of
   - A state space
   - A transmission model
     -  a successor function with actions and cost
   - A start state and a goal test
   - A path cost function
 - Solution is a squence of actions which transforms the start state to a goal state.

#### Search algorithm properties
- _Complete_ : Guaranteed to find a solution if one exists
- _Optimal_ : Guaranteed to find the least cost path
- _Time_ complexity matters
- _Space_ complexity matters

#### General Tree Search
![image](https://user-images.githubusercontent.com/45999644/143463346-50dc1f5a-76f7-42ca-8fe5-e7dfd797f5c3.png)

This algorithm makes a frontier list and every time choose a state from that frontier with a strategy (e.g. UCS, DFS, etc.)

#### General Graph Search
![image](https://user-images.githubusercontent.com/45999644/143463203-7d5e8c29-07a8-4795-9818-0bddd0f3e775.png)

This algorithm makes a frontier list and also a explored list. Every time chooses a state from that frontier with a strategy (e.g. UCS, DFS, etc.) and it checks that, the state that has been choosen was not been seen before.
## Uninformed Search Strategies
The main characteristic of the Uninfomred search is to not using the information about the goal.

1. Breadth-First Search (BFS)
2. Uniform-Cost Search (UCS)
3. Depth-First Search (DFS)
4. Depth-Limited Search (DLS)
5. Iterative Deepening Search (IDS)

### Depth-First Search
- DFS strategy is to expand the deepest node first. 
- Its frontier is _LIFO (Last in first out = stack)_
- It returns the solution by the time it reaches to it.

### Breadth-First Search
- BFS strategy is to expand the shallowest node first. 
- Its frontier is _FIFO (First in first out = queue)_
- It returns the solution by the time it reaches to it.

### Depth-limited Search

### Iterative-deepening Search

### Uniform-Cost Search

## Informed Search
The main characteristic of the informed search is using some information about the goal, to reach the Goal. These types of search method uses a heuristics function to evaluate the cost from the current state to the Goal state.

#### A heuristic is 
- A function that estimates how close a state is to a goal
- Designed for a particular search problem
Examples: Manhattan distance, Euclidean distance for pathing

### Greedy Search
Greedy search expands the node that appears to be closest to goal, So its priority queue is only base on _h(n)_ and _h(n)_ calculation can be diffrent and the node with the lowest _h(n)_ will be selected from the frontier. In 8 puzzle it can be number of miss place tile or manhattan distance.

### A* Search
This algorithm has a evaluation function _F(n) = G(n) + h(n)_. This algorithm each time choose the state with lowest F(n) value. So F(n) value defines the priority in the frontier.
