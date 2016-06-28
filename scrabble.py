from random import shuffle

"""
Scrabble Game
Classes:
Tile - keeps track of the tile letter and value
Rack - keeps track of the tiles in a player's letter rack
Bag - keeps track of the remaining tiles in the bag
Word - checks the validity of a word and its placement
Board - keeps track of the tiles' location on the board
"""
LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}

class Tile:
    """
    Class that allows for the creation of a tile. Initializes using an uppercase string of one letter,
    and an integer representing that letter's score.
    """
    def __init__(self, letter, letter_values):
        self.letter = letter.upper()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        return self.letter

    def get_score(self):
        #Returns the tile's score value.
        return self.score

class Bag:
    """
    Creates the bag of all tiles that will be available during the game. Contains 98 letters and two blank tiles.
    Takes no arguments to initialize.
    """
    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def __str__(self):
        for line in self.bag:
            "\n"

    def add_to_bag(self, tile, quantity):
        #Adds a certain quantity of a certain tile to the bag. Takes a tile and an integer quantity as arguments.
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):
        #Adds the intiial 100 tiles to the bag.
        global LETTER_VALUES
        self.add_to_bag(Tile("A", LETTER_VALUES), 9)
        self.add_to_bag(Tile("B", LETTER_VALUES), 2)
        self.add_to_bag(Tile("C", LETTER_VALUES), 2)
        self.add_to_bag(Tile("D", LETTER_VALUES), 4)
        self.add_to_bag(Tile("E", LETTER_VALUES), 12)
        self.add_to_bag(Tile("F", LETTER_VALUES), 2)
        self.add_to_bag(Tile("G", LETTER_VALUES), 3)
        self.add_to_bag(Tile("H", LETTER_VALUES), 2)
        self.add_to_bag(Tile("I", LETTER_VALUES), 9)
        self.add_to_bag(Tile("J", LETTER_VALUES), 9)
        self.add_to_bag(Tile("K", LETTER_VALUES), 1)
        self.add_to_bag(Tile("L", LETTER_VALUES), 4)
        self.add_to_bag(Tile("M", LETTER_VALUES), 2)
        self.add_to_bag(Tile("N", LETTER_VALUES), 6)
        self.add_to_bag(Tile("O", LETTER_VALUES), 8)
        self.add_to_bag(Tile("P", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Q", LETTER_VALUES), 1)
        self.add_to_bag(Tile("R", LETTER_VALUES), 6)
        self.add_to_bag(Tile("S", LETTER_VALUES), 4)
        self.add_to_bag(Tile("T", LETTER_VALUES), 6)
        self.add_to_bag(Tile("U", LETTER_VALUES), 4)
        self.add_to_bag(Tile("V", LETTER_VALUES), 2)
        self.add_to_bag(Tile("W", LETTER_VALUES), 2)
        self.add_to_bag(Tile("X", LETTER_VALUES), 1)
        self.add_to_bag(Tile("Y", LETTER_VALUES), 2)
        self.add_to_bag(Tile("Z", LETTER_VALUES), 1)
        self.add_to_bag(Tile("#", LETTER_VALUES), 2)
        shuffle(self.bag)

    def take_from_bag(self):
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.bag.pop()

    def get_remaining_tiles(self):
        #Returns the number of tiles left in the bag.
        return len(self.bag)

class Rack:
    """
    Creates each player's 'dock', or 'hand'. Allows players to add, remove and replenish the number of tiles in their hand.
    """
    def __init__(self, bag):
        self.rack = []
        self.bag = bag
        self.initialize()

    def add_to_rack(self):
        #Takes a tile from the bag and adds it to the player's rack.
        self.rack.append(self.bag.take_from_bag())

    def initialize(self):
        #Adds the initial 7 tiles to the player's hand.
        for i in range(7):
            self.add_to_rack()

    def get_rack_str(self):
        #Displays the user's rack in string form.
        return ", ".join(str(item.get_letter()) for item in self.rack)

    def get_rack_arr(self):
        #Returns the rack as an array of tile instances
        return self.rack

    def remove_from_rack(self, tile):
        #Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

    def get_rack_length(self):
        #Returns the number of tiles left in the rack.
        return len(self.rack)

    def replenish_rack(self):
        #Adds tiles to the rack after a turn such that the rack will have 7 tiles (assuming a proper number of tiles in the bag).
        while self.get_rack_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_rack()

class Player:
    """
    Creates an instance of a player. Initializes the player's rack, and allows you to set/get a player name.
    """
    def __init__(self, bag):
        self.name = ""
        self.rack = Rack(bag)
        self.score = 0

    def set_name(self, name):
        #Sets the player's name.
        self.name = name

    def get_name(self):
        #Gets the player's name.
        return self.name

    def get_rack_str(self):
        #Returns the player's rack.
        return self.rack.get_rack_str()

    def get_rack_arr(self):
        return self.rack.get_rack_arr()

    def increase_score(self, increase):
        self.score += increase

    def get_score(self):
        return self.score

class Board:
    """
    Creates the scrabble board.
    """
    def __init__(self):
        self.board = [["   " for i in range(15)] for j in range(15)]
        self.add_premium_squares()
        self.board[7][7] = " * "

    def get_board(self):
        #Returns the board in string form.
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def add_premium_squares(self):
        #Adds all of the premium squares that influence the word's score.
        TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DLS"

    def place_word(self, word, location, direction, player):
        #Allows you to play words, assuming that they have already been confirmed as valid.
        global premium_spots
        premium_spots = []
        direction.lower()
        word = word.upper()
        if direction == "right":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]][location[1]+i] = " " + word[i] + " "
        elif direction == "down":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]+i][location[1]] = " " + word[i] + " "

        #Removes tiles from player's rack and replaces them with tiles from the bag.
        for letter in word:
            for tile in player.get_rack_arr():
                if tile.get_letter() == letter:
                    player.rack.remove_from_rack(tile)
        player.rack.replenish_rack()

    def board_array(self):
        return self.board

