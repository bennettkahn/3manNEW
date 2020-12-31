import chessbrain as cb
import chessGUI as gui
import playersAndGames as p
import tkSetUp as t
from tkinter import *

class Game():

	def __init__(self):
		# a list to store the players
		self.players = []
		# a clean Board object to play the Game on
		self.board = cb.Board()
		# a list to store moves played
		self.moves_played = []
	
	def initialize(self):
		self.initial_gui = t.TkinterSetUp()
		self.game_options = self.initial_gui.send_data()



		# for now p1 is white
		self.players.append(p.Player(True, 'w', self.game_options[0]))
		# p2 is gray
		self.players.append(p.Player(True, 'g', self.game_options[2]))
		# p3 is black
		self.players.append(p.Player(True, 'b', self.game_options[4]))
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
			# see if the Player's King is in check before executing their move
			check_before_move = False
			# this will get us the Spot of the current Player's King
			curr_king_spot = self.board.get_spot_of_piece(self.current_turn.color, 'k')
			c = curr_king_spot.is_check(self.board, self.current_turn.color)
			# if the Player's King is in check
			if c:
				print("Your King is in Check! Move him!!!!")
				check_before_move = True
				# we check if it is checkmate when the Player's King is in check
				if self.is_checkmate(curr_king_spot, c):
					print('\nCHECKMATE! for ' + self.current_turn.color + '\n')
					removed = self.current_turn
					# increment turn_tracker
					self.turn_tracker = (self.turn_tracker + 1) % len(self.players)
					self.players.remove(removed)
					if removed.color == 'w' or removed.color == 'g':
						self.turn_tracker -= 1
					# set current_turn to next player
					self.current_turn = self.players[self.turn_tracker]
					print(self.turn_tracker)
					print(self.current_turn.color)
					continue
			move_tuple = self.gui_game.get_user_input(self.board, self.current_turn, check_before_move)
			# store move
			self.moves_played.append(p.Move(self.current_turn, *move_tuple))
			# check if any moats are in need of bridging
			self.board.bridge_moats_check()
			# increment turn_tracker
			self.turn_tracker = (self.turn_tracker + 1) % len(self.players)
			# set current_turn to next player
			self.current_turn = self.players[self.turn_tracker]


	def is_checkmate(self, curr_king_spot, curr_threats):
		for end_spot in curr_king_spot.Piece.possible_moves(self.board):
			print(end_spot.ring, end_spot.pos)
			if end_spot.is_check(self.board, self.current_turn.color) == False:
				return False
		num_threats = len(curr_threats)
		same_color_pieces = []
		for i in range(6):
			for j in range(24):
				if self.board.board[i][j].Piece != None:
					if self.board.board[i][j].Piece.color == self.current_turn.color:
						same_color_pieces.append(self.board.board[i][j].Piece)
		for threat in curr_threats:
			print(threat)
			for spot in threat[3]:
				print("spot: %d %d" % (spot.ring, spot.pos))
				for piece in same_color_pieces:
					if piece.piece_tag != 'k':
						if spot in piece.possible_moves(self.board):
							print("You can move your %s to Spot (%d, %d) in order to save your king!" % (piece.piece_tag, spot.ring, spot.pos))
							return False

		return True


main_game = Game()
main_game.initialize()
main_game.main_loop()



