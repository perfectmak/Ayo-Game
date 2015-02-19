
from BoardScene import BoardScene;
from HomeScene import HomeScene;

class SceneManager:
	BoardScene = "board";
	HomeScene = "home";

	"""docstring for SceneManager"""
	def __init__(self):
		pass;

	def getScene(scene, surface):
		if scene == SceneManager.HomeScene:
			scene = HomeScene();
		if scene == SceneManager.BoardScene:
			scene = BoardScene();
		
		scene.load(surface);
		return scene;

	getScene = staticmethod(getScene)


		