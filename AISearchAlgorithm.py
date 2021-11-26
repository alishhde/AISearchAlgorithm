# Writer of this code:
# Seyyed Ali Shohadaalhosseini

# We'll never forget that:
#                        < What doesn't kill you makes you STRONGER >

class SearchAlgorithm():
    """
        This module contains all the AI Search Algorithm.
        Just import and call the method you want with the
        required arguments.
    """
    def __init__(self):
        pass
    
    def searchDFS(self, initialState, GoalState, spaceGraph=[]):
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
            self.updateFringe(currentState, explored)
            
            # Step 3
            currentState = self.fringe[-1]
            
            counter += 1
            
    def searchBFS(self, initialState, GoalState, spaceGraph=[]):
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
            self.updateFringe(currentState, explored)
            
            # Step 3
            currentState = self.fringe[0]
            
            # counter += 1
            
    def searchDLS(self, initialState, GoalState, limitation, spaceGraph=[]):
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
            
            currentState = initialState
            self.fringe.append(currentState)
            
        else:
            # we don't need to calculate the childs.
            pass
        counter = 0 
        limitCounter = 0
        while True:
            
            if limitCounter == limitation:
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
                self.updateFringe(currentState, explored)
                
                # Step 3
                currentState = self.fringe[-1]
                
                limitCounter += 1
        
            # counter += 1
            
    def searchIDS(self, initialState, GoalState, spaceGraph=[]):
        """ DLS Has problem. """
        pass
    
    def searchUCS(self, initialState, GoalState, spaceGraph=[]):
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
                    print("The path has been found.")
                    return explored
                
            else:
                # current state is in explored list
                pass
            
            # step 2 - deleting the currentstate from the fringe and cost
            currentStateIndex = self.fringe.index(currentState)
            del self.fringe[currentStateIndex]
            self.FatherCost = self.cost[currentStateIndex]
            del self.cost[currentStateIndex]
            
            # now we must calculate the child of the currentstate and add them to the frontier 
            # In this code our default problem is 8 puzzle problem
            self.updateFringe(currentState, explored, GoalState, algorithmType="UCS")
            
            # Step 3 - Choosing the state we minimum cost
            minimumCost = min(self.cost)
            minimumCostIndex = self.cost.index(minimumCost)
            currentState = self.fringe[minimumCostIndex]
            
            counter += 1
    
    def searchGreedy(self, initialState, GoalState, spaceGraph=[]):
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
                    print("The path has been found.")
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
    
    def searchAstar(self):
        pass

    def updateFringe(self, currentState, parents, GoalState, algorithmType="", problem="eightPuzzle"):
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
            if (spaceIndex[0] - 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0] - 1, spaceIndex[1]))

            if (spaceIndex[0] + 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0] + 1, spaceIndex[1]))

            if (spaceIndex[1] - 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0], spaceIndex[1] - 1))
                
            if (spaceIndex[1] + 1) in domain:
                availableMoveIndexForSpace.append((spaceIndex[0], spaceIndex[1] + 1))    
            
            # 3- Now we must create those states and return all thenext states we have
            from copy import deepcopy
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
                        self.cost.append(self.CostCalculator(newstate, GoalState, type="MissedPlaced"))
                    
                    elif algorithmType == "Greedy":
                        self.fringe.append(newstate)
                        self.cost.append(self.heuristics(newstate, GoalState, type="MissedPlaced"))
                    
                    elif algorithmType == "":
                        self.fringe.append(newstate)
                        
            
            return self.fringe # A list of all the next states
    
    def CostCalculator(self, newState, GoalState, type="MissedPlaced"):
        """This function calculates the cost of a state

        Args:
            newState (list): The state is a a of three list
            type (str, optional):  Defaults to "MissedPlaced".
        """
        # -------------------This method is not right--------------------- #
        # -------------------This method is not right--------------------- #
        if type == "MissedPlaced":
            CostOfNewState = 0
            for row in range(len(newState)):
                for col in  range(len(GoalState)):
                    if newState[row][col] != GoalState[row][col]:
                        CostOfNewState += 1
            return CostOfNewState + self.FatherCost
        # -------------------This method is not right--------------------- #
        # -------------------This method is not right--------------------- #
    
    def heuristics(self, newState, GoalState, type="MissedPlaced"):
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