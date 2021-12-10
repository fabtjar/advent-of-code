def get_rows_and_columns(lines):
    rows = []
    for n in range(2, len(lines), 6):
        # Rows.
        board = lines[n:n + 5]
        board = [[int(i) for i in row.split()] for row in board]
        rows += board

        # Add columns.
        rows += [[row[i] for row in board] for i in range(len(board[0]))]
    return rows


def get_winning_row_index(drawn, rows):
    count = [0 for _ in rows]
    wins = []
    for d in drawn:
        for i, row in enumerate(rows):
            if d in row:
                count[i] += 1
                if count[i] == 5:
                    board_index = i // 10
                    if board_index not in wins:
                        wins.append(board_index)
                        if len(wins) * 10 == len(rows):
                            return board_index, d


def get_score(board, drawn, last_drawn):
    drawn_so_far = drawn[:drawn.index(last_drawn) + 1]
    board = [[n for n in row if n not in drawn_so_far] for row in board]
    return sum([sum(row) for row in board]) * last_drawn


def calculate(lines):
    drawn = [int(line) for line in lines[0].split(',')]
    rows = get_rows_and_columns(lines)
    row_index, last_drawn = get_winning_row_index(drawn, rows)
    board = rows[row_index * 10:row_index * 10 + 5]
    return get_score(board, drawn, last_drawn)


with open('input.txt') as f:
    lines = f.read().splitlines()
    print(calculate(lines))
