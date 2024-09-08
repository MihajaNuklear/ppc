def is_safe(board, row, col, n):
    # Vérifier la colonne
    for i in range(row):
        if board[i] == col:
            return False

    # Vérifier la diagonale ascendante
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Vérifier la diagonale descendante
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False

    return True

def solve_n_queens(n):
    def backtrack(board, row):
        if row == n:
            # Si toutes les reines sont placées, ajouter la solution
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col  # Placer la reine
                backtrack(board, row + 1)  # Passer à la rangée suivante
                # Retour en arrière (backtrack)

    solutions = []
    board = [-1] * n  # Initialiser un échiquier vide
    backtrack(board, 0)
    return solutions

# Exemple d'utilisation pour 4 reines
solutions = solve_n_queens(4)

# Affichage des solutions
for sol in solutions:
    print(sol)
