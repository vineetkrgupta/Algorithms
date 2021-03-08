def search_for_words_in_board(board, words):
    """Given a board of letters, find all the words vertically, horizontally and diagonally"""
	
	if not board:
		return []
	
	# build the hash table of letter and locations
	hash_table = build_hash_table(board)
	
    return list(
        filter(
            lambda word: contains_word(board, hash_table, word),
            words
        )
    )

def contains_word(board, hash_table, word):
    
    starting_letter = word[0]
    if starting_letter not in hash_table:
        return False
        
    if len(word) < 2:
        return True
    
    starting_indexes = hash_table[starting_letter]
    for start_i in starting_indexes:
        if contains_word(board, word, start_i):
            return True
            

def contains_word_at_index(board, word, start_i):
	directions = get_directions(board, word, start_i)
	
	# see if the whole word matches for the whole direction
	for direction in directions:
		
		row, col, _ = get_next_cell(start_i[0], start_i[1], direction)
		word_i = 1
		word_length = 1
		
		while not is_out_of_bounds(board, row, col) and word_i < len(word):
			
			if board[row][col] != word[word_i]:
				break
			
			# see if the word matched
			# set cursor to next letter in the direction
			row, col, _ = get_next_cell(row, col, direction)
			word_length += 1
			word_i += 1
			
		if word_length == len(word):
			return True
				
def get_directions(board, word, start_i):
	"""Get directions of all first matched letters"""
	directions = []
	word_i = 0
	letter_to_match = word[1]
	start_row, start_col = start_i
	
	for row, col, direction in [
			get_next_cell(start_row, start_col, "top"),
			get_next_cell(start_row, start_col, "top-right"),
			get_next_cell(start_row, start_col, "right"),
			get_next_cell(start_row, start_col, "right-bottom"),
			get_next_cell(start_row, start_col, "bottom"),
			get_next_cell(start_row, start_col, "left-bottom"),
			get_next_cell(start_row, start_col, "left"),
			get_next_cell(start_row, start_col, "left-top")
		]:
		if is_out_of_bounds(board, row, col):
			continue
		
		if board[row][col] == letter_to_match and direction is not None:
			directions.append(direction)
				
	return directions

def is_out_of_bounds(board, row, col):
	"""checks if the indexes are within the boundary of the board"""
	return not (0 <= row < len(board) and 0 <= col < len(board[0]))
		
def get_next_cell(row, col, direction):
	"""based on direction get the next cell location"""
	
	if direction == "top":
		return row - 1, col, direction
	elif direction == "top-right":
		return row - 1, col + 1, direction
	elif direction == "right":
		return row, col + 1, direction
	elif direction == "right-bottom":
		return row + 1, col + 1, direction
	elif direction == "bottom":
		return row + 1, col, direction
	elif direction == "left-bottom":
		return row + 1, col - 1, direction
	elif direction == "left":
		return row, col - 1, direction
	elif direction == "left-top":
		return row - 1, col - 1, direction
	else:
		raise Exception("Invalid direction")

def build_hash_table(board):
	"""builds a hash table of locations of all the starting letters"""
	
	hash_table = {}
	for row in range(len(board)):
		for col in range(len(board[0])):
			
			letter = board[row][col]
			if letter in hash_table:
				hash_table[letter].append((row, col))
			else:
				hash_table[letter] = [(row, col)]
				
	return hash_table
			
