def generate_parentheses(n):
    """
    Fonction pour générer toutes les combinaisons correctes de parenthèses
    :param n: Nombre de paires de parenthèses
    :return: Liste des combinaisons de parenthèses correctes
    """
    result = []

    def backtrack(current, open_count, close_count):
        # Si la combinaison courante est complète, on l'ajoute au résultat
        if len(current) == 2 * n:
            result.append(current)
            return

        # On ajoute une parenthèse ouvrante si le nombre d'ouvrantes est inférieur à n
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # On ajoute une parenthèse fermante si le nombre de fermantes est inférieur aux ouvrantes
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    # Appel initial à la fonction backtrack avec une chaîne vide et aucune parenthèse ajoutée
    backtrack("", 0, 0)
    return result

# Exemple d'utilisation avec 3 paires de parenthèses
n = 3
solutions = generate_parentheses(n)

# Affichage des solutions
for sol in solutions:
    print(sol)
