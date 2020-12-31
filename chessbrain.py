import time

class Board:
	"""
	The class to represent a chess board

	***

	Attributes
	----------
	* board:  
			# our chess board is stored as a list with 6 sublists
			# each sublist represents an 'ring' of the board, with the first being the outermost ring
			# each sublist has 24 elements, each representing a spot on the board
			# Spot with NoneType piece indicates to piece in that spot
			# an occupied spot will have a Spot class object at its respective spot


	Methods
	-------
	* get_space(x, y):
	* set_board()
	*
	"""


	def __init__(self):
		self.board = [[0 for j in range(24)] for i in range(6)]
		# moat between white and gray
		self.moat_0_bridged = False
		# moat between gray and black
		self.moat_1_bridged = False
		# moat between black and white
		self.moat_2_bridged = False
		self.set_board()


	def get_space(self, x, y):
		"""
		Parameters
		----------
		x: int (0, 5)
			The 'ring' of the circle; ring 0 being the outermost ring of the circle, ring 5 being the innermost
		y: int (0,23)
			The space along the circular board; begins with 0, the leftmost white pieces, and ends with 23, the rightmost gray piece
		"""

		try:
			return self.board[x][y]
		except:
			print("Index out of bound")


	def set_board(self):
		""" Sets the board with all pieces to starting position."""

		# initialize all white pieces
		self.board[0][0] = Spot(0, 0, Rook('w', 'r'))
		self.board[0][1] = Spot(0, 1, Knight('w', 'kn'))
		self.board[0][2] = Spot(0, 2, Bishop('w', 'b'))
		self.board[0][3] = Spot(0, 3, King('w', 'k'))
		self.board[0][4] = Spot(0, 4, Queen('w', 'q'))
		self.board[0][5] = Spot(0, 5, Bishop('w', 'b'))
		self.board[0][6] = Spot(0, 6, Knight('w', 'kn'))
		self.board[0][7] = Spot(0, 7, Rook('w', 'r'))

		self.board[1][0] = Spot(1, 0, Pawn('w', 'p0'))
		self.board[1][1] = Spot(1, 1, Pawn('w', 'p1'))
		self.board[1][2] = Spot(1, 2, Pawn('w', 'p2'))
		self.board[1][3] = Spot(1, 3, Pawn('w', 'p3'))
		self.board[1][4] = Spot(1, 4, Pawn('w', 'p4'))
		self.board[1][5] = Spot(1, 5, Pawn('w', 'p5'))
		self.board[1][6] = Spot(1, 6, Pawn('w', 'p6'))
		self.board[1][7] = Spot(1, 7, Pawn('w', 'p7'))


		# initialize all black pieces
		self.board[0][8] = Spot(0, 8, Rook('b', 'r'))
		self.board[0][9] = Spot(0, 9, Knight('b', 'kn'))
		self.board[0][10] = Spot(0, 10, Bishop('b', 'b'))
		self.board[0][11] = Spot(0, 11, King('b', 'k'))
		self.board[0][12] = Spot(0, 12, Queen('b', 'q'))
		self.board[0][13] = Spot(0, 13, Bishop('b', 'b'))
		self.board[0][14] = Spot(0, 14, Knight('b', 'kn'))
		self.board[0][15] = Spot(0, 15, Rook('b', 'r'))

		self.board[1][8] = Spot(1, 8, Pawn('b', 'p0'))
		self.board[1][9] = Spot(1, 9, Pawn('b', 'p1'))
		self.board[1][10] = Spot(1, 10, Pawn('b', 'p2'))
		self.board[1][11] = Spot(1, 11, Pawn('b', 'p3'))
		self.board[1][12] = Spot(1, 12, Pawn('b', 'p4'))
		self.board[1][13] = Spot(1, 13, Pawn('b', 'p5'))
		self.board[1][14] = Spot(1, 14, Pawn('b', 'p6'))
		self.board[1][15] = Spot(1, 15, Pawn('b', 'p7'))


		# initialize all gray pieces
		self.board[0][16] = Spot(0, 16, Rook('g', 'r'))
		self.board[0][17] = Spot(0, 17, Knight('g', 'kn'))
		self.board[0][18] = Spot(0, 18, Bishop('g', 'b'))
		self.board[0][19] = Spot(0, 19, King('g', 'k'))
		self.board[0][20] = Spot(0, 20, Queen('g', 'q'))
		self.board[0][21] = Spot(0, 21, Bishop('g', 'b'))
		self.board[0][22] = Spot(0, 22, Knight('g', 'kn'))
		self.board[0][23] = Spot(0, 23, Rook('g', 'r'))

		self.board[1][16] = Spot(1, 16, Pawn('g', 'p0'))
		self.board[1][17] = Spot(1, 17, Pawn('g', 'p1'))
		self.board[1][18] = Spot(1, 18, Pawn('g', 'p2'))
		self.board[1][19] = Spot(1, 19, Pawn('g', 'p3'))
		self.board[1][20] = Spot(1, 20, Pawn('g', 'p4'))
		self.board[1][21] = Spot(1, 21, Pawn('g', 'p5'))
		self.board[1][22] = Spot(1, 22, Pawn('g', 'p6'))
		self.board[1][23] = Spot(1, 23, Pawn('g', 'p7'))


		# set the remaining Spots to None
		for i in range(6):
			for j in range(24):
				if self.board[i][j] == 0:
					self.board[i][j] = Spot(i, j, None)


	def get_spot_of_piece(self, color: str, piece_tag: str) -> str:
		''' Get what Spot a Piece is currently at '''

		# if the color of the Piece being looked for is white, we start at position 0
		if color == 'w': 
			search_start = -1
		elif color == 'g': 
			search_start = 15
		else: 
			search_start = 7
		# search all Spots in ring 0, then ring 1, 2, 3, etc.
		for i in range(5):
			for j in range(search_start, search_start + 24):
				# continue our seach one position over
				j = (j + 1) % 24
				# if the color and piece_tag of the piece at that Spot are equivalent to our search criteria,
				# we have found our Piece
				if (self.get_space(i, j).Piece != None):
					if (self.get_space(i, j).Piece.color == color) and (self.get_space(i, j).Piece.piece_tag == piece_tag):
						return self.get_space(i, j)

	def diagonal_traverse(self, start_ring, start_pos, left_right: str, for_back: str):
		# list to store all pieces along diagonal in
		# element 0 is start spot, element 1 is the spot along the forward/backward right/left
			# diagonal (dependent on the arguments passed)
		spots = []
		if left_right == 'right':
			# a rignt diagonal move increases the position around the circle by one
			horiz_shift = 1
		else:
			# a left diagonal move decreases the position around the circle by one
			horiz_shift = -1
		if for_back == 'for':
			vert_shift = 1
			# check to see if ring is at this to see if we have crossed center
			check = 5
			x_to = 5
			crossed = False
		else: 
			vert_shift = -1
			check = 0
			x_to = 1
			crossed = False

		x = start_ring
		y = start_pos
		
			
		if (x == check):
			crossed = not(crossed)
			if for_back == "for":
				x = x_to
				if left_right == "right":
					y = (y - 10) % 24
				else: 
					y = (y + 10) % 24
			else: 
				return [self.get_space(x,y)]
		else:
			x += vert_shift
			y = (y + horiz_shift) % 24
	
		while (x != start_ring or y != start_pos):
			if for_back == 'back' and x == check:
				break
			#print(x, y)
			spots.append(self.get_space(x, y))
			y = (y + horiz_shift) % 24
			if crossed == False:
				#print("in crossed is false")
				x += vert_shift
			else:
				#print("in crossed is true")
				x += -1*vert_shift
			# at end of board
			if (x == -1):
				#print("x is -1")
				x = 1
				crossed = not(crossed)
			# crossing center
			if (x == 6):
				x = 5 
				# the two cases in which we shift 10 to the LEFT for a diag move through center
				if (left_right == "right" and for_back == "for") or (left_right == "right" and for_back == "back"):
					y = (y - 11) % 24
				else: 
					y = (y + 11) % 24
				crossed = not(crossed)
		spots.append(self.get_space(x,y))
		return spots

	
	def is_clear_path(self, start, end) -> bool:
		piece = start.Piece 
		# if the piece being moved is a Knight, we are not concerned about a path
		if (isinstance(piece, Knight)):
			return True

		# calculate how many positions over the piece has moved
		pos_change = (end.pos - start.pos) % 24
		adj_pos_change = pos_change
		if adj_pos_change > 12:
			adj_pos_change = 24 - adj_pos_change

		# calculate how many rings the piece has moved
		ring_change = end.ring - start.ring

		diag_move = False
		# CHECK IF MOVE IS DIAGONAL
		if (abs(ring_change) == adj_pos_change) and abs(ring_change) > 0:
			diag_move = True
		if start.ring > 0:
			if start.ring == adj_pos_change - end.ring:
				diag_move = True

		# we are looking at a HORIZONTAL MOVEMENT!!!!
			# a horizontal move could also be a diagonal move, so we have to check for that
		if (pos_change != 0) and (ring_change == 0) and (diag_move == False):
			# we have to check both ways for a horizontal movement
			horiz_right = True
			horiz_left = True
			# CHECK FOR CLEAR PATH GOING RIGHT

			# record starting location
			x = start.ring
			y = ((start.pos) + 1) % 24
			# traverse right until arriving at end Spot
			while (y != end.pos):
				# if we encounter a spot with a Piece on it, return False
				if (self.get_space(x,y).Piece != None):
					horiz_right = False
				y = (y + 1) % 24
			# CHECK FOR CLEAR PATH GOING LEFT

			# record starting location
			x = start.ring
			y = ((start.pos) - 1) % 24
			# traverse right until arriving at end Spot
			while (y != end.pos):
				if (self.get_space(x,y).Piece != None):
					horiz_left = False
				y = (y - 1) % 24
			# if neither the path is clear, return false
			if (horiz_right == False) and (horiz_left == False):
				return False

		# we are looking at a VERTICAL MOVEMENT!!!!!
		if (pos_change == 0 or pos_change == 12):
			# move is one unit through center (starts and ends on ring 5)
			if start.ring == 5 and ring_change == 0:
				return True
		
			x = start.ring
			y = start.pos
			# vertical movement FORWARD
			if (ring_change >= 0) or (pos_change == 12):
				crossed_center = False
				if (x == 5):
					x = 5
					y = (y - 12) % 24
					crossed_center = True
				if not(crossed_center):
					x += 1
				else:
					x -= 1
				
				while (x != end.ring or y != end.pos):
					if (self.get_space(x,y).Piece != None):
						return False
					if not(crossed_center):
						x += 1
					else:
						x -= 1
					if (x == 6):
						x = 5
						y = (y - 12) % 24
						crossed_center = True
			# vertical movement BACKWARDS
			else:
				x -= 1
				while (x != end.ring):
					if (self.get_space(x,y).Piece != None):
						return False
					x -= 1
					if (x == -1):
						break

		# if both of these are not 0, we are looking at a DIAGONAL MOVEMENT
		if (diag_move == True):
			# PIECE MOVES ALONG ITS FORWARD RIGHT/BACKWARDS LEFT DIAGONAL
			print('for right back left')
			forward_right = True
			backwards_left = True

			l = self.diagonal_traverse(start.ring, start.pos, 'right', 'for')
			for s in l:
				print(s.ring, s.pos)
				# if we get to our end Spot, break
				if s == end:
					break
				if (s.Piece != None):
					forward_right = False
			if forward_right: 
				return True

			l = self.diagonal_traverse(start.ring, start.pos, 'left', 'back')
			for s in l:
				print(s.ring, s.pos)
				# if we get to our end Spot, break
				if s == end:
					break
				if (s.Piece != None):
					backwards_left = False
			if backwards_left:
				return True



			# PIECE MOVES ALONG ITS FORWARD LEFT/BACKWARDS RIGHT DIAGONAL
			print('for left back right')
			forward_left = True
			backwards_right = True

			l = self.diagonal_traverse(start.ring, start.pos, 'left', 'for')
			for s in l:
				# if we get to our end Spot, break
				if s == end:
					break
				if (s.Piece != None):
					forward_left = False
			if forward_left:
				return True

			l = self.diagonal_traverse(start.ring, start.pos, 'right', 'back')
			for s in l:
				# if we get to our end Spot, break
				if s == end:
					break
				if (s.Piece != None):
					backwards_right = False
			if backwards_right:
				return True
			
			# if none of the diagonal moves were valid, return False
			return False

		# if the path is clear, return true...
		return True

	
	
	def bridge_moats_check(self):
		# temporarily set each moat to be bridged
		# if any Piece remains in color's back rank, we re-establish moat
		white_count = 0
		black_count = 0
		gray_count = 0
		# we only check white's outer rank if both the surrounding moats are not already bridged
		if self.moat_0_bridged == False or self.moat_1_bridged == False:
			for i in range(0, 8):
				if (self.board[0][i].Piece == None):
					white_count += 1
		# we only check black's outer rank if both the surrounding moats are not already bridged
		if self.moat_1_bridged == False or self.moat_2_bridged == False:
			for j in range(8, 16):
				if (self.board[0][j].Piece == None):
					black_count += 1
		# we only check gray's outer rank if both the surrounding moats are not already bridged
		if self.moat_2_bridged == False or self.moat_0_bridged == False:
			for k in range(16, 24):
				if (self.board[0][k].Piece == None):
					gray_count += 1

		# all Spots along white's outer rank are empty
		if white_count == 8:
			self.moat_0_bridged = True
			self.moat_1_bridged = True
		if black_count == 8:
			self.moat_1_bridged = True
			self.moat_2_bridged = True
		if gray_count == 8:
			self.moat_2_bridged = True
			self.moat_0_bridged = True


