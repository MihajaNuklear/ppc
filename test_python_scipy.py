from scipy.optimize import minimize
#Problème : Optimisation d'une fonction quadratique

# Définir la fonction à minimiser
def objective_function(x):
    return x**2 + 3*x + 2

# Initialiser une valeur initiale pour x (par exemple x = 0)
x0 = 0

# Lancer l'optimisation
result = minimize(objective_function, x0)

# Afficher le résultat
print(f"Solution optimale pour x: {result.x}")
print(f"Valeur minimale de la fonction: {result.fun}")
