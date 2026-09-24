def checkmate(board):
    rows = board.strip("\n").split("\n")

    if not rows:
        return

    size = len(rows)

    if any(len(row) != size for row in rows):
        return

    kings = []

    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                kings.append((row, col))

    if len(kings) != 1:
        return

    king_row, king_col = kings[0]

#=====================================================================================================================
    pawn_row = king_row + 1

    if pawn_row < size:
        for pawn_col in (king_col - 1, king_col + 1):
            if 0 <= pawn_col < size:
                if rows[pawn_row][pawn_col] == "P":
                    print("Success")
                    return

#=====================================================================================================================
    straight = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in straight:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "PBRQK":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return
                break

            row += dr
            col += dc

#=====================================================================================================================
    diagonal = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in diagonal:
        row = king_row + dr
        col = king_col + dc

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "PBRQK":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return
                break

            row += dr
            col += dc

    print("Fail")