def check_word(word, location, player, direction, board):
    #Checks the word to make sure that it is in the dictionary, and that the location falls within bounds.
    #Also controls the overlapping of words.
    global round_number, players
    word_score = 0
    word = word.upper()
    dictionary = open("dic.txt").read()

    current_board_ltr = ""
    needed_tiles = ""
    blank_tile_val = ""
    if word != "":
        if "#" in word:
            while len(blank_tile_val) != 1:
                blank_tile_val = raw_input("Please enter the letter value of the blank tile: ")
            word = word[:word.index("#")] + blank_tile_val.upper() + word[(word.index("#")+1):]

        if direction.lower() == "right":
            for i in range(len(word)):
                if board[location[0]][location[1]+i][1] == " " or board[location[0]][location[1]+i] == "TLS" or board[location[0]][location[1]+i] == "TWS" or board[location[0]][location[1]+i] == "DLS" or board[location[0]][location[1]+i] == "DWS" or board[location[0]][location[1]+i][1] == "*":
                    current_board_ltr += " "
                else:
                    current_board_ltr += board[location[0]][location[1]+i][1]
        elif direction.lower() == "down":
            for i in range(len(word)):
                if board[location[0]+i][location[1]] == "   " or board[location[0]+i][location[1]] == "TLS" or board[location[0]+i][location[1]] == "TWS" or board[location[0]+i][location[1]] == "DLS" or board[location[0]+i][location[1]] == "DWS" or board[location[0]+i][location[1]] == " * ":
                    current_board_ltr += " "
                else:
                    current_board_ltr += board[location[0]+i][location[1]][1]
        else:
            return "Error: please enter a valid direction."

        if word not in dictionary:
            return "Please enter a valid dictionary word.\n"

        for i in range(len(word)):
            if current_board_ltr[i] == " ":
                needed_tiles += word[i]
            elif current_board_ltr[i] != word[i]:
                print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + word + ", Needed_Tiles: " + needed_tiles)
                return "The letters do not overlap correctly, please choose another word."

        if blank_tile_val != "":
            needed_tiles = needed_tiles[needed_tiles.index(blank_tile_val):] + needed_tiles[:needed_tiles.index(blank_tile_val)]

        if (round_number != 1 or (round_number == 1 and players[0] != player)) and current_board_ltr == " " * len(word):
            print("Current_board_ltr: " + str(current_board_ltr) + ", Word: " + word + ", Needed_Tiles: " + needed_tiles)
            return "Please connect the word to a previously played letter."
        for letter in needed_tiles:
            if letter not in player.get_rack_str() or player.get_rack_str().count(letter) < needed_tiles.count(letter):
                return "You do not have the tiles for this word\n"


        if location[0] > 14 or location[1] > 14 or location[0] < 0 or location[1] < 0 or (direction.lower() == "down" and (location[0]+len(word)-1) > 14) or (direction.lower() == "right" and (location[1]+len(word)-1) > 14):
            return "Location out of bounds.\n"
        if round_number == 1 and players[0] == player and location != [7,7]:
            return "The first turn must begin at location (7, 7).\n"
        return True
    else:
        if raw_input("Are you sure you would like to skip your turn? (y/n)").upper() == "Y":
            return True
        else:
            return "Please enter a word."

