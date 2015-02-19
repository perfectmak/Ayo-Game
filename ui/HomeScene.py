import pygame
from pygame.locals import *
import Game

import Buttons
from AssetManager import AssetManager as AM
import SceneManager as SM

class HomeScene:
	"""docstring for HomeScene"""
	def __init__(self):
		pass

	def load(self, surface):
		self._surface = surface;
		self.size = self.width, self.height = self._surface.get_size();

		self._titleFont = pygame.font.Font(AM.font("EmpireStateDeco.ttf"), 60);
		self._title = "Ayo Olopon";

		pygame.display.set_caption("Ayo Olopon")
		self._gameBg = pygame.image.load(AM.img("game_bg.jpg")).convert();

		self._startButton = Buttons.Button();

	def onRender(self):
		self._surface.blit(self._gameBg, [0,0]);

		title = self._titleFont.render(self._title, 1, [0,0,0]);
		self._surface.blit(title, [self.width/2 - self._titleFont.size(self._title)[0]/2,50])

		self._startButton.create_button(self._surface, [34,55,66], self.width/2 - 250/2, self.height/2, 250, 100, 60, "Start Game", [255,255,255]);

	def onLoop(self):
		pass

	def onEvent(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (event.button == 1): #1 is left
				if self._startButton.pressed(pygame.mouse.get_pos()):
					Game.Game.UI.currentScene = SM.SceneManager.getScene(SM.SceneManager.BoardScene, self._surface);
					print("start clicked");

