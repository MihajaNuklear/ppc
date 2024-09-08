def rendu_monnaie(V, N):
    # Initialiser un tableau pour stocker le nombre minimum de pièces pour chaque valeur de 0 à N
    min_pieces = [float('inf')] * (N + 1)
    
    # Base: pour rendre 0, on a besoin de 0 pièce
    min_pieces[0] = 0

    # Stocker les pièces utilisées pour rendre chaque montant
    coins_used = [-1] * (N + 1)

    # Parcourir chaque valeur jusqu'à N pour trouver la solution optimale
    for i in range(1, N + 1):
        for coin in V:
            if coin <= i:
                if min_pieces[i - coin] + 1 < min_pieces[i]:
                    min_pieces[i] = min_pieces[i - coin] + 1
                    coins_used[i] = coin

    # Si on ne peut pas rendre la monnaie, retourner None
    if min_pieces[N] == float('inf'):
        return None

    # Reconstituer la combinaison des pièces utilisées
    result = []
    value = N
    while value > 0:
        result.append(coins_used[value])
        value -= coins_used[value]

    return result

# Exemple 1: V = {1, 2, 5}, N = 13
V = [1, 2, 5]
N = 13
solution = rendu_monnaie(V, N)
if solution:
    print(f"Pour rendre {N} unités monétaires, la solution optimale est: {solution}")
    print(f"Nombre total de pièces : {len(solution)}")
else:
    print(f"Impossible de rendre {N} avec les pièces disponibles.")

# Exemple 2: V = {1, 3, 4}, N = 6
V = [1, 3, 4]
N = 6
solution = rendu_monnaie(V, N)
if solution:
    print(f"Pour rendre {N} unités monétaires, la solution optimale est: {solution}")
    print(f"Nombre total de pièces : {len(solution)}")
else:
    print(f"Impossible de rendre {N} avec les pièces disponibles.")
