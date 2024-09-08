import itertools
import random

# Fonction pour évaluer la tentative par rapport à la combinaison secrète
def evaluate_guess(secret, guess):
    correct_place = sum([1 for i in range(len(secret)) if secret[i] == guess[i]])
    wrong_place = 0
    secret_count = {}
    guess_count = {}
    
    # Compter les occurrences des couleurs pour les mauvaises positions
    for i in range(len(secret)):
        if secret[i] != guess[i]:
            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1
    
    # Calculer le nombre de bonnes couleurs mais mal placées
    for color in guess_count:
        if color in secret_count:
            wrong_place += min(secret_count[color], guess_count[color])
    
    return correct_place, wrong_place

# Fonction principale de l'IA
def mastermind_solver(colors, length, max_attempts=10):
    # Générer toutes les combinaisons possibles
    all_combinations = list(itertools.product(colors, repeat=length))
    
    # Choisir une combinaison secrète aléatoire pour tester l'IA
    secret_combination = random.choice(all_combinations)
    print(f"Combinaison secrète choisie : {secret_combination}")
    
    attempts = 0
    while attempts < max_attempts and all_combinations:
        # L'IA propose une combinaison
        guess = all_combinations[0]
        print(f"Tentative {attempts + 1}: {guess}")
        
        # Évaluer la tentative
        correct_place, wrong_place = evaluate_guess(secret_combination, guess)
        print(f"Résultat : {correct_place} bien placées, {wrong_place} mal placées")
        
        # Si la combinaison est correcte, l'IA a gagné
        if correct_place == length:
            print(f"L'IA a trouvé la solution en {attempts + 1} tentatives : {guess}")
            return
        
        # Filtrer les combinaisons possibles en fonction des indices reçus
        all_combinations = [
            comb for comb in all_combinations 
            if evaluate_guess(comb, guess) == (correct_place, wrong_place)
        ]
        
        attempts += 1
    
    print("L'IA n'a pas pu trouver la solution dans le nombre maximal de tentatives.")

# Paramètres du jeu
colors = ['Rouge', 'Vert', 'Bleu', 'Jaune']
length = 4
mastermind_solver(colors, length)
