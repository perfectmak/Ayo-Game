from Player import Player
from GameState import GameState

class Node:
	"""docstring for Node"""
	def __init__(self, gameState, gain = 0):
		self._gameState = gameState;
		self._gain = gain
		self._parentNode = None;

	"""
    Generates a new GameState when the hole is played by player
    """
	def play(self, player, hole):
		if player == Player.A:
			hole = hole;
		else:
			hole = 11 - hole

		if self.gameState.board[hole] == 0:
			return None;

		seeds = self.gameState.board[hole];
		newBoard = [i for i in self.gameState.board];
		newBoard[hole] = 0;
		selectedHole = hole;
		for i in range(seeds):
			selectedHole = self.nextHole(selectedHole)
			if(hole == selectedHole):
				continue
			newBoard[selectedHole] = newBoard[selectedHole]+1;

		gain = 0;

		#cleanup
		while True:
			if GameState.isCapturable(newBoard[selectedHole]) and Player.canCapture(player, selectedHole):
				gain += newBoard[selectedHole];
				newBoard[selectedHole] = 0
			else:
				break;

			selectedHole = self.prevHole(selectedHole)

		self._gain = gain;

		return (GameState(newBoard, player, hole), gain);

	# in anticlockwise direction
	def nextHole(self, hole):
		if hole == 0:
			return 11;
		else:
			return hole - 1;

	# in clockwise direction
	def prevHole(self, hole):
		if hole == 11:
			return 0;
		else:
			return hole + 1;

	@property
	def gain(self):
	    return self._gain
	@gain.setter
	def gain(self, value):
	    self._gain = value
	
	@property
	def gameMatrix(self):
	    return self._gameMatrix
	@gameMatrix.setter
	def gameMatrix(self, value):
	    self._gameMatrix = value
	

	@property
	def parentNode(self):
	    return self._parentNode

	@parentNode.setter
	def parentNode(self, value):
	    self._parentNode = value
	

	@property
	def gameState(self):
	    return self._gameState
	@gameState.setter
	def gameState(self, value):
	    self._gameState = value

	@property
	def height(self):
	    return self._height
	@height.setter
	def height(self, value):
	    self._height = value
	
	
		