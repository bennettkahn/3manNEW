import chessbrain as cb
import enum

class Player():

	def __init__(self, is_human, color, name):
		self.is_human = is_human
		self.color = color
		self.name = name


class Move():
	def __init__(self, player: Player, start: cb.Spot, end: cb.Spot):
		self.player = player
		self.start = start
		self.end = end
		self.piece_moved = start.Piece
		self.piece_killed = None
'''
class GameStatus(enum.Enum):
	active = 1
	white_win = 2
	gray_win = 3
	blck_win = 4
	forfeit = 5
	stalemate = 6
'''