import copy
def h0(puzzle):
	openList = []
	closeList = []
	sol = []
	search = []
	openList.append(puzzle) #appending the initial node
	sol.append([0,0,puzzle.getState()])
	counter = 0 
	while not openList[0].isGoal(): #as long is it dosnt find the goal keep loopin
		search.append([0,0,openList[0].getSumOfPermInv(), openList[0].getState()])
		counter += 1 #this counts in how many moves it found the solution
		populateOpenList(openList, closeList)
		closeList.append(openList[0])
		openList.pop(0)
	print('cycles: ' + str(counter))
	print('cost: ' +  str(closeList[-1].getTotCost()))
	return state

def h1(puzzle):
	openList = []
	closeList = []
	search = []
	openList.append(puzzle) #appending the initial node

	while not closeList or not closeList[-1].isGoal(): #as long is it dosnt find the goal keep loopin
		search.append([0,0,openList[0].getSumOfPermInv(), openList[0].getState()])		
		populateOpenList(openList, closeList)
		closeList.append(openList.pop(0))
		openList.sort(key=lambda x : x.getSumOfPermInv()) #this sorts the list using sum of inv perm
	return search, closeList[-1].getSolution()
 
def h2(puzzle):
	openList = []
	closeList = []
	search = []
	openList.append(puzzle) #appending the initial node

	while not closeList or not closeList[-1].isGoal(): #as long is it dosnt find the goal keep loopin
		search.append([0,0,openList[0].getSumOfPermInv(), openList[0].getState()])		
		populateOpenList(openList, closeList)
		closeList.append(openList.pop(0))
		openList.sort(key=lambda x : x.getManhattanDist()) #this sorts the list using sum of inv perm
	return search, closeList[-1].getSolution()
#this function takes in an open list and closed list, checks the first element of the list and appends all avalable moves
#if they werent already either in the open list or closed list
def populateOpenList(openList, closeList):
	for x in openList[0].getMoves():
		p = copy.deepcopy(openList[0])
		p.move(x[0])
		if p.getState() not in [x.getState() for x in closeList] and p.getState() not in [x.getState() for x in openList]: #checks lists
			openList.append(p)


		
