from constraint import Problem

# 1. Définir le graphe
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (2, 1), (3, 1)]

# 2. Définir le nombre de couleurs disponibles (par exemple, 3 couleurs)
colors = range(3)

# 3. Créer un problème
problem = Problem()

# 4. Ajouter des variables (chaque nœud peut avoir une couleur)
for node in nodes:
    problem.addVariable(node, colors)

# 5. Ajouter des contraintes pour s'assurer que les nœuds adjacents ont des couleurs différentes
for node1, node2 in edges:
    problem.addConstraint(lambda color1, color2: color1 != color2, (node1, node2))

# 6. Résoudre le problème
solution = problem.getSolution()

# 7. Afficher la solution
if solution:
    for node in nodes:
        print(f"Nœud {node} a la couleur {solution[node]}")
else:
    print("Pas de solution trouvée")
