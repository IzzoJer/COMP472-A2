class Puzzle:
	#initializes the game board 
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.cost = 0

	#prints the curent state of the board
	def printState(self):
		print(*self.puzzle[:4], sep = "	")
		print(*self.puzzle[4:], sep = "	")

	def getCurrent(self):
		return self.puzzle	
	#returns the current total cost 
	def getTotCost(self):
		return self.cost

	#return true if puzzle is completed 
	def isGoal(self):
		if self.puzzle == self.getFinal():
			return True
		return False

	#returns final state
	def getFinal(self):
		return [1,2,3,4,5,6,7,0]

	#private function for swapping positions on the board
	def __swap(self, pos1, pos2):
		self.puzzle[pos1], self.puzzle[pos2] = self.puzzle[pos2], self.puzzle[pos1] 

	#swaps the 0 slot up or down and adds to cost
	def horizontalMove(self):
		pos = self.puzzle.index(0)
		if self.puzzle.index(0) < 4:
			self.__swap(pos, pos+4)
		else:
			self.__swap(pos, pos-4)
		self.cost += 1

	#moves 0 left and adds 1 to cost, if 0 is on the left edge then it wraps around and cost += 2
	def leftVerticalMove(self):
		pos = self.puzzle.index(0)
		if pos != 0 and pos != 4:
			self.__swap(pos, pos-1)
			self.cost += 1
		elif pos == 0:
			self.__swap(pos, 3)
			self.cost += 2
		elif pos == 4:
			self.__swap(pos, 7)
			self.cost += 2

	#moves 0 right and adds 1 to cost, if 0 is on the right edge then it wraps around and cost += 2
	def rightVerticalMove(self):
		pos = self.puzzle.index(0)
		if pos != 3 and pos != 7:
			self.__swap(pos, pos+1)
			self.cost += 1
		elif pos == 3:
			self.__swap(pos, 0)
			self.cost += 2
		elif pos == 7:
			self.__swap(pos, 4)
			self.cost += 2

	#moves the 0 diag left if 0 is in one of the corners and adds 3 to cost
	def leftDiagMove(self):
		pos = self.puzzle.index(0)
		if pos == 0 or pos == 4:
			self.__swap(pos, pos-1)
			self.cost += 3
		if pos == 3 or pos == 7:
			self.__swap(pos, (pos-5)%8)
			self.cost += 3

	##moves the 0 diag right if 0 is in one of the corners and adds 3 to cost
	def rightDiagMove(self):
		pos = self.puzzle.index(0)
		if pos == 0 or pos == 4:
			self.__swap(pos, (pos+5)%8)
			self.cost += 3
		if pos == 3 or pos == 7:
			self.__swap(pos, (pos+1)%8)
			self.cost += 3	

	def getSumOfPermInv(current):
	count = 0 
	for x in range(len(current)):
		for y in range(x+1,len(current)):
			if current[x] > current[y]:
				count += 1
	return count


	def getMoves(self):
		pos = self.puzzle.index(0)
		moves = []
		moves.append(('up', 1))
		if pos == 0 or pos == 4:
			moves.append(('left', 2))
			moves.append(('diagLeft', 3))
			moves.append(('diagRight', 3))
		else:
			moves.append(('Left', 1))
		if pos == 3 or pos == 7:
			moves.append(('right', 2))
			moves.append(('diagLeft', 3))
			moves.append(('diagRight', 3))
		else:
			moves.append(('right', 1))
		return moves

	def move(self, direction):
		if direction == 'up':
			self.horizontalMove()
		if direction == 'left':
			self.leftVerticalMove()
		if direction == 'right':
			self.rightVerticalMove()
		if direction == 'diagRight':
			self.rightDiagMove()
		if direction == 'diagLeft':
			self.leftDiagMove()


puzzle = Puzzle([3, 0, 1, 4, 2, 6, 5, 7])
puzzle.printState()
print(puzzle.getMoves())
puzzle.printState()
print(getSumOfPermInv(puzzle.getCurrent()))