class Spot:
	def __init__(self, ring, pos, Piece):
		self.ring = ring
		self.pos = pos
		self.Piece = Piece

	def is_check(self, board: Board, color: str) -> bool:

		# below we begin the logic of whether or not a King is in check


		# a dictionary to store all Spot objects that are within a direct path of the king
			# we store the Spot object because it has the coordinates of the piece and the type of piece itself
		threats = []

		# get first piece to the horizontal right

		# record starting location
		x = self.ring
		y = ((self.pos) + 1) % 24
		# we will store all spots we encounter on traversal
		# this will be used to see if one of these Spots can be blocked (i.e. block a checkmate)
		spots = []
		# tracker
		horiz_right_count = 1

		# traverse right until arriving at a Spot occupied by a Piece
		while (board.get_space(x, y).Piece == None):
			# in some cases, the King may be the only Piece on a given ring
			# we need to break upon returning to end Spot to avoid an infinite loop 
			if y == self.pos:
				break
			spots.append(board.get_space(x, y))
			horiz_right_count += 1
			y = (y + 1) % 24

			
		spots.append(board.get_space(x,y))
		threats.append([board.get_space(x,y), "horizontal", horiz_right_count, spots])



		# get first piece to the horizontal left

		x = self.ring
		y = (self.pos - 1) % 24
		spots = []
		# tracker
		horiz_left_count = 1

		# traverse left until arriving at a spot occupied by a Piece
		while (board.get_space(x, y).Piece == None):
			if y == self.pos:
				break
			spots.append(board.get_space(x, y))
			horiz_left_count += 1
			y = (y - 1) % 24
		spots.append(board.get_space(x,y))
		threats.append([board.get_space(x,y), "horizontal", horiz_left_count, spots])

		# get first piece vertically in front


		x = self.ring
		y = self.pos
		spots = []
		# tracker
		vert_front_count = 1
		# boolean value to store whether or not our scanning algorithm has crossed the center
		crossed_center = False
		if (x == 6):
			x = 5
			y = (y - 12) % 24
			crossed_center = True
		if crossed_center == False:
			x += 1
		else:
			x -= 1

		# traverse forward until arriving at a spot occupied by a Piece
		while (board.get_space(x, y).Piece == None):
			spots.append(board.get_space(x, y))
			vert_front_count += 1
			if crossed_center == False:
				x += 1
			else:
				x -= 1
			# if we get to x = 6, wrap back to 5; add/subtract 12 from position
			# this simulates motion through the center
			if (x == 6):
				x = 5
				y = (y - 12) % 24
				crossed_center = True
			if (x == -1):
				break
		spots.append(board.get_space(x,y))
		threats.append([board.get_space(x,y), "forward-vertical", vert_front_count, spots])

		# get first piece vertically behind


		x = self.ring
		y = self.pos
		spots = []
		# tracker
		vert_back_count = 1
		x -= 1

		# traverse backwards until arriving at a spot occupied by a Piece
		while (board.get_space(x, y).Piece == None):
			spots.append(board.get_space(x, y))
			vert_back_count += 1
			x -= 1
			if (x == -1):
				break
		# sometimes, we get x = -1, this gives us reverse indexing in get_space() method, which we do not want
		if x >= 0:
			spots.append(board.get_space(x,y))
			threats.append([board.get_space(x,y), "behind-vertical", vert_back_count, spots])

		# get first piece to the forward, right diagonal

		x = self.ring
		y = self.pos
		crossed_center = False

		# track how many spaces we traverse for our forward right diagonal scan
		# will be used if scan algorithm catches a Pawn because Pawns are only a threat
		# if they are to the immediate forward diagonal of the King
		forward_r_diag_count = 0
		f_r_spot = self
		l = board.diagonal_traverse(self.ring, self.pos, 'right', 'for')
		spots = []
		for s in l:
			spots.append(s)
			forward_r_diag_count += 1
			if s.Piece != None:
				f_r_spot = s
				break

		threats.append([f_r_spot, "f-r-diagonal", forward_r_diag_count, spots])	

		# get first piece to the forward, left diagonal

		x = self.ring
		y = self.pos
		crossed_center = False
		spots = []

		# same reasoning for tracker as above; this one for left forward diagonal
		forward_l_diag_count = 0
		f_l_spot = self
		l = board.diagonal_traverse(self.ring, self.pos, 'left', 'for')
		for s in l:
			spots.append(s)
			forward_l_diag_count += 1
			if s.Piece != None:
				f_l_spot = s
				break

		threats.append([f_l_spot, "f-l-diagonal", forward_l_diag_count, spots])


		# get first piece to the backwards, right diagonal


		x = self.ring
		y = self.pos
		spots = []
		# tracker
		back_right_count = 0
		b_r_spot = self
		l = board.diagonal_traverse(self.ring, self.pos, 'right', 'back')
		for s in l:
			spots.append(s)
			back_right_count += 1
			if s.Piece != None:
				b_r_spot = s
				break

		threats.append([b_r_spot, "b-r-diagonal", back_right_count, spots])

		# get first piece to the backwards, left diagonal
		x = self.ring
		y = self.pos
		spots = []
		# tracker
		back_left_count = 0
		b_l_spot = self
		l = board.diagonal_traverse(self.ring, self.pos, 'left', 'back')
		for s in l:
			spots.append(s)
			back_left_count += 1
			if s.Piece != None:
				b_l_spot = s
				break

		threats.append([b_l_spot, "b-l-diagonal", back_left_count, spots])

		# there is one last Piece that we have to consider for having the King in checkmate
		# this is the only Piece that cannot be identified by a directional linear scan from the King: a Knight

		# check all Spots from which a Knight could reach the King in one move

		# a list to store all the Kinght potential Spots BEHIND the King
		knights = []

		x = self.ring
		y = self.pos


		# append all horse-shaped moves which end in a final Spot behind King's Spot

		if (self.ring != 0 and self.ring != 1):
			# back 2, left 1
			knights.append(board.get_space(x - 2, (y - 1) % 24))
			
			# back 2, right 1
			knights.append(board.get_space(x - 2, (y + 1) % 24))

		# for all rings other than 0, knights can move back 1
		if (self.ring != 0):
			# left 2, back 1
			knights.append(board.get_space(x - 1, (y - 2) % 24))
			# right 2, back 1
			knights.append(board.get_space(x - 1, (y + 2) % 24))

		if (self.ring <= 4):
			# left 2, forward 1
			knights.append(board.get_space(x + 1, (y - 2) % 24))
			# right 2, forward 1
			knights.append(board.get_space(x + 1, (y + 2) % 24))
			if (self.ring != 4):
				# forward 2, right 1
				knights.append(board.get_space(x + 2, (y + 1) % 24))
				# forward 2, left 1
				knights.append(board.get_space(x + 2, (y - 1) % 24))
			else: 
				# on ring 4, some poential horse Spots will be through the circle

				# forward 2, right 1 
				# equivalent to landing in ring 5, shifting 11 units left
				knights.append(board.get_space(5, (y + 11) % 24))
				knights.append(board.get_space(5, (y - 11) % 24))

		# in ring 5
		else:
			# forward 2, right 1
			knights.append(board.get_space(4, (y + 11) % 24))
			# forward 2, left 1
			knights.append(board.get_space(4, (y - 11) % 24))
			# forward 1, left 2
			knights.append(board.get_space(5, (y + 10) % 24))
			# forward 1, right 2
			knights.append(board.get_space(5, (y - 10) % 24))



		'''
		* After finding all 8 Spots with the closest Piece in a direct path with the king from all 8 directions,
		* we identifiy all of those Pieces in those spots
			* If a Spot is occupied by a Piece of the same color, that Piece is not a threat
			* Otherwise, we compare the Piece's movement capabilities with their position in the threats list:
				* Elements 1 and 2, for example, represent Spots acquired by horizontal scanning from the King: 
				  if the respective Piece has horizontal moving capability, that Piece would have the King in check
				* Elements 3 and 4 represent vertical scanning; respective Pieces cannot have vertical capability
				* Elements 5-8 are diagonal scanning; Pieces cannot have diagonal capability
					* Note: Pawns are only checked for at elements 5 and 6 because those represent a forward
					        diagonal movement from the King's perspective. A Pawn behind a King is not a threat

		'''

		'''
		# we only need to check the Pieces that are not on the King's team
		'''

		#print(threats)
		real_threats = []
		for t in threats:
			if (t[0].Piece != None):
				print("Threatened by: " + t[1])
				print(t[0].Piece.color)
				print(t[0].Piece.piece_tag)
				print()
				if (t[0].Piece.color != color):
					if isinstance(t[0].Piece, King):
						# if the threatening Piece is a King 1 unit away, we cannot move our king there (regardless of direction)
						if (t[2] == 1):
							real_threats.append(t)
					elif isinstance(t[0].Piece, Pawn):
						# Pawns along the King's forward diagonal cuase Check iff they are to the immediate diagonal
						# below conditional variables tracked how far many units our traversal moved
						if (t[1][-8:] == "diagonal") and (t[2] == 1):
							print(t[1] + " is killing you")
							real_threats.append(t)
					else:
						if (t[0].Piece.horizontal == True and t[1] == "horizontal"):
							print(t[1] + " is killing you")
							real_threats.append(t)
						if (t[0].Piece.vertical == True and t[1][-8:] == "vertical"):
							print(t[1] + " is killing you")
							real_threats.append(t)
						if (t[0].Piece.diagonal == True and t[1][-8:] == "diagonal"):
							print(t[1] + " is killing you")
							real_threats.append(t)

		# checking if we found any potential Knight Spots that contain a Knight of differing color
		# if so, the Spot the King is trying to move to results in check
		for k in knights:
			# if the detected Piece is a Knight
			if (isinstance(k.Piece, Knight)):
				if (k.Piece.color != color):
					print("Oh no, a knight is getting you in check!")
					real_threats.append(k, "knight", 0, [])
		# if we found any real threats
		if len(real_threats) > 0:
			return real_threats
		# if True is never returned, return False (i.e. King is NOT moving into check)
		return False


