import a_star as A

class Puzzle:
    #initializes the game board 
    def __init__(self, puzzle, height, width):
        self.puzzle = puzzle
        self.height = height
        self.width = width
        self.cost = 0

    #prints the curent state of the board
    def printState(self):
        for i in range(self.height):
            w = self.width
            print(*self.puzzle[i*w:(i+1)*w], sep = " ")

    def getState(self):
        return self.puzzle

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
        l = list(range(self.width * self.height))
        l.append(l.pop(0))
        return l

    #private function for swapping positions on the board
    def __swap(self, pos1, pos2):
        self.puzzle[pos1], self.puzzle[pos2] = self.puzzle[pos2], self.puzzle[pos1] 

    #swaps the 0 slot up or down and adds to cost
    def upVerticalMove(self):
        pos = self.puzzle.index(0)
        w = self.width
        h = self.height

        if pos + w > len(self.getState()):
            self.__swap(pos, (pos+w)%w)
        else:
            self.__swap(pos, pos+w)

        self.cost += 1

    #moves 0 left and adds 1 to cost, if 0 is on the left edge then it wraps around and cost += 2
    def leftHorizontalMove(self):
        pos = self.puzzle.index(0)
        w = self.width

        if pos % w == 0:
            self.__swap(pos, pos + w - 1)
            self.cost += 2
        else:
            self.__swap(pos, pos-1)

    #moves 0 right and adds 1 to cost, if 0 is on the right edge then it wraps around and cost += 2
    def rightHorizontalMove(self):
        pos = self.puzzle.index(0)
        w = self.width

        if pos % w == w - 1:
            self.__swap(pos, pos - w + 1)
            self.cost += 2
        else:
            self.__swap(pos, pos+1)

    #moves the 0 diag left if 0 is in one of the corners and adds 3 to cost
    def leftDiagMove(self):
        pos = self.puzzle.index(0)
        w = self.width
        h = self.height

        top_l = 0
        bottom_l = w*(h-1)
        top_r = w-1
        bottom_r = w*h-1

        if pos == top_l:
            self.__swap(pos, bottom_r)
        elif pos == bottom_l:
            self.__swap(pos, top_r)
        elif pos == top_r:
            self.__swap(pos, pos + w -1)
        elif pos == bottom_l:
            self.__swap(pos, pos - w -1)
        self.cost +=3



    ##moves the 0 diag right if 0 is in one of the corners and adds 3 to cost
    def rightDiagMove(self):
        pos = self.puzzle.index(0)
        w = self.width
        h = self.height

        top_l = 0
        bottom_l = w*(h-1)
        top_r = w-1
        bottom_r = w*h-1

        if pos == top_l:
            self.__swap(pos, pos + w + 1)
        elif pos == bottom_l:
            self.__swap(pos, pos - w + 1)
        elif pos == top_r:
            self.__swap(pos, bottom_l)
        elif pos == bottom_r:
            self.__swap(pos, top_l)
        self.cost += 3

    def getSumOfPermInv(self):
        count = 0 
        current = self.puzzle
        for x in range(len(current)):
            for y in range(x+1,len(current)):
                if current[x] > current[y]:
                    count += 1
        return count

    def getManhattanDist(self):
        total_dist = 0
        puzzle = self.getState()
        final = self.getFinal()
        i=0
        dist_row = 0
        for tile in final:
            j = 0
            for t in puzzle:
                if t == tile:
                    dist_col = j%4 #width
                    total_dist += dist_row + dist_col
                    dist_row = 0
                    break 
                j += 1
            i += 1
            dist_row += 1 if i %2 == 0 else 0

        return total_dist


    def getMoves(self):
        pos = self.puzzle.index(0)
        w = self.width
        h = self.height
        top_l = 0
        bottom_l = w*(h-1)
        top_r = w-1
        bottom_r = w*h-1

        moves = []
        moves.append(('up', 1))
        if pos == top_l or pos == bottom_l:
            moves.append(('left', 2))
            moves.append(('diagLeft', 3))
            moves.append(('diagRight', 3))
        else:
            moves.append(('Left', 1))
        if pos == top_r or pos == bottom_r:
            moves.append(('right', 2))
            moves.append(('diagLeft', 3))
            moves.append(('diagRight', 3))
        else:
            moves.append(('right', 1))

        moves.sort(key=lambda tup: tup[1])
        return moves

    def move(self, direction):
        if direction == 'up':
            self.upVerticalMove()
        if direction == 'left':
            self.leftHorizontalMove()
        if direction == 'right':
            self.rightHorizontalMove()
        if direction == 'diagRight':
            self.rightDiagMove()
        if direction == 'diagLeft':
            self.leftDiagMove()


puzzle = Puzzle([0, 3, 1, 4, 2, 6, 5, 7], 2, 4)
puzzle.printState()
print(puzzle.getManhattanDist())
# print(puzzle.getFinal())
# A.find_best(puzzle)


