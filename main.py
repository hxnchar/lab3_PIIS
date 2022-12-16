import chess
import random


def material_balance(board):
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


def numberOFPieces(board, whoToMove):
    if whoToMove == 1:
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


def evaluationFunction(board, whoToMove):
    numberOfWhites = numberOFPieces(board, 1)
    numberOfBlacks = numberOFPieces(board, -1)
    materialBalance = material_balance(board)
    return materialBalance * (numberOfWhites - numberOfBlacks) * whoToMove