from abc import ABC, abstractmethod
class Piece(ABC):
	"""
	Abstract class to represent a chess piece. All other types of pieces will inherit from Piece class

	***

	Attributes
	----------
	* color: 
			# the color of the chess piece, 'w' for white, 'b' for black, 'g' for gray
	* killed:
			# whether or not the piece is killed
	* piece_tag:
			# what piece the Piece is: king, queen, etc.

	Methods
	-------
	* color()
			# returns color of chess piece
			# sets color to new color
	* set_killed()
			# sets piece's kill status variable to killed
	* get_kill_status()
			# returns whether or not a piece has been killed
	* valid_move()
			# determines whether a move is valid
	"""
	
	def __init__(self, color, piece_tag):
		''' 
		Parameters
		----------
		* color: str ('w', 'b', 'g')
				# the color of the chess piece
		* piece_tag: str 
				# what kind of piece the piece is
		'''

		# a piece defaults to killed being false
		self.killed = False

		self.__color = color
		self.piece_tag = piece_tag



	@property
	def color(self):
		''' Return color of chess piece'''
		return self.__color

	def set_killed(self):
		''' Sets killed variable for that piece to True, meaning it has been killed'''
		self.killed = True

	def get_kill_status(self):
		''' Returns whether or not a piece has been kiilled'''
		return self.killed

	#@abstractmethod
	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:
		''' Abstract method; determines whether or not a move is valid'''
		pass

	def possible_moves(self, board: Board):
		''' Abstract method; generates a list of all valid Spots for a player. 
			will be used in determining checkmate'''
		# get the current Spot the piece is at
		curr_spot = board.get_spot_of_piece(self.color, self.piece_tag)
		# list to store all the Spots the Piece can currently move to
		possible_moves = []
		# iterating over our board
		# our board always has 5 sublists for rings
		for i in range(6):
			# each containing 23 elements for positions
			for j in range(24):
				# if the move from the Piece's current Spot to the Spot on the board is valid
				# add it as a possible move
				if (self.valid_move(board, curr_spot, board.board[i][j]) and board.is_clear_path(curr_spot, board.board[i][j])):
					possible_moves.append(board.board[i][j])
		return possible_moves


