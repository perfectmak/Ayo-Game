import pygame
from pygame.locals import *

import Buttons
from AssetManager import AssetManager as AM
from SceneManager import SceneManager as SM


class GameUI:
	"""docstring Interface class """
	Width = 640
	Height = 400

	def __init__(self, game):
		self._running = True;
		self._display = None;
		self.size = self.width, self.height = GameUI.Width, GameUI.Height
		self.Game = game;

	def load(self):
		pygame.init();
		self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF);		
		self.currentScene = SM.getScene(SM.HomeScene, self._display);

		self._running = True

	def onEvent(self, event):
		self.currentScene.onEvent(event);
		if event.type == pygame.QUIT:
			self._running = False

	def onLoop(self):
		self.currentScene.onLoop();
		pass;

	def onRender(self):
		self.currentScene.onRender();

		pygame.display.update();
		pass

	def cleanUp(self):
		pygame.quit();

	def start(self):
		print("start");
		while(self._running):
			for event in pygame.event.get():
				self.onEvent(event);
			self.onLoop();
			self.onRender();
		self.cleanUp();
		