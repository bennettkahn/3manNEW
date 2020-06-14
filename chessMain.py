import chessbrain as cb
import chessGUI as gui
import playersAndGames as p

class Game():

	def __init__(self):
		# a list to store the players
		self.players = []
		# a clean Board object to play the Game on
		self.board = cb.Board()
		# a list to store moves played
		self.moves_played = []
	
	def initialize(self, p1: p.Player, p2: p.Player, p3: p.Player):
		# for now p1 is white
		self.players.append(p1)
		# p2 is gray
		self.players.append(p2)
		# p3 is black
		self.players.append(p3)
		self.turn_tracker = 0
		self.current_turn = self.players[self.turn_tracker]
		# clear all moves from list
		self.moves_played.clear()

		self.gui_game = gui.Gui()


	def main_loop(self):
		for i in range(1000):
			# draw board
			self.gui_game.draw(self.board)
			print("It is " + str(self.current_turn.color) + " turn.")
			move_tuple = self.gui_game.get_user_input(self.board, self.current_turn)
			# store move
			self.moves_played.append(p.Move(self.current_turn, *move_tuple))
			# check if any moats are in need of bridging
			self.board.bridge_moats_check()
			# increment turn_tracker
			self.turn_tracker = (self.turn_tracker + 1) % 3
			# set current_turn to next player
			self.current_turn = self.players[self.turn_tracker]


	def is_checkmate(self):
		pass


main_game = Game()
main_game.initialize(p.Player(True, 'w'), p.Player(True, 'g'), p.Player(True, 'b'))
main_game.main_loop()