class King(Piece):
	horizontal = True
	vertical = True
	diagonal = True

	def __init__(self, color, piece_tag):
		# we set variable castled to false
		self.castled = False
		super().__init__(color, piece_tag)


	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:

		# we cannot move to a Spot occupied by a piece of the same color
		if (end.Piece != None):
			if (end.Piece.color == self.color):
				return False

		# calculate how many positions over the piece has moved
		pos_change = (end.pos - start.pos) % 24
		if pos_change > 12:
			pos_change = 24 - pos_change

		# calculate how many rings the piece has moved
		ring_change = abs(start.ring - end.ring)

		# if the king is at ring 4 or lower or is at ring five and moving BACKWARDS
		if (start.ring <= 4) or (end.ring < start.ring):
			# king moves 1 position unit and 0 or 1 ring unit
			if (pos_change == 1) and (ring_change <= 1):
				return True

			# king moves 0 position units and 1 ring unit
			if (pos_change == 0) and (ring_change == 1):
				return True
		# if the king is at ring 5 and moves through the center
		if (start.ring == 5):
			# movement through the center corresponds to a positional shift of 12 units and ring change of 0
			if (pos_change == 12) and (ring_change == 0):
				return True
class Pawn(Piece):
	horizontal = False
	vertical = False
	diagonal = True
	def __init__(self, color, piece_tag):
		super().__init__(color, piece_tag)

	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:

		# we cannot move to a Spot occupied by a piece of the same color
		if (end.Piece != None):
			if (end.Piece.color == self.color):
				return False

		pos_change = (end.pos - start.pos) % 24
		if pos_change > 12:
			pos_change = 24 - pos_change

		ring_change = abs(start.ring - end.ring)

		# Pawns can move diagonally as long as they are killing a piece of a different color
		if (ring_change == 1) and (pos_change == 1) and (end.Piece != None):
			return True

		# in general, Pawns can move one space up (no piece can be there)
		if (ring_change == 1) and (pos_change == 0) and (end.Piece == None): 
			return True
		# if they haven't moved yet, they can move two spaces up (no piece can be there)
		if (start.ring == 1 and ring_change == 2) and (pos_change == 0) and (end.Piece == None):
			return True
		# a Pawn can move through the center when it is ring 5
		if (start.ring == 5) and (pos_change == 12) and (end.Piece == None):
			if (self.color == 'w') and (start.pos >= 0 and start.pos <= 7):
				return True
			if (self.color == 'b') and (start.pos >= 8 and start.pos <= 15):
				return True
			if (self.color == 'g') and (start.pos >= 16):
				return True

