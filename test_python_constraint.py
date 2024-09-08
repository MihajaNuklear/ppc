from constraint import Problem
# Problème : Résoudre un puzzle simple

# Créer un problème
problem = Problem()

# Ajouter des variables x, y, z comprises entre 1 et 10
problem.addVariable('x', range(1, 11))
problem.addVariable('y', range(1, 11))
problem.addVariable('z', range(1, 11))

# Ajouter les contraintes :
# Somme des variables (x + y + z = 15)
problem.addConstraint(lambda x, y, z: x + y + z == 15, ['x', 'y', 'z'])
# x doit être plus petit que z (x < z)
problem.addConstraint(lambda x, z: x < z, ['x', 'z'])

# Trouver toutes les solutions
solutions = problem.getSolutions()

# Afficher les solutions
for solution in solutions:
    print(f"x = {solution['x']}, y = {solution['y']}, z = {solution['z']}")
