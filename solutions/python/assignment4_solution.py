from __future__ import annotations

WIN_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def new_board() -> list[str]:
    return ["-" for _ in range(9)]


def render_board(board: list[str]) -> str:
    rows = [" | ".join(board[index:index + 3]) for index in range(0, 9, 3)]
    return "\n".join(rows)


def choose_players(first_symbol: str) -> tuple[str, str]:
    symbol = first_symbol.upper()
    if symbol not in {"X", "O"}:
        raise ValueError("Choose X or O")
    return symbol, "O" if symbol == "X" else "X"


def make_move(board: list[str], position: int, symbol: str) -> bool:
    index = position - 1
    if index < 0 or index >= len(board):
        return False
    if board[index] != "-":
        return False
    board[index] = symbol
    return True


def winner(board: list[str]) -> str | None:
    for first, second, third in WIN_LINES:
        if board[first] != "-" and board[first] == board[second] == board[third]:
            return board[first]
    return None


def is_tie(board: list[str]) -> bool:
    return winner(board) is None and "-" not in board


def switch_player(current_player: str) -> str:
    return "O" if current_player == "X" else "X"


def play_turns(moves: list[int], first_symbol: str = "X") -> dict[str, object]:
    board = new_board()
    current, _ = choose_players(first_symbol)
    for move in moves:
        if make_move(board, move, current):
            won = winner(board)
            if won:
                return {"winner": won, "board": board, "tie": False}
            if is_tie(board):
                return {"winner": None, "board": board, "tie": True}
            current = switch_player(current)
    return {"winner": winner(board), "board": board, "tie": is_tie(board)}


if __name__ == "__main__":
    result = play_turns([1, 4, 2, 5, 3])
    print(render_board(result["board"]))
    print(f"Winner: {result['winner']}")
