import copy
from puzzle import Puzzle

def ucs(puzzle):

    open_list=[]
    open_list.append(puzzle)
    closed_list =[]

    while not open_list[0].isGoal():
        #print(*open_list[0].puzzle)
        closed_list.append(open_list[0])
        moves = open_list[0].getMoves()

        for move in moves:
            p = copy.deepcopy(open_list[0])
            p.move(move[0])
            open_list.append(p)
        open_list.sort(key=lambda x: x.cost)

        open_list.pop(0)

    print(open_list[0].getSolution())

puzzle = Puzzle([1,0,3,7,5,2,6,4],2,4)
ucs(puzzle)
