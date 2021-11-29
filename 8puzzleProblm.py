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

# print(Search.searchDFS(initialState, GoalState))
# print(Search.searchBFS(initialState, GoalState))
print(Search.searchDLS(initialState, GoalState, 2), sep=" === > \n\n")
# print(Search.searchUCS(initialState, GoalState), sep=" === > \n\n")
# print(Search.searchGreedy(initialState, GoalState), sep=" === > \n\n")