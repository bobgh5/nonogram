from typing import List


def verify_one_direction(board: List[List[bool]], constrains: List[int], run_over_rows=True) -> bool:
    x = len(board)
    y = len(board[0])
    if not run_over_rows:
        y = len(board)
        x = len(board[0])
    for i in range(x):
        counter = 0
        for j in range(y):
            if run_over_rows:
                is_black = board[i][j]
            else:
                is_black = board[j][i]
            if is_black:
                counter += 1
            else:
                if counter != constrains[i] and counter != 0:
                    return False
        if counter != constrains[i]:
            return False
    return True


def verify_nonogram_board(board: List[List[bool]], rows_constrains: List[int], column_constrains: List[int]) -> bool:
    first_ = verify_one_direction(board, rows_constrains, run_over_rows=True)
    second = verify_one_direction(board, column_constrains, run_over_rows=False)
    return first_ and second


def main():
    board = [[True, True, False, True], [True, True, True, False], [False, False, True, True]]
    ans3 = verify_nonogram_board(board, [3, 3, 2], [2, 2, 2, 2])
    print(ans3)


if __name__ == '__main__':
    main()
