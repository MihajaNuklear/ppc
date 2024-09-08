from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD
# Optimisation de la Production pour Maximiser les Profits en Éliminant la Sortie Détailée du Solveur CBC dans PuLP

# 1. Création du problème d'optimisation (maximisation des profits)
problem = LpProblem("Maximiser_Profit", LpMaximize)

# 2. Définition des variables
produit_A = LpVariable("Produit_A", lowBound=10, cat='Integer')  # Doit produire au moins 10 unités
produit_B = LpVariable("Produit_B", lowBound=5, cat='Integer')   # Doit produire au moins 5 unités

# 3. Définition de la fonction objectif (maximiser les profits)
problem += 40 * produit_A + 30 * produit_B, "Profit_Total"

# 4. Ajout des contraintes de production
problem += 2 * produit_A + 1 * produit_B <= 100, "Heures_de_Travail_Disponibles"

# 5. Résolution du problème sans affichage des logs du solveur
problem.solve(PULP_CBC_CMD(msg=False))

# 6. Affichage des résultats
print(f"Quantité de Produit A à produire : {produit_A.varValue}")
print(f"Quantité de Produit B à produire : {produit_B.varValue}")
print(f"Profit total : {problem.objective.value()}")



