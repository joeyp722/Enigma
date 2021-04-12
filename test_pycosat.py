# SAT solver functions

import pycosat

cnf = [[5],[-4,1],[-4,2],[4,-1,-2],[-5,4,3],[5,-4],[5,-3]]
solution = pycosat.solve(cnf)
print(solution)
