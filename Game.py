
from GameState import GameState
from Node import Node
from Player import Player
from TreeGen import TreeGen
from GameUI import GameUI

class Game:
	"""docstring for Game"""
	CurrentState = None;
	Computer = None;
	ComputerGain = 0;
	Human = None;
	HumanGain = 0;
	UI = None;

	def __init__(self):
		self.loadGame();
		self.setup();
		self.start();

	def loadGame(self):
		print("Welcome to Ayo Olopon, the Game.");
		startBoard = [4 for i in range(12)];
		# startBoard = [8, 8, 2, 2, 0, 1, 6, 7, 7, 0, 0, 7]
		Game.CurrentState = GameState(startBoard, Player.NONE, -1);
		self.rootNode = Node(Game.CurrentState);

		Game.UI = GameUI(self);
		Game.UI.load();

	def start(self):
		self.printBoard();
		self.currentPlayer = Player.A
		Game.UI.start();

		# while True:
		# 	self.nextTurn();

	def printBoard(self):
		print("A",Game.CurrentState.board[:6]);
		b = Game.CurrentState.board[6:];
		b.reverse();
		print("B",b);

	def setup(self):
		"""Determine who will be Player A or Player B"""
		self.setPlayers(Player.A, Player.B);

	def getUserInput(self):
		return raw_input();

	def setPlayers(self, human, computer):
		Game.Human = human;
		Game.Computer = computer;

	def switchCurrentPlayer(self):
		if self.currentPlayer == Player.A:
			self.currentPlayer = Player.B
		else:
			self.currentPlayer = Player.A
		pass

	def nextTurn(self, hole):
		if self.currentPlayer == Game.Human:
			#human to play
			hole = int(hole);
			response = self.rootNode.play(self.currentPlayer, hole);
			if response == None:
				print("You cannot pick an empty hole");
				return False
			Game.HumanGain += int(response[1]);
		else:
			#computer to play
			response = TreeGen.bestNode(self.rootNode, self.currentPlayer);
			Game.ComputerGain += int(response[1]);
			# return;

		Game.CurrentState = response[0];
		self.rootNode = Node(response[0], response[1]);
		self.printBoard();
		self.switchCurrentPlayer();

		return True;