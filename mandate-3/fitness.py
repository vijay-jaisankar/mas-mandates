"""
    Prisoners' dilemma - scoring functions
"""

# Score matrix represented as (agent, antagonist)
SCORE_MATRIX = {
    ('C', 'C'): (5, 5),
    ('C', 'D'): (0, 10),
    ('D', 'C'): (10, 0),
    ('D', 'D'): (3, 3)
}

"""
    All D antagonist
"""
def score_against_all_d(gene):
    score = 0
    for ch in gene:
        score += SCORE_MATRIX[(ch, 'D')][0]
    return score

"""
    All C antagonist
"""
def score_against_all_c(gene):
    score = 0
    for ch in gene:
        score += SCORE_MATRIX[(ch, 'C')][0]
    return score

"""
    Mirror antagonist
"""
def score_against_mirror(gene):
    score = 0
    for ch in gene:
        score += SCORE_MATRIX[(ch, ch)][0]
    return score