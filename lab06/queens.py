import copy


def main():
    chess_board = read_chess_board_from_file("input.txt", "r")
    queen_positions = get_queen_positions(chess_board)
    print("current heuristic: ", end='')
    print(calculate_heuristic(queen_positions))

    heuristic_board = calculate_heuristic_board(queen_positions)
    reverse_board(heuristic_board)
    for column in heuristic_board:
        print(column)

    write_chess_board_to_file(heuristic_board)


def write_chess_board_to_file(heuristic_board):
    f = open("output.txt", "w")
    for row in heuristic_board:
        for item in row:
            f.write(str(item) + ' ')
        f.write('\n')


def read_chess_board_from_file(file_name, mode):
    chess_board = []
    f = open(file_name, mode)
    for line in f:
        row = []
        for it in line.strip().split(' '):
            row.append(it)
        chess_board.append(row)
    return chess_board


def get_queen_positions(chess_board):
    queen_positions = []
    for y in range(0, 8):
        for x in range(0, 8):
            if chess_board[y][x] == 'Q':
                queen_positions.append((x, y))
    return queen_positions


def reverse_board(board):
    for y in range(0, 8):
        for x in range(0, 8):
            board[x][y] = board[y][x]


def calculate_heuristic_board(queen_positions):
    heuristic_board = []
    for queen_position in queen_positions:
        heuristic_board.insert(queen_position[0], calculate_heuristic_column_of_queen(queen_position, queen_positions))
    return heuristic_board


def calculate_heuristic_column_of_queen(current_queen_pos, queen_positions):
    new_queen_positions = copy.deepcopy(queen_positions)
    new_queen_positions.remove(current_queen_pos)
    x, y = current_queen_pos

    heuristic_column = []
    basic_heuristic = calculate_heuristic(new_queen_positions)

    for i in range(0, 8):
        heuristic_column.append(basic_heuristic + get_checks_of_queen((x, i), new_queen_positions))

    return heuristic_column


def calculate_heuristic(queen_positions):
    heuristic = 0
    for queen_position in queen_positions:
        heuristic = heuristic + get_checks_of_queen(queen_position, queen_positions)
    return heuristic / 2


def get_checks_of_queen(current_queen_pos, all_queen_pos):
    checks = 0
    for queen_pos in all_queen_pos:
        if queen_pos == current_queen_pos:
            continue
        elif is_check(current_queen_pos, queen_pos):
            checks = checks + 1
    return checks


def is_check(queen_pos_a, queen_pos_b):
    return is_check_on_y(queen_pos_a, queen_pos_b) \
           or is_check_on_x(queen_pos_a, queen_pos_b) \
           or is_check_on_diagonal(queen_pos_a, queen_pos_b)


def is_check_on_y(queen_pos_a, queen_pos_b):
    return queen_pos_a[1] == queen_pos_b[1]


def is_check_on_x(queen_pos_a, queen_pos_b):
    return queen_pos_a[0] == queen_pos_b[0]


def is_check_on_diagonal(queen_pos_a, queen_pos_b):
    return abs(queen_pos_a[0] - queen_pos_b[0]) == abs(queen_pos_a[1] - queen_pos_b[1])


if __name__ == '__main__':
    main()
