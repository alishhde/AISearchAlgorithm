# Writer of this code:
# Seyyed Ali Shohadaalhosseini

# We'll never forget that:
#                        < What doesn't kill you makes you STRONGER >

from random import shuffle
from copy import deepcopy
from time import sleep

class SearchAlgorithm():
    """
        This module contains all the AI Search Algorithm.
        Just import and call the method you want with the
        required arguments.
    """
    def __init__(self):
        pass
    
    def searchDFS(self, initialState, GoalState, spaceGraph=[]):
        ## DONE Successfully
        """This algorithm will return the solution path.

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        if spaceGraph == []:
            currentState = list()
            self.fringe = list()
            explored = list()
            parentStates = list()
            
            currentState = initialState
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        
        while True:
            
            # step 1
            if currentState not in explored:
                explored.append(currentState)
                
                print("\n\n", "This is currrent state: ", "\n\n")
                for row in currentState:
                    print(row)
                    
                if counter == 50:
                    break
                if currentState == GoalState:
                    print("The path has been found.")
                    return explored
            else:
                # current state is in explored list
                pass
            
            # step 2 - deleting the currentstate from the fringe 
            currentStateIndex = self.fringe.index(currentState)
            del self.fringe[currentStateIndex]
            
            # now we must calculate the child of the currentstate and add them to the frontier 
            # In this code our default problem is 8 puzzle problem
            self.updateFringe(currentState, explored, GoalState)
            
            # Step 3
            currentState = self.fringe[-1]
            
            counter += 1
            
    def searchBFS(self, initialState, GoalState, spaceGraph=[]):
        ## DONE Successfully
        """This algorithm will return the solution path.

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        if spaceGraph == []:
            currentState = list()
            self.fringe = list()
            explored = list()
            parentStates = list()
            
            currentState = initialState
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        
        while True:
            
            # step 1
            if currentState not in explored:
                explored.append(currentState)
                
                print("\n\n", "This is currrent state: ", "\n\n")
                for i in currentState:
                    print(i)
                    
                # if counter == 50:
                #     break
                
                if currentState == GoalState:
                    print("The path has been found.")
                    return explored
                
            else:
                # current state is in explored list
                pass
            
            # step 2 - deleting the currentstate from the fringe 
            currentStateIndex = self.fringe.index(currentState)
            del self.fringe[currentStateIndex]
            
            # now we must calculate the child of the currentstate and add them to the frontier 
            # In this code our default problem is 8 puzzle problem
            self.updateFringe(currentState, explored, GoalState)
            
            # Step 3
            currentState = self.fringe[0]
            
            # counter += 1
            
    def searchDLS(self, initialState, GoalState, limitation, spaceGraph=[]):
        ## DONE Successfully
        """This algorithm is depth limited search and will return the solution path. 

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        if spaceGraph == []:
            currentState = list()
            self.fringe = list()
            explored = list()
            parentStates = list()
            pathexplored = list()
            self.limitation = limitation
            currentState = initialState
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        self.limitCounter = 0
        while True:
            
            if self.limitCounter == self.limitation:
                # step 1
                if currentState not in explored:
                    explored.append(currentState)
                    
                    print("\n\n", "This is currrent state: ", "\n\n")
                    for row in currentState:
                        print(row)
                        
                    # if counter == 50:
                    #     break
                    
                    if currentState == GoalState:
                        print("The path has been found.")
                        self.answerFLAG = True
                        return explored
                else:
                    # current state is in explored list
                    pass
                
                # step 2 - deleting the currentstate from the fringe 
                currentStateIndex = self.fringe.index(currentState)
                del self.fringe[currentStateIndex]
                
                if self.fringe == []:
                    return "The answere has not been found in this depth", explored
                
                # Step 3
                currentState = self.fringe[-1]
            
            else:
                # step 1
                if currentState not in explored:
                    explored.append(currentState)
                    
                    print("\n\n", "This is currrent state: ", "\n\n")
                    for row in currentState:
                        print(row)
                        
                    if counter == 50:
                        break
                    if currentState == GoalState:
                        print("The path has been found.")
                        return explored
                else:
                    # current state is in explored list
                    pass
                
                # step 2 - deleting the currentstate from the fringe 
                currentStateIndex = self.fringe.index(currentState)
                del self.fringe[currentStateIndex]
                
                # now we must calculate the child of the currentstate and add them to the frontier 
                # In this code our default problem is 8 puzzle problem
                if self.limitCounter == self.limitation:
                     # Step 3
                    currentState = self.fringe[-1]
                
                else:
                    self.limitCounter += 1
                    self.updateFringe(currentState, explored, GoalState, algorithmType="DLS")
                    if self.limitCounter+1 == limitation:
                        self.limitCounter += 1
                    
                    print("This is our fringe state: ")
                    print(self.fringe)
                    # for i in self.fringe:
                    #     print(f"State {i}")
                    #     for j in i:
                    #         print(j)
                            
                    # Step 3
                    currentState = self.fringe[-1]
                
        
            # counter += 1
            
    def searchIDS(self, initialState, GoalState, spaceGraph=[]):
        ## DONE Successfully
        depthCounter = 26
        self.answerFLAG = False
        while not self.answerFLAG:
            answerIs = self.searchDLS(initialState, GoalState, depthCounter)
        else:
            print(f"This didn't kill you too, the path found at the depth {depthCounter} ;)")
            return answerIs
    
    def searchUCS(self, initialState, GoalState, spaceGraph=[]):
        ## Temporary Done
        """This algorithm will return the solution path.

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        if spaceGraph == []:
            currentState = list()
            self.fringe = list()
            self.cost = [0]
            explored = list()
            parentStates = list()
            
            currentState = deepcopy(initialState)
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        while True:
            
            # step 1
            if currentState not in explored:
                explored.append(currentState)
                
                # print("\n\n", "This is currrent state: ", "\n\n")
                # for i in currentState:
                #     print(i)
                
                # if counter == 1000:
                    # break
                    
                if currentState == GoalState:
                    print(f"The path has been found at iterate {counter}")
                    return explored
                
            else:
                # current state is in explored list
                pass
            
            # step 2 - deleting the currentstate from the fringe and cost
            currentStateIndex = self.fringe.index(currentState)
            del self.fringe[currentStateIndex]
            self.FatherCost = self.cost[currentStateIndex]
            del self.cost[currentStateIndex]
            print(self.FatherCost)
            # now we must calculate the child of the currentstate and add them to the frontier 
            # In this code our default problem is 8 puzzle problem
            self.updateFringe(currentState, explored, GoalState, algorithmType="UCS")
            
            # Step 3 - Choosing the state we minimum cost
            minimumCost = min(self.cost)
            minimumCostIndex = self.cost.index(minimumCost)
            currentState = self.fringe[minimumCostIndex]
            
            counter += 1
    
    def searchGreedy(self, initialState, GoalState, spaceGraph=[]):
        ## DONE Successfully
        """This algorithm will return the solution path.

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        if spaceGraph == []:
            currentState = list()
            self.fringe = list()
            self.cost = [0]
            explored = list()
            parentStates = list()
            
            currentState = initialState
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        while True:
            
            # step 1
            if currentState not in explored:
                explored.append(currentState)
                
                print("\n\n", "This is currrent state: ", "\n\n")
                for i in currentState:
                    print(i)
                
                # if counter == 1000:
                    # break
                    
                if currentState == GoalState:
                    print(f"The path has been found at iterate {counter}")
                    return explored
                
            else:
                # current state is in explored list
                pass
            
            # step 2 - deleting the currentstate from the fringe and cost
            currentStateIndex = self.fringe.index(currentState)
            del self.fringe[currentStateIndex]
            del self.cost[currentStateIndex]
            
            # now we must calculate the child of the currentstate and add them to the frontier 
            # In this code our default problem is 8 puzzle problem
            self.updateFringe(currentState, explored, GoalState, algorithmType="Greedy")
            
            # Step 3 - Choosing the state we minimum cost
            minimumCost = min(self.cost)
            minimumCostIndex = self.cost.index(minimumCost)
            currentState = self.fringe[minimumCostIndex]
            
            counter += 1
    
    def searchAstar(self, initialState, GoalState, spaceGraph=[]):
        ## Temporary Done
        """This algorithm will return the solution path.

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        if spaceGraph == []:
            currentState = list()
            self.fringe = list()
            self.cost = [0]
            explored = list()
            parentStates = list()
            
            currentState = deepcopy(initialState)
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        while True:
            
            # step 1
            if currentState not in explored:
                explored.append(currentState)
                
                # print("\n\n", "This is currrent state: ", "\n\n")
                # for i in currentState:
                #     print(i)
                
                # if counter == 1000:
                    # break
                    
                if currentState == GoalState:
                    print(f"The path has been found at iterate {counter}")
                    return explored
                
            else:
                # current state is in explored list
                pass
            
            # step 2 - deleting the currentstate from the fringe and cost
            currentStateIndex = self.fringe.index(currentState)
            del self.fringe[currentStateIndex]
            self.FatherCost = self.cost[currentStateIndex]
            del self.cost[currentStateIndex]
            print(self.FatherCost)
            # now we must calculate the child of the currentstate and add them to the frontier 
            # In this code our default problem is 8 puzzle problem
            self.updateFringe(currentState, explored, GoalState, algorithmType="Astar")
            
            # Step 3 - Choosing the state we minimum cost
            minimumCost = min(self.cost)
            minimumCostIndex = self.cost.index(minimumCost)
            currentState = self.fringe[minimumCostIndex]
            
            counter += 1

    def searchHillClimbing(self, initialState, GoalState, spaceGraph=[]):
        ## Done successfully
        """This algorithm will return the solution path.

        Args:
            initialState (List): Start state.
            GoalState (list): End state.
            spaceGraph (list): For the time user enter his graph states.
        """
        # Step 1
        currentState = deepcopy(initialState)
        explored = [] # We don't use this in hillClimbing. it is for not getting error
        
        # Step 2 - loop
        while currentState != GoalState:
            
            # Step 3
            self.fringe = []
            self.updateFringe(currentState, explored, GoalState, algorithmType="")
            
            # Step 4
            statesCost = []
            for state in self.fringe:
                cst = self.heuristics(state, GoalState)
                statesCost.append(cst)
            minValue = min(statesCost)
            minValueIndex = statesCost.index(minValue)
            
        
            currentValue = self.heuristics(currentState, GoalState)
            
            # print(self.fringe, self.fringe[minValueIndex], minValue, currentState, currentValue, sep="\n")
            # raise NotImplementedError
        
            # Step 5, 6
            if currentValue < minValue: # Lower because, lower heuristic means we are closer to the goal
                # we are trap into the local Maximum
                # now we must have random restart
                # we do this by creating a random state
                print(currentValue)
                print("we are restarting..")
                sleep(3)
                currentState = self.random8PuzzleCreator()
            else:
                currentState = self.fringe[minValueIndex]
            
        else:
            return currentState
                        
    def random8PuzzleCreator(self):
        # Done successfully
        """
            we want a list, consist of three list that 
            each list consists three value
            
            """
        states = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]
        shuffle(states)
        for row in states:
            shuffle(row)
        return states
        
    def updateFringe(self, currentState, parents, GoalState, algorithmType="", problem="eightPuzzle", callInMethod=False):
        # Done successfully
        """
        as we are solving 8 puzzle, we describe it here,
            1- First we must find the space in the 8 puzzle.
            2- then we must find the nodes that can change their place,
            3- then we must return these nodes that can move.
        
        return:
            This functions calculates the frontier nodes and returns it
        """
        
        if problem == "eightPuzzle":
            """In 8 puzzle problem, we have a list consist of 3 list each consist of three values e.g.
                [
                    [1, 2, 3],
                    [8, " ", 4], 
                    [7, 6, 5]
                ] 
                In this problem 1- we must find the space and 2- look for the numbers that can change their place
                with space and return those states.
            """
            
            # 1- We look for the space in the currentState
            rowCounter = 0
            columnCounter = 0
            flag = False
            for eachrow in currentState:
                for col in eachrow:
                    if col == " ":
                        """
                            Now we must find this value's index
                        """
                        spaceIndex = [rowCounter, columnCounter]
                        flag = True # says we must to break
                        break
                    else:
                        columnCounter += 1
                if flag:
                    flag = False
                    break
                columnCounter = 0
                rowCounter += 1
            
            # 2- In the next lines we are going to add all the possible state's index
            availableMoveIndexForSpace = list()
            domain = [0, 1, 2]
            if (spaceIndex[0] - 1) in domain: # Upper Row
                availableMoveIndexForSpace.append((spaceIndex[0] - 1, spaceIndex[1]))

            if (spaceIndex[0] + 1) in domain: # Lower Row
                availableMoveIndexForSpace.append((spaceIndex[0] + 1, spaceIndex[1]))

            if (spaceIndex[1] - 1) in domain: # Left Column
                availableMoveIndexForSpace.append((spaceIndex[0], spaceIndex[1] - 1))
                
            if (spaceIndex[1] + 1) in domain: # Right Column
                availableMoveIndexForSpace.append((spaceIndex[0], spaceIndex[1] + 1))    
            
            # 3- Now we must create those states and return all thenext states we have
            for moveIndex in availableMoveIndexForSpace:
                # Here we must change the space and the number
                newstate = []
                newstate = deepcopy(currentState)
                newstate[spaceIndex[0]][spaceIndex[1]], newstate[moveIndex[0]][moveIndex[1]] = newstate[moveIndex[0]][moveIndex[1]], newstate[spaceIndex[0]][spaceIndex[1]]
                
                if newstate in parents or newstate in self.fringe:
                    continue
                else:
                    if algorithmType == "UCS":
                        self.fringe.append(newstate)
                        self.cost.append(self.CostCalculator(newstate, GoalState, type="OnDepthCount"))
                    elif algorithmType == "Astar":
                        self.fringe.append(newstate)
                        gn = self.CostCalculator(newstate, GoalState, type="OnDepthCount")
                        hn = self.heuristics(newstate, GoalState, type="MissedPlaced")
                        fn = gn + hn
                        self.cost.append(hn)
                        pass
                    
                    elif algorithmType == "Greedy":
                        self.fringe.append(newstate)
                        self.cost.append(self.heuristics(newstate, GoalState, type="MissedPlaced"))
                    
                    elif algorithmType == "DLS":
                        if callInMethod:
                            if newstate in self.fringe:
                                pass
                            else:
                                self.fringe.insert(self.newstateINDEX, newstate)
                        if self.limitCounter+1 == self.limitation and not(callInMethod):
                            if newstate in self.fringe:
                                pass
                            else:
                                self.fringe.append(newstate)
                                self.newstateINDEX = self.fringe.index(newstate) - 1
                                self.updateFringe(newstate, parents, GoalState, algorithmType="DLS", callInMethod=True)
                        else:
                            if newstate in self.fringe:
                                pass
                            else:
                                self.fringe.append(newstate)
                    
                    elif algorithmType == "":
                        self.fringe.append(newstate)
                        
            return self.fringe # A list of all the next states
    
    def CostCalculator(self, newState, GoalState, type="OnDepthCount"):
        # This function has problem
        """This function calculates the cost of a state
        This function calculates the G(n)

        Args:
            newState (list): The state is a a of three list
            type (str, optional):  Defaults to "OnDepthCount".
        """
        # -------------------This must be check more--------------------- #
        return 1 + self.FatherCost
    
    def heuristics(self, newState, GoalState, type="MissedPlaced"):
        # Done successfully
        """This function calculates the cost of a state

        Args:
            newState (list): The state is a a of three list
            type (str, optional):  Defaults to "MissedPlaced".
        """
        if type == "MissedPlaced":
            CostOfNewState = 0
            for row in range(len(newState)):
                for col in  range(len(GoalState)):
                    if newState[row][col] != GoalState[row][col]:
                        CostOfNewState += 1
            return CostOfNewState