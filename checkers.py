white = "@"
black = "#"

# Initial board setup
board = [
    ["", black, "", black, "", black, "", black],
    [black, "", black, "", black, "", black, ""],
    ["", black, "", black, "", black, "", black],
    [""] * 8,
    [""] * 8,
    ["", "", "", "", "", "", "", ""],
    ["", white, "", white, "", white, "", white],
    [white, "", white, "", white, "", white, ""]
]

# Function to print the board
def print_board():
    print("   a  b  c  d  e  f  g  h")
    for i in range(8):
        row = " " + str(i + 1) + " "
        for j in range(8):
            if board[i][j] == "":
                row += "[ ]"
            else:
                row += "[" + board[i][j] + "]"
        print(row)

# Function to update piece position
def move_piece(piece_coords):
    piece_row = int(piece_coords[1]) - 1
    piece_col = ord(piece_coords[0]) - ord('A')
    destination_coords = input("Enter destination coordinates (A1-H8):\n").upper()
    dest_row = int(destination_coords[1]) - 1
    dest_col = ord(destination_coords[0]) - ord('A')
    board[dest_row][dest_col] = board[piece_row][piece_col]
    board[piece_row][piece_col] = ""
    print_board()

# Print initial board
print_board()

# Get user input for piece coordinates
piece_coords = input("Enter piece coordinates (A1-H8):\n").upper()

# Move piece
move_piece(piece_coords)