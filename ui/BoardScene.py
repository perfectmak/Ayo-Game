import pygame
from pygame.locals import *

import Game
import AAfilledRoundedRect as AAFRR

class BoardScene:
	"""docstring for BoardScene"""
	def __init__(self):
		self.boardColor = (189, 133, 76)
		self.circleColor = (255,255,255)
		self.circleRadius = 35;
		self.halfRadius = self.circleRadius/2

		self._seedFont = pygame.font.SysFont("Calibri", 30);
		self._textFont = pygame.font.SysFont("Calibri", 40);

		self.playerA = "Player A";
		self.playerB = "Player B (Computer)";

		self.startx = 70
		self.starty = 50
		self.boardWidth = 500
		self.boardHeight = 250;
		self.updateText = "";
		self.computerScore = "";
		self.humanScore = "";
		# self._seedFont = pygame.font.Font(AM.font("EmpireStateDeco.ttf"), 10);
		pass

	def load(self, surface):
		self._surface = surface;

		self.boardSurface = pygame.Surface((500,250))
		self.boardSurface.fill(self.boardColor);

		self.holeSurface = pygame.Surface((self.circleRadius+10, self.circleRadius+10));
		self.holeSurface.fill((255,255,255));

		background = pygame.Surface(self._surface.get_size())
		self.background = background.convert()
		self.background.fill((250, 250, 250))

		self._surface.blit(self.background, (0,0));

	def onRender(self):
		self._surface.blit(self.background, (0,0));
		#draw Board
		gameState = Game.Game.CurrentState;
		startx = self.startx
		starty =self.starty
		width = self.boardWidth
		height = self.boardHeight

		AAFRR.AAfilledRoundedRect(self.boardSurface,(0, 0, width, height),self.boardColor,1.0)
		self._surface.blit(self.boardSurface, [startx, starty]);

		playerA = self._seedFont.render(self.playerA, 1, [0,0,0]);
		self._surface.blit(playerA, [(startx+width/2) - self._textFont.size(self.playerA)[0]/2, starty-10 - self._textFont.size(self.playerA)[1]/2])		

		playerB = self._seedFont.render(self.playerB, 1, [0,0,0]);
		self._surface.blit(playerB, [(startx+width/2) - self._textFont.size(self.playerB)[0]/2, starty+height+20 - self._textFont.size(self.playerB)[1]/2])		

		self.holeRange = [];
		for i in range(2):
			for j in range(6):
				x = startx+self.circleRadius+((self.circleRadius+6)*j*2)+10
				y = starty+self.circleRadius+((self.circleRadius+20)*2*i)+25

				pygame.draw.circle(self._surface, self.circleColor, (x,y), self.circleRadius, 0)

				#to store the bounds of the drawn circle
				self.holeRange.append(((x-self.circleRadius, x+self.circleRadius),(y-self.circleRadius, y+self.circleRadius)));

				if (i == 1):
					seedPos = 11-j
				else:
					seedPos = j;

				seed = str(gameState.board[seedPos]);
				count = self._seedFont.render(seed, 1, [0,0,0]);
				self._surface.blit(count, [x - self._seedFont.size(seed)[0]/2,y - self._seedFont.size(seed)[1]/2])

		#show game status
		update = self._seedFont.render(self.updateText, 1, [0,0,0]);
		self._surface.blit(update, [(startx+width/2) - self._textFont.size(self.playerB)[0]/2, 380 - self._textFont.size(self.playerB)[1]/2])		

		aSeeds = self._seedFont.render(self.humanScore, 1, [0,0,0]);
		self._surface.blit(aSeeds, [10, 10])	

		bSeeds = self._seedFont.render(self.computerScore, 1, [0,0,0]);
		self._surface.blit(bSeeds, [self._surface.get_size()[0]- self._textFont.size(self.computerScore)[0], 10])	

	def onLoop(self):
		pass

	def onEvent(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button == 1): #1 is left
				#determine the location clicked
				pos = pygame.mouse.get_pos();
				for i in enumerate(self.holeRange):
					if (pos[0] >= i[1][0][0]) and (pos[0] <= i[1][0][1]):
						if (pos[1] >= i[1][1][0]) and (pos[1] <= i[1][1][1]):
							if (i[0] > 5):
								seedPos = 6+ (11 - i[0])
							else:
								seedPos = i[0];

							self.play(seedPos);
							print(seedPos, "clicked");

				pass

	def play(self, hole):
		if (Game.Game.UI.Game.currentPlayer == Game.Game.Human):
			if(hole > 5):
				print("Illegal move");
			else:
				if Game.Game.UI.Game.nextTurn(hole): #human playes
					Game.Game.UI.Game.nextTurn(hole); # then computer plays next
					#update last played view
					lastHole = 11 - Game.Game.UI.Game.CurrentState.lastHole;
					self.updateText = "Computer Played Hole:" + str(lastHole+1);

					self.humanScore = "A Seeds: " + str(Game.Game.UI.Game.HumanGain);
					self.computerScore = "B Seeds : " + str(Game.Game.UI.Game.ComputerGain);