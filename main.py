from puzzle import Puzzle
from gbfs import gbfs
import out

# 3 0 1 4 2 6 5 7
# 6 3 4 7 1 2 5 0
# 1 0 3 6 5 2 7 4
# puzzle = Puzzle([1, 0, 3, 6, 5, 2, 7, 4], 2, 4)
# puzzle = Puzzle([5, 0 ,8, 4, 2, 1, 7, 3, 6], 3,3)

# A.find_best(puzzle)

#puzzle = Puzzle([1, 0, 3, 7, 5, 2, 6, 4],2, 4)
#puzzle = Puzzle([0, 3, 1, 4, 2, 6, 5, 7], 2, 4)
puzzle = Puzzle([1, 0, 3, 7, 5, 2, 6, 4], 2, 4)

# out.solutionFile(gbfs(puzzle, 1)[1:], 'test')
out.searchFile(gbfs(puzzle, 1)[0], 'test')