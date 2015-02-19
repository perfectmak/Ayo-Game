
import copy
import random

from Node import Node
from Queue import Queue
# from Game import Game
from Player import Player

class TreeGen:
	"""docstring for TreeGen
		Generator of the Game tree from a specific node
	"""

	gameMatrix = [];
	maxHeight = 4; #height of the game tree
	matrixResults = [];
	maxGain = 0;

	def __init__(self, arg):
		self.arg = arg

	def maxMoveAndValue(matrix):
		hole = 0;
		goal = 0;
		for i in enumerate(matrix):
			for j in enumerate(i[1]):
				if(j[1] > goal):
					goal = j[1];
					hole = j[0];
		
		return (hole, goal);

	def getParentAtHeight(node, height):
	# 	mNode = copy.deepcopy(node);
		while (node.height != height) and (node.height != 0):
			node = node.parentNode;

		return node;



	def bestNode(node, player):
		# TreeGen.gameMatrix = [[0 for j in range(6)] for i in range(6)]
		TreeGen.matrixResults = [];
		frontier = Queue();
		node.height = 0;
		node.gameMatrix = [[0 for j in range(6)] for i in range(6)];
		frontier.put(node);

		# where player is Computer and should be evenPlayer
		if player == Player.B:
			oddPlayer = Player.A;
			evenPlayer = Player.B;
		else:
			oddPlayer = Player.B;
			evenPlayer = Player.A;

		while not frontier.empty():
			currentNode = frontier.get_nowait();
			# print("node:",currentNode.height,currentNode.gameState.board, currentNode.gain);

			if currentNode.height == TreeGen.maxHeight: #tree has exceeded max height to generate
				#extract max value from nodes game tree
				# TreeGen.matrixResults.append(TreeGen.maxMoveAndValue(currentNode.matrixResults));				
				if currentNode.gain > TreeGen.maxGain:
					TreeGen.maxGain = currentNode.gain;
					TreeGen.matrixResults = [TreeGen.getParentAtHeight(currentNode, 1)];
				elif currentNode.gain == TreeGen.maxGain:
					TreeGen.matrixResults.append(TreeGen.getParentAtHeight(currentNode, 1));
				continue;

			for i in range(6): #check thru all possible moves

				if (currentNode.height%2 == 1): #odd
					player = oddPlayer; 
				else:
					player = evenPlayer;

				response = currentNode.play(player, i);
			
				if response == None: #prun moves that don't exist
					continue;

				newNode = Node(response[0]);
				newNode.height = currentNode.height + 1;
				newNode.gameMatrix = currentNode.gameMatrix[:];
				newNode.parentNode = currentNode;
				computerHole = response[0].lastHole;

				# computer hole is in the range of 0 - 11
				# so converting it to range for game matrix
				if computerHole > 5:
					computerHole = 11 - computerHole;

				#update the gameMatrix
				if newNode.height%2 == 0: #computer playing					
					# TreeGen.gameMatrix[i][computerHole] += response[1]
					# newNode.gameMatrix[i][computerHole] += response[1]
					newNode.gain = currentNode.gain + response[1];
				else: #human playing
					# TreeGen.gameMatrix[i][computerHole] -= response[1]
					# newNode.gameMatrix[i][computerHole] -= response[1]
					newNode.gain = currentNode.gain - response[1];

				frontier.put(newNode);
		
		# get max value from gameMatrix:
		if len(TreeGen.matrixResults) > 0:
			nextHoleNode = random.choice(TreeGen.matrixResults);
		else:
			return			
				
		# print(TreeGen.gameMatrix);
		print("Computer selected:", nextHoleNode.gameState.lastHole);

		return node.play(player, nextHoleNode.gameState.lastHole);


	bestNode = staticmethod(bestNode);
	maxMoveAndValue = staticmethod(maxMoveAndValue);
	getParentAtHeight = staticmethod(getParentAtHeight);