class Knight(Piece):
	horizontal = False
	vertical = False
	diagonal = False

	def __init__(self, color, piece_tag):
		super().__init__(color, piece_tag)


	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:

		# we cannot move to a Spot occupied by a piece of the same color
		if (end.Piece != None):
			if (end.Piece.color == self.color):
				return False

		## CONSIDER ADDING ABOVE TWO AND BELOW TWO LINES OF CODE TO PIECE CLASS
		# calculate how many positions over the piece has moved
		pos_change = (end.pos - start.pos) % 24
		# calculate how many rings the piece has moved
		ring_change = abs(start.ring - end.ring)
		if pos_change > 12:
			pos_change = 24 - pos_change

		# if the knight is on ring three or lower, there are two cases to look at
		# OR if the knight is on ring four or five and moves backwards, the same two cases apply
		if (start.ring <= 3) or (end.ring < start.ring):
			if (ring_change == 1 and pos_change == 2):
				return True

			if (ring_change == 2 and pos_change == 1):
				return True

		# if the knight is on the fifth ring, it can move through the center
		if (start.ring == 5):

			# the knight moves two forward (to ring four) and one left or right (11 from start piece)
			if (end.ring == 4 and pos_change == 11):
				return True

			# the kinght moves one forward (still in ring 5) and two left or right (10 from start piece) 
			if (ring_change == 0 and pos_change == 10):
			 	return True
		
		# if the knight is on the fourth ring, we also have to account for it moving through center
		if (start.ring == 4):
			# the knight moves two forward (to ring 5) and one left or right (11 from start)
			if (end.ring == 5 and pos_change == 11):
				return True
			# the knight moves one forward and two left or right
			if (end.ring == 5 and pos_change == 2):
				return True


