game_board = [[" 1 |"," 2 |"," 3 "],[" 4 |"," 5 |"," 6 "],[" 7 |"," 8 |"," 9 "]] 

player_input = None
player_input_pos = None

wins_for_x = 0
wins_for_o = 0

count = 1

def board():
	global game_board

	for row in game_board:
		for e in row:
			print(e,end="")
		print()		

def header():
	print("Welcome to the tic-tac-toe game!")
	print(f"Wins for X = {wins_for_x} and Wins for O = {wins_for_o}")

def play():
	global player_input
	global player_input_pos
	global count

	global wins_for_x
	global wins_for_o

	while True:
		board()
		header()
			
		if count % 2 != 0:
			print("X's turn")
			player_input = "X"
			

		elif count % 2 == 0:
			print("O's turn")
			player_input ="O"
			
		
	
		
		if player_input=="X" or player_input=="O":	
			player_input_pos = input(f"Enter position for {player_input} or quit: ")	
			if player_input_pos == "quit":
				if wins_for_x > wins_for_o:
					print("X Won this round!")
				elif wins_for_x < wins_for_o:
					print("O Won this round!")
				elif wins_for_o == wins_for_x:
					print("There is no winner!")	
				break
			else:
				try:

					player_input_pos = int(player_input_pos)
					mark_input()	

				except ValueError:
					print("You can only enter a position from 1-9")
		


					

def mark_input():
	global count
	global player_input
	global player_input_pos
	# print(f"count is {count}" )

	#game_board = [   [" 1 |"," 2 |"," 3 "],
					# [" 4 |"," 5 |"," 6 "],
					# [" 7 |"," 8 |"," 9 "]] 

	if player_input_pos in range(1,4):
		if game_board[0][player_input_pos-1] == " " +"X" + "  " or game_board[0][player_input_pos-1] == " " +"O" + "  ":
			print("That position has already been marked!")
		else:		
			game_board[0][player_input_pos-1] = " " +player_input + "  "
			count += 1
	elif player_input_pos in range(4,7):
		if game_board[1][player_input_pos-4] == " " +"X" + "  " or game_board[1][player_input_pos-4] == " " +"O" + "  ":
			print("That position has already been marked!")
		else:
			game_board[1][player_input_pos-4] = " " +player_input + "  "
			count += 1 
	else:
		if game_board[2][player_input_pos-7] == " " +"X" + "  " or game_board[2][player_input_pos-7] == " " +"O" + "  ":
			print("That position has already been marked!")
		else:
			game_board[2][player_input_pos-7] = " " +player_input  + "  "
			count += 1

	check_if_won_or_tie()		


def check_if_won_or_tie():
	global wins_for_x
	global wins_for_o

	global game_board
	reset = [[" 1 |"," 2 |"," 3 "],[" 4 |"," 5 |"," 6 "],[" 7 |"," 8 |"," 9 "]] 
	global count
	won_count = 0
	for row in range(len(game_board)):
		for el in range(0,3):
			if " " +player_input + "  " in game_board[row][el]:
				won_count+=1
				if (won_count == 3):
					if count %2 == 0:
						print("X WON!")
						wins_for_x += 1
						game_board = reset 
					elif count %2 != 0:
						print("O WON")
						wins_for_o += 1
						game_board = reset


		won_count =0

	won_count_diag = 0
	for row in range(len(game_board)):
		for el in range(0,3):
			if el == row:
				if " " +player_input + "  " in game_board[row][el]:
					won_count_diag+=1
				if (won_count_diag == 3):
					if count %2 == 0:
						print("X WON!")
						wins_for_x += 1
						game_board = reset
					elif count %2 != 0:
						print("O WON")
						wins_for_o += 1	
						game_board = reset

	for row in game_board:
		row.reverse()						
		
	won_count_diag_reverse = 0
	for row in range(len(game_board)):
		for el in range(0,3):
			if el == row:
				if " " +player_input + "  " in game_board[row][el]:
					won_count_diag_reverse+=1
				if (won_count_diag_reverse == 3):
					if count %2 == 0:
						print("X WON!")
						wins_for_x += 1
						game_board = reset
						return
					elif count %2 != 0:
						print("O WON")
						wins_for_o += 1
						game_board = reset
						return

	for row in game_board:
		row.reverse()						
	
	down_count_1 = 0
	down_count_2 = 0
	down_count_3 = 0

	for i in range(0,9):
		if i in [0,1,2]:
			if game_board[i][0] == " " +player_input + "  " :
				down_count_1 += 1
				if down_count_1 == 3:
					if count %2 == 0:
						print("X WON!")
						wins_for_x += 1
						game_board = reset
					elif count %2 != 0:
						print("O WON")
						wins_for_o += 1
						game_board = reset
		if i in [3,4,5]:										
			if game_board[i-3][1] == " " +player_input + "  " :
				down_count_2 += 1
				if down_count_2 == 3:
					if count %2 == 0:
						print("X WON!")
						wins_for_x += 1
						game_board = reset
					elif count %2 != 0:
						print("O WON")
						wins_for_o += 1
						game_board = reset
		if i in [6,7,8]:
			if game_board[i-6][2] == " " +player_input + "  " :
				down_count_3 += 1
				if down_count_3 == 3:
					if count %2 == 0:
						print("X WON!")
						wins_for_x += 1
						game_board = reset
					elif count %2 != 0:
						print("O WON")
						wins_for_o += 1
						game_board = reset

	tie_count = 0
	for row in range(len(game_board)):
		for el in range(0,3):
			if " " +"X" + "  " in game_board[row][el] or  " " +"O" + "  " in game_board[row][el]:		
				tie_count += 1
			if tie_count == 9:
				print("Game Tied!")
				game_board =reset	
	# if game_board[0][0] == " " +player_input + "  "  and game_board[1][0] == " " +player_input + "  " and game_board[2][0] == " " +player_input + "  "					
		




play()





