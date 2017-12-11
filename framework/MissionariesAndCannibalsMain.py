from MissionariesAndCannibals import *

p = MissionariesAndCannibals()
def h1(n) :
	"""A simple heuristic, not a good one, but it works"""
	return 1
#s = breadth_first_search(p)
#s = depth_first_tree_search(p)
s = astar_search(p,h1)
sol = s.solution() # The sequence of actions to go from the root to this node
path = s.path() # The nodes that form the path from the root to this node
print "Solution: \n+{0}+\n|Action\t|State\t	\t|Path Cost |\n+{0}+".format('-'*42)
for i in range(len(path)) :
	state = path[i].state
	cost = path[i].path_cost
	action = " "
	if i > 0 : # The initial state has not an action that results to it
		action = sol[i-1]
	print "|{0}\t|{1} \t|{2} \t   |".format(action, state, cost)
print "+{0}+".format('-'*42)

