from puzzle import Puzzle
from gbfs import gbfs
from ucs import ucs
import out
import random

# A.find_best(puzzle)

puzzNum = 2
#puzzle = Puzzle([1, 0, 3, 7, 5, 2, 6, 4],2, 4)
#puzzle = Puzzle([0, 3, 1, 4, 2, 6, 5, 7], 2, 4)
puzzle = Puzzle([1, 0, 3, 7, 5, 2, 6, 4], 2, 4)

# gbfs_h0 = gbfs(puzzle, 0) 
# gbfs_h1 = gbfs(puzzle, 1)
# gbfs_h2 = gbfs(puzzle, 2)

#Output

#READ
#	****look at my return function in gbfs for details on the parameters of the output file functions**********
#	search takes in a list of lists per itteration so i append a list of [score, score, score, currentState] at each itteration for search
#	solution file takes in the (finalNode.getSolution(), finalScore, time) is a tuple,
#	I returned everything i needed when i call my fucntion so everyting is avalable for calling 

# out.solutionFile(gbfs_h1[1:], f'{puzzNum}_gbfs-h1_solution')
# out.searchFile(gbfs_h1[0], f'{puzzNum}_gbfs-h1_search')
# out.solutionFile(gbfs_h2[1:], f'{puzzNum}_gbfs-h2_solution')
# out.searchFile(gbfs_h2[0], f'{puzzNum}_gbfs-h2_search')
#out.solutionFile(ucs(puzzle)[1:], f'{puzzNum}_ucs_solution')
#out.searchFile(ucs(puzzle)[0], f'{puzzNum}_ucs_search')

#Analysis

puzzles =[]
with open('puzzles.txt', 'w')as f:
	puzz = [1,2,3,4,5,6,7,0]
	for x in range(50):
		random.shuffle(puzz)
		f.write(str(puzz) + '\n')
		puzzles.append(puzz)

#for x in puzzles:
#	p = Puzzle(x, 2, 4)
#	ucs(p)