def calculate_word_score(word, player):
    #Calculates the score of a word
    global LETTER_VALUES, premium_spots
    premium_spots = []
    word = word.upper()
    word_score = 0
    for letter in word:
        for spot in premium_spots:
            if letter == spot[0]:
                if spot[1] == "TLS":
                    word_score += LETTER_VALUES[letter] * 2
                elif spot[2] == "DLS":
                    word_score += LETTER_VALUES[letter]
        word_score += LETTER_VALUES[letter]
    for spot in premium_spots:
        if spot[1] == "TWS":
            word_score *= 3
        elif spot[1] == "DWS":
            word_score *= 2
    player.increase_score(word_score)

def turn(player, board, bag):
    #Begins a turn, by displaying the current board, getting the information to play a turn, and creates a recursive loop to allow the next person to play.
    global round_number, players, skipped_turns
    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):
        print("\nRound " + str(round_number) + ": " + player.get_name() + "'s turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Letter Rack: " + player.get_rack_str())

        #Gets information in order to play a word.
        word_to_play = raw_input("Word to play: ")
        location = []
        col = raw_input("Column number: ")
        row = raw_input("Row number: ")
        if (col == "" or row == ""):
            location = [-1, -1]
        else:
            location = [int(row), int(col)]
        direction = raw_input("Direction of word (right or down): ")

        #If the first word throws an error, creates a recursive loop until the information is given correctly.
        while check_word(word_to_play, location, player, direction, board.board_array()) != True:
            print (check_word(word_to_play, location, player, direction, board.board_array()))
            word_to_play = raw_input("Word to play: ")
            location = []
            col = raw_input("Column number: ")
            row = raw_input("Row number: ")
            if (col == "" or row == ""):
                location = [-1, -1]
            else:
                location = [int(row), int(col)]
            direction = raw_input("Direction of word (right or down): ")

        if word_to_play == "":
            print("Your turn has been skipped.")
            skipped_turns += 1
        else:
        #Plays the correct word and prints the board.
            board.place_word(word_to_play, location, direction, player)
            calculate_word_score(word_to_play, player)
            skipped_turns = 0

        print("\n" + player.get_name() + "'s score is: " + str(player.get_score()))

        if players.index(player) != (len(players)-1):
            player = players[players.index(player)+1]
        else:
            player = players[0]
            round_number += 1
        if bag.get_remaining_tiles() > 0:
            turn(player, board, bag)
    else:
        end_game()

def start_game():
    #Begins the game and calls the turn function.
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag()

    num_of_players = int(raw_input("\nPlease enter the number of players (2-4): "))
    while num_of_players < 2 or num_of_players > 4:
        num_of_players = int(raw_input("This number is invalid. Please enter the number of players (2-4): "))
    print("Welcome to Scrabble! Please enter the names of the players below.")
    players = []
    for i in range(num_of_players):
        players.append(Player(bag))
        players[i].set_name(raw_input("Please enter player " + str(i+1) + "'s name: "))

    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    #Forces the game to end when the bag runs out of tiles.
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    print("The game is over! " + player.get_name() + ", you have won!")

start_game()
