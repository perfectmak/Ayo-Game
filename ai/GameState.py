

class GameState:
	"""
	docstring for GameState
	This is used to model the state of the game at a particular time

	_board is in this structure
	A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6
	0  1  2  3  4  5  6  7  8  9  10 11
	"""
	def __init__(self, board, lastPlayer, lastHole):
		#init board
		self._board = board;
		self._player = lastPlayer;
		self._lastHole = lastHole;


	@property
	def player(self):
	    return self._player
	@player.setter
	def player(self, value):
	    self._player = value

	@property
	def board(self):		
	    return self._board
	@board.setter
	def board(self, value):
	    self._board = value

	@property
	def lastHole(self):
	    return self._lastHole
	@lastHole.setter
	def lastHole(self, value):
	    self._lastHole = value
	

	def isCapturable(seeds):
		if (seeds == 2) or (seeds == 3):
			return True;
		else:
			return False;

	isCapturable = staticmethod(isCapturable);