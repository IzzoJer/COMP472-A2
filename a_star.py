from copy import deepcopy
import heapq as hq

class Node:

    def __init__(self, puzzle, parent=None):
        self.current_state = puzzle
        self.g = 0
        self.h = 0
        self.f = 0
        self.movement_cost = 0
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def computeChildren(self):
        puzzle = deepcopy(self.current_state)
        moves = puzzle.getMoves()
        children = []
        
        for direction, cost in moves:
            p = deepcopy(puzzle)
            p.move(direction)
            node = Node(p, parent=self)
            node.movement_cost = cost
            children.append(node)
            # print(f"Heuristic cost of {direction}: {h_1(p)}")
        children.sort()
        self.children = children
        return children


def h_0(puzzle):

    if puzzle.getState()[-1] == 0:
        return 0

    return 1

def h_1(puzzle):
    return puzzle.getSumOfPermInv() 

def contains(node, _list):
    state = node.current_state.getState()

    for node in _list:
        if node.current_state.getState() == state:
            return True

    return False

def add_to_open(open_list, node):
    for n in open_list:
        if n.current_state.getState() == node.current_state.getState() and node.f > n.f:
            return False
    return True

def is_goal(node):
    goal = list(range(8))
    goal.append(goal.pop(0))

    return node.current_state.getState() == goal

def print_moves(node):
    out = []

    while node.parent != None:
        out.insert(0,node)
        node = node.parent

    for n in out:
        print(n.current_state.printState())
        print('')

def find_best(puzzle):
    open_list = []
    closed_list = []

    node = Node(puzzle)
    open_list.append(node)

    while open_list != []:
        open_list.sort(key=lambda x: x.f)
        current_node = open_list.pop(0)
        closed_list.append(current_node)

        if is_goal(current_node):
            print(f"Found solution with cost of {current_node.g}")
            print_moves(current_node)
            break

        children = current_node.computeChildren()

        for child_node in children:
            in_closed = contains(child_node, closed_list)
            in_open = contains(child_node, open_list)

            if not in_closed:
                child_node.g = current_node.g + child_node.movement_cost
                child_node.h = h_1(child_node.current_state)
                child_node.f = child_node.g + child_node.h

                if add_to_open(open_list, child_node):
                    open_list.append(child_node)
                    
