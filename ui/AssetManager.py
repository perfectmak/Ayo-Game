
import os

class AssetManager:
	"""docstring for AssetManager"""

	AssetPath = os.getcwd()+"/ui/assets/"

	def __init__(self):
		pass

	def img(name):
		return AssetManager.AssetPath + "img/" + name;

	def font(name):
		return AssetManager.AssetPath + "font/" + name;

	img = staticmethod(img);
	font = staticmethod(font);
		