import board
from heat import Heuristics
import pieces


class AI:

    INFINITE = 10000000

    @staticmethod
    def get_ai_move(chessboard, invalid_moves):
        best_move = 0
        best_score = AI.INFINITE

        for move in chessboard.get_possible_moves(pieces.Piece.BLACK):
            if (AI.is_invalid_move(move, invalid_moves)):
                continue

            copy = board.Board.clone(chessboard)
            copy.perform_move(move)

            score = AI.alphabeta(copy, 2, -AI.INFINITE, AI.INFINITE, True)

            if (score < best_score):
                best_score = score
                best_move = move

        # Checkmate.
        if (best_move == 0):
            return 0

        copy = board.Board.clone(chessboard)
        copy.perform_move(best_move)

        if (copy.is_checkmate(pieces.Piece.BLACK)):
            invalid_moves.append(best_move)
            return AI.get_ai_move(chessboard, invalid_moves)

        return best_move

    @staticmethod
    def is_invalid_move(move, invalid_moves):
        for invalid_move in invalid_moves:
            if (invalid_move.equals(move)):
                return True

        return False

    @staticmethod
    def minimax(board, depth, maximizing):
        if (depth == 0):
            return Heuristics.evaluate(board)

        if (maximizing):
            best_score = -AI.INFINITE

            for move in board.get_possible_moves(pieces.Piece.WHITE):
                copy = board.Board.clone(board)
                copy.perform_move(move)

                score = AI.minimax(copy, depth-1, False)
                best_score = max(best_score, score)

            return best_score
        else:
            best_score = AI.INFINITE

            for move in board.get_possible_moves(pieces.Piece.BLACK):
                copy = board.Board.clone(board)
                copy.perform_move(move)

                score = AI.minimax(copy, depth-1, True)
                best_score = min(best_score, score)

            return best_score

    @staticmethod
    def alphabeta(chessboard, depth, a, b, maximizing):
        if (depth == 0):
            return Heuristics.evaluate(chessboard)

        if (maximizing):
            best_score = -AI.INFINITE

            for move in chessboard.get_possible_moves(pieces.Piece.WHITE):
                copy = board.Board.clone(chessboard)
                copy.perform_move(move)

                best_score = max(best_score, AI.alphabeta(
                    copy, depth-1, a, b, False))
                a = max(a, best_score)
                if (b <= a):
                    break

            return best_score
        else:
            best_score = AI.INFINITE

            for move in chessboard.get_possible_moves(pieces.Piece.BLACK):
                copy = board.Board.clone(chessboard)
                copy.perform_move(move)

                best_score = min(best_score, AI.alphabeta(
                    copy, depth-1, a, b, True))

                b = min(b, best_score)

                if (b <= a):
                    break

            return best_score


x = 1

chesspieces = [
    [pieces.Rook.BLACK, 0],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]
