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
# print(Search.searchDLS(initialState, GoalState, 28), sep=" === > \n\n")
# print(Search.searchIDS(initialState, GoalState), sep=" === > \n\n")
# print(Search.searchUCS(initialState, GoalState), sep=" === > \n\n")
# print(Search.searchGreedy(initialState, GoalState), sep=" === > \n\n")
print(Search.seachHillClimbing(initialState, GoalState), sep=" === > \n\n")


# """ DLS Has problem. """
#         depthCounter = 0
#         while not self.answerFLAG:
#             answerIs = self.searchDLS(initialState, GoalState, depthCounter)
#         else:
#             print(f"This didn't kill you too, the path found at the depth {depthCounter} ;)")
#             return answerIs