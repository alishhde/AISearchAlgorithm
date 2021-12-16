# Written by
# Seyyed Ali Shohadaalhosseini

# We'll never forget that:
#                        < What doesn't kill you makes you STRONGER >

import AISearchAlgorithm


Search = AISearchAlgorithm.SearchAlgorithm()

initialState = [
    [1, 2, 3],
    [7, 8, 4],
    [6, " ", 5]
]

# This can not be found easily
# initialState = [
#     [1, 2, 3],
#     [6, " ", 4],
#     [7, 8, 5]
# ]


GoalState = [
    [1, 2, 3],
    [8, " ", 4],
    [7, 6, 5]
]

ans = "y"

while ans == "y":
    WhichAlgorithm = input("""Enter one of the name below to search with the default parameters: \n
        Enter DFS as Depth First Search\n
        Enter BFS as Breadth First Search\n
        Enter DLS as Depth Limited Search\n
        Enter IDS as Iterative Deepening Search\n
        Enter UCS as Uniform Cost Search\n
        Enter ASTAR as A Star Search\n
        Enter GREEDY as Greedy Search\n
        Enter HILL as Hill Climbing Search: \n
        Enter the name here: """).lower()
    
    if WhichAlgorithm == "DFS".lower():
        print(Search.searchDFS(initialState, GoalState))
        
    elif WhichAlgorithm == "BFS".lower():
        print(Search.searchBFS(initialState, GoalState))
        
    elif WhichAlgorithm == "DLS".lower():
        print(Search.searchDLS(initialState, GoalState, 28), sep=" === > \n\n")

    elif WhichAlgorithm == "IDS".lower():
        print(Search.searchIDS(initialState, GoalState), sep=" === > \n\n")

    elif WhichAlgorithm == "UCS".lower():
        print(Search.searchUCS(initialState, GoalState), sep=" === > \n\n")
        
    elif WhichAlgorithm == "ASTAR".lower():
        print(Search.searchAstar(initialState, GoalState), sep=" === > \n\n")
        
    elif WhichAlgorithm == "GREEDY".lower():
        print(Search.searchGreedy(initialState, GoalState), sep=" === > \n\n")
        
    elif WhichAlgorithm == "HILL".lower():
        print(Search.searchHillClimbing(initialState, GoalState), sep=" === > \n\n")
    
    ans = input("Do you want to continue ? y/n ")
