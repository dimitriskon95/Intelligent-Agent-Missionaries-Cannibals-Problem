"""Missionaries and Cannibals problem"""

from search import * # This file imports utils.py so it should be in the same folder
import sys # System-specific parameters and functions

class MissionariesAndCannibals(Problem) :
	"""Subclass of search.Problem"""
	
	def __init__(self) :
		"""Sets initial state and goal.
		States are representated as a tuple (m, c, b) where
		m is the number of missionaries in left(starting) bank, 
		c is the number of cannibals in left(ending) bank and
		b is the position of the boat (left or right bank)"""
		super(MissionariesAndCannibals, self).__init__((3, 3, 'left'), (0 , 0 , 'right'))
#_______________________________________________________________
	
	def __isValidState(self, m, c) :
		"""Checks if a state is valid. """
		if m < 0 or c < 0 : # Error ! 
			return False
		if m > 3 or c > 3 : # Error !
			return False	
		if m > c and m != 3 : # There are both cannibals and missionaries in right bank but cannibals are more
			return False
		if m < c and m != 0 : # There are both cannibals and missionaries in left bank but cannibals are more
			return False
		return True
#_______________________________________________________________

	def actions(self, state) :
		"""Returns the actions that can be executed in the state"""
		# possibleActions are all actions that may be executed, but some of 
		# them may lead in invalid state. So possibleActions should be filtered
		possibleActions = [(1, 1), (1, 0), (2, 0), (0,1), (0,2)]
		validActions = [] # It will store only actions that lead in a valid state
		if state[2] == 'left' :
			for possibleAction in possibleActions :
				m = state[0] - possibleAction[0]
				c = state[1] - possibleAction[1]
				if self.__isValidState(m, c) :
					validActions.append(possibleAction)
		else : # right
			for possibleAction in possibleActions :
				m = state[0] + possibleAction[0]
				c = state[1] + possibleAction[1]
				if self.__isValidState(m, c) :
					validActions.append(possibleAction)
#		print len(validActions)
#		for validAction in validActions :
#			print "\t", validAction, self.result(state, validAction)
#			raw_input("pause")
		return validActions
#_______________________________________________________________

	def result(self, state, action) :
		""""""
		m = state[0]
		c = state[1]
		b = state[2]
		if b == 'left' :
			m = state[0] - action[0]
			c = state[1] - action[1]
			b = 'right'
		else : # right
			m = state[0] + action[0]
			c = state[1] + action[1]
			b = 'left'
		
		return (m, c, b)
