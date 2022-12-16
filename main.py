import chess
import random


def material_balance(board: chess.Board()):
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
        3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
        3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
        5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
        9 * (chess.popcount(white & board.queens) -
             chess.popcount(black & board.queens))
    )


def numberOFPieces(board: chess.Board(), turnToMove: int):
    if turnToMove == 1:
        chosen = board.occupied_co[chess.WHITE]
    else:
        chosen = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(chosen & board.pawns) +
        (chess.popcount(chosen & board.knights)) +
        (chess.popcount(chosen & board.bishops)) +
        (chess.popcount(chosen & board.rooks)) +
        (chess.popcount(chosen & board.queens))
    )


def evaluationFunction(board: chess.Board(), turnToMove: int):
    numberOfWhite = numberOFPieces(board, 1)
    numberOfBlack = numberOFPieces(board, -1)
    materialBalance = material_balance(board)
    return materialBalance * (numberOfWhite - numberOfBlack) * turnToMove


def negaMax(board: chess.Board(), depth: int, turnToMove: int) -> tuple:
    if depth == 0:
        return evaluationFunction(board, turnToMove), None
    maxScore = -999
    bestMove = ''
    for legalMove in board.legal_moves:
        score = -(negaMax(board, depth - 1, -turnToMove)[0])
        if score == 0:
            score = random.random()
        if score > maxScore:
            maxScore = score
            bestMove = legalMove
    return maxScore, bestMove


board = chess.Board()
depth, turnToMove = 5, -1

while not board.is_checkmate():
    print("Game state:\n")
    print(board)
    move = input("Input your move: ")
    board.push_san(move)
    negaMove = negaMax(board, depth, turnToMove)[1]
    board.push(negaMove)


# len(board.pieces(1, chess.BLACK))
#  board.is_legal()
# board.push_san("g1h3")