class Rook(Piece):
	horizontal = True
	vertical = True
	diagonal = False

	def __init__(self, color, piece_tag):
		super().__init__(color, piece_tag)


	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:
		pos_change = (end.pos - start.pos) % 24
		if pos_change > 12:
			pos_change = 24 - pos_change

		# we cannot move to a Spot occupied by a piece of the same color
		if (end.Piece != None):
			if (end.Piece.color == self.color):
				return False
		# not through center
		if (start.ring == end.ring) or (start.pos == end.pos):
			return True

		# through center
		if (pos_change == 12):
			return True

		return False

class Queen(Piece):
	horizontal = True
	vertical = True
	diagonal = True

	def __init__(self, color, piece_tag):
		super().__init__(color, piece_tag)


	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:

		# we cannot move to a Spot occupied by a piece of the same color
		if (end.Piece != None):
			if (end.Piece.color == self.color):
				return False

		## CONSIDER ADDING ABOVE TWO AND BELOW TWO LINES OF CODE TO PIECE CLASS
		# calculate how many positions over the piece has moved
		pos_change = (end.pos - start.pos) % 24
		if pos_change > 12:
			pos_change = 24 - pos_change
		# calculate how many rings the piece has moved
		ring_change = abs(start.ring - end.ring)

		'''there are two cases to look at for a piece that can move diagonally

                1. if the piece does not cross the center
                2. if the piece crosses the center
                '''

		
                ##1. if the piece does not cross the center
                #if the ring change equals the position change, the piece will move diagonally
		#(but ring change must be greater than 0 because the piece must move)
		if (ring_change == pos_change) and ring_change > 0:
			return True

		if start.ring > 0:

			if start.ring == pos_change - end.ring:
				return True


		# BEGINNING HORIZONTAL MOVES!
		# we cannot move to a Spot occupied by a piece of the same color
		
		# not through center
		if (start.ring == end.ring) or (start.pos == end.pos):
			return True

		# through center
		if (pos_change == 12):
			return True

		return False


