import random

# -----------------------------
# 스도쿠 보드 초기화
# -----------------------------
def initialize_board():
    return [[0 for _ in range(9)] for _ in range(9)]

# -----------------------------
# 스도쿠 보드 출력
# -----------------------------
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()

# -----------------------------
# 유효성 검사
# -----------------------------
def is_valid(board, row, col, num):
    # 행 검사
    if num in board[row]:
        return False
    # 열 검사
    for i in range(9):
        if board[i][col] == num:
            return False
    # 3x3 박스 검사
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# -----------------------------
# 스도쿠 풀이 알고리즘 (백트래킹)
# -----------------------------
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# -----------------------------
# 퍼즐 생성
# -----------------------------
def generate_sudoku():
    board = initialize_board()
    solve_sudoku(board)
    # 무작위로 40칸 비움
    for _ in range(40):
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

# -----------------------------
# 게임 플레이
# -----------------------------
def play_sudoku():
    board = generate_sudoku()
    print("스도쿠 게임을 시작합니다!\n")
    print_board(board)

    while True:
        try:
            row = int(input("행(0-8): "))
            col = int(input("열(0-8): "))
            num = int(input("숫자(1-9): "))

            if board[row][col] == 0:
                if is_valid(board, row, col, num):
                    board[row][col] = num
                else:
                    print("잘못된 숫자입니다.")
                print_board(board)
            else:
                print("이미 숫자가 있는 칸입니다!")

            # 완성 여부 확인
            temp = [r[:] for r in board]
            if solve_sudoku(temp):
                if all(all(cell != 0 for cell in r) for r in board):
                    print("🎉 스도쿠를 완성했습니다! 🎉")
                    break

        except ValueError:
            print("숫자를 입력하세요!")
        except IndexError:
            print("행과 열은 0~8 사이여야 합니다.")

# -----------------------------
# 실행
# -----------------------------
if __name__ == "__main__":
    play_sudoku()
