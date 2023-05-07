"""
    Prisoners' dilemma - mutations and crossovers
"""
import random

# Mutation and crossover probabilities
P_MUTATION = 0.25
P_CROSSOVER = 0.75

"""
    Randomly mutate a gene string
"""
def get_mutated_single(gene):
    new_gene = list(gene)
    trial_value = random.random()
    length = len(gene)


    if trial_value <= P_MUTATION:
        random_index = random.randint(0, length - 1)
        if new_gene[random_index] == 'C':
            new_gene[random_index] = 'D'
        else:
            new_gene[random_index] = 'C'

    return ''.join(new_gene)

"""
    Randomly crossover two gene strings
"""
def get_crossover_pair(gene1, gene2):
    c1 = gene1
    c2 = gene2

    trial_value = random.random()
    length = len(c1)

    if trial_value <= P_CROSSOVER:
        random_index = random.randint(1, length - 2)
        c1 = gene1[:random_index] + gene2[random_index:]
        c2 = gene2[:random_index] + gene1[random_index:]
    
    return [''.join(c1), ''.join(c2)]