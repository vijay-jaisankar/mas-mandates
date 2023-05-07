import random 
from fitness import score_against_all_c, score_against_all_d, score_against_mirror
from transformations import get_mutated_single, get_crossover_pair

import matplotlib.pyplot as plt

# Initialisation
N_EPISODES = 20_000
POPULATION_SIZE = 250
GENE_SIZE = 100
K = 25

"""
    Get random strings with 'C' and 'D' for initialising the population 
"""
def get_random_population(population_size = POPULATION_SIZE, gene_size = GENE_SIZE):
    population = []
    for _ in range(population_size):
        res = ''.join(random.choices(['C', 'D'], k = GENE_SIZE))
        population.append(res)
    
    return population

"""
    Run the genetic algorithm over N_EPISODES and get the best performer, and the history of maximum and average scores across episodes.
"""
def run_genetic_algorithm(fitness_function, num_episodes = N_EPISODES, elitism_value = K, population_size = POPULATION_SIZE, gene_size = GENE_SIZE, verbose = True):

    # Initialise the score arrays
    max_scores = []
    avg_scores = []

    # Get initial population
    population = get_random_population(population_size, gene_size)
    for i in range(num_episodes):
        if verbose:
            print(f"Episode {i}")
        
        # Get the top performers
        current_population = population.copy()
        current_population.sort(key = lambda x: fitness_function(x), reverse = True)
        sorted_population = current_population.copy()
        top_k_performers = sorted_population[:elitism_value]

        # Evaulate and store metrics
        top_scores = [fitness_function(x) for x in current_population]
        max_score = max(top_scores)
        average_score = sum(top_scores)/len(top_scores)
        max_scores.append(max_score)
        avg_scores.append(average_score)

        if verbose:
            print(f"Max score: {max_score}, Average score: {average_score}")

        # Shuffle the remaining population
        remaining_population = sorted_population[elitism_value:]
        random.shuffle(remaining_population)
        shuffled_population = remaining_population.copy()

        # Crossover
        new_population = []
        for i in range(1, len(shuffled_population) - 1, 2):
            parent1 = shuffled_population[i]
            parent2 = shuffled_population[i+1]
            child1, child2 = get_crossover_pair(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)
        
        # Edge case: Odd number of elements in the population
        if len(shuffled_population) != len(new_population):
            new_population.append(shuffled_population[-1])

        # Mutation
        mutated_population = [get_mutated_single(x) for x in new_population]

        # Set the population
        population = mutated_population
        population.extend(top_k_performers)

    # Get the best gene sequence    
    population.sort(key = lambda x: fitness_function(x), reverse = True)
    top_performer = population[0]
    return top_performer, max_scores, avg_scores

if __name__ == "__main__":
    # Get the top strategy against "All D"
    top_d_contender, max_scores_all_d, avg_scores_all_d = run_genetic_algorithm(score_against_all_d, verbose=True)
    print(top_d_contender)

    # Get the top strategy against "All C"
    top_c_contender, max_scores_all_c, avg_scores_all_c = run_genetic_algorithm(score_against_all_c, verbose=False)
    print(top_c_contender)

    # Get the top strategy against "Mirror"
    mirror_contender, max_scores_mirror, avg_scores_mirror = run_genetic_algorithm(score_against_mirror, verbose=False)
    print(mirror_contender)
