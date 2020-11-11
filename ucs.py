import copy
import time

def ucs(puzzle):
    start = time.time()
    open_list=[]
    open_list.append(puzzle)
    closed_list =[]

    while not open_list[0].isGoal():

        closed_list.append([0,open_list[0].getTotCost(),0,open_list[0].getState()])
        moves = open_list[0].getMoves()

        for move in moves:
            p = copy.deepcopy(open_list[0])
            p.move(move[0])
            open_list.append(p)
        open_list.sort(key=lambda x: x.cost)

        open_list.pop(0)

        now = time.time()
        if (now - start) > 60:
            return

    return closed_list, open_list[0].getSolution(),open_list[0].getTotCost(),now-start


