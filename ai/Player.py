
class Player:
	"""This is basically an enum for player representation"""
	A = "A";
	B = "B";
	NONE = "";
	aSeeds = 0;
	bSeeds = 0;

	def canCapture(player, hole):
		if (hole > 5) and (player == Player.A):
			return True
		elif (hole < 6) and (player == Player.B):
			return True
		else:
			return False

	canCapture = staticmethod(canCapture);
		