class Bishop(Piece):
	horizontal = False
	vertical = False
	diagonal = True

	def __init__(self, color, piece_tag):
		super().__init__(color, piece_tag)


	def valid_move(self, board: Board, start: Spot, end: Spot) -> bool:

		# we cannot move to a Spot occupied by a piece of the same color
		if (end.Piece != None):
			if (end.Piece.color == self.color):
				return False

		## CONSIDER ADDING ABOVE TWO AND BELOW TWO LINES OF CODE TO PIECE CLASS
		# calculate how many positions over the piece has moved
		pos_change = (end.pos - start.pos) % 24
		if pos_change > 12:
			pos_change = 24 - pos_change
		# calculate how many rings the piece has moved
		ring_change = abs(start.ring - end.ring)

		'''there are two cases to look at for a piece that can move diagonally

                1. if the piece does not cross the center
                2. if the piece crosses the center
                '''

		
                ##1. if the piece does not cross the center
                #if the ring change equals the position change, the piece will move diagonally
		#(but ring change must be greater than 0 because the piece must move)
		if (ring_change == pos_change) and (ring_change != 0 or pos_change != 0):
			return True

           	##2. if the piece crosses the center
              
		if start.ring > 0:
			if start.ring == pos_change - end.ring:
				return True
		return False



if __name__ == "__main__":

	test = Board()
	try:
		print(test.get_space(0, 1).Piece.piece_tag)
		for i in range(6):
			for j in range(24):
				print(str(i) + str(j) + (test.board[i][j].Piece.piece_tag))
	except: 
		pass

