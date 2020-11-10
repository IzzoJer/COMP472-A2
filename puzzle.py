import a_star as A
import gbfs

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
        if self.puzzle == self.getFinal()[0] or self.puzzle == self.getFinal()[1]:
            return True
        return False

    #returns final state
    def getFinal(self):
        l = list(range(self.width * self.height))
        l.append(l.pop(0))
        l2 = []
        for x in range(len(self.puzzle)):
            if x % 2 != 0:
                l2.append(x)
        for x in range(len(self.puzzle)):
            if x % 2 == 0:
                l2.append(x)
        l2.append(l2.pop(l2.index(0)))
        return l, l2

    #private function for swapping positions on the board
    def __swap(self, pos1, pos2):
        self.puzzle[pos1], self.puzzle[pos2] = self.puzzle[pos2], self.puzzle[pos1] 

    #swaps the 0 slot up or down and adds to cost
    def upVerticalMove(self):
        pos = self.puzzle.index(0)
        w = self.width

        self.__swap(pos, pos-w)
        self.cost += 1

    def downVerticalMove(self):
        pos = self.puzzle.index(0)
        w = self.width

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
        count2 = 0
        current = self.puzzle
        for x in current:
            remain = current[current.index(x)+1:]
            f1 = self.getFinal()[0]
            f2 = self.getFinal()[1]
            f1 = f1[:f1.index(x)]
            f2 = f2[:f2.index(x)]
            for x in remain:
                if x in f1:
                    count += 1
                if x in f2:
                    count2 += 1
        return min(count, count2)

    def getManhattanDist(self):
        total_dist = [0,0]
        puzzle = self.getState()
        for x in range(2):
            final_puzzle = self.getFinal()[x]
            w = self.width
            i=0
            for tile in puzzle:
                if tile == 0:
                    i += 1
                    continue

                row_pos = int(i/w)
                col_pos = i % w

                j = final_puzzle.index(tile)
                
                row_final = int(j/w)
                col_final = j % w

                dist_row = abs(row_pos - row_final)
                dist_col = abs(col_pos - col_final)

                total_dist[x] += dist_row + dist_col
                i+= 1
        print(total_dist[0], total_dist[1])
        return min(total_dist[0], total_dist[1])


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
        moves.append(('down', 1))

        if top_l <= pos <= top_r:
            moves.remove(('up', 1))
        elif bottom_l <= pos <= bottom_r:
            moves.remove(('down', 1))

        if pos == top_l or pos == bottom_l:
            moves.append(('left', 2))
            moves.append(('diagLeft', 3))
            moves.append(('diagRight', 3))
        else:
            moves.append(('left', 1))
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
        if direction == 'down':
            self.downVerticalMove()
        if direction == 'left':
            self.leftHorizontalMove()
        if direction == 'right':
            self.rightHorizontalMove()
        if direction == 'diagRight':
            self.rightDiagMove()
        if direction == 'diagLeft':
            self.leftDiagMove()

# 3 0 1 4 2 6 5 7
# 6 3 4 7 1 2 5 0
# 1 0 3 6 5 2 7 4
# puzzle = Puzzle([1, 0, 3, 6, 5, 2, 7, 4], 2, 4)
# puzzle = Puzzle([5, 0 ,8, 4, 2, 1, 7, 3, 6], 3,3)

# A.find_best(puzzle)

#puzzle = Puzzle([1, 0, 3, 7, 5, 2, 6, 4],2, 4)
puzzle = Puzzle([0, 3, 1, 4, 2, 6, 5, 7], 2, 4)
#puzzle = Puzzle([5, 0, 8, 4, 2, 1, 7, 3, 6], 2, 3)
puzzle.getManhattanDist()
gbfs.gbfs(puzzle)

