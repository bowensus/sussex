import numpy as np
import matplotlib.pyplot as plt

n = 20
pop_size = 100
n_genes = n
half = n // 2
n_generations = 100
mutation_rate = 1/ (50*n_genes)
mutation = True
elitism = True
crossover = True
select_fitness = np.zeros(n_generations)

def generate_relationship_matrix(n):
    matrix = np.random.choice([-1, 1], size=(n, n))
    matrix = np.triu(matrix) + np.triu(matrix, k=1).T
    np.fill_diagonal(matrix, 0)
    return matrix

def generate_group(n, pop_size):
    population = np.zeros((pop_size, n))
    population[:, half:] = 1
    for row in population:
        np.random.shuffle(row)
    return population

def get_index(row):
    population1 = np.where(row == 0)[0]
    population2 = np.where(row == 1)[0]
    return population1, population2

def get_fitness(groups):
    fitness = np.zeros(pop_size)
    for idx, group in enumerate(groups):
        group1, group2 = get_index(group) # get the No. friends in every group
        fitness[idx] += np.sum(relation[group1, :][:, group1])  # 1*1*1 or 1*(-1)*1
        fitness[idx] -= np.sum(relation[group1, :][:, group2])  # (-1)*1*(-1) or (-1)*1*1
        fitness[idx] += np.sum(relation[group2, :][:, group2])  # 1*1*1 or 1*(-1)*1
    return fitness

def choose_by_wheel():
    wheel = np.cumsum(range(pop_size))
    max_wheel = sum(range(pop_size))
    pick_1 = np.random.rand() * max_wheel
    idx_1 = idx_2 = 0
    while pick_1 > wheel[idx_1]:
        idx_1 += 1
    pick_2 = np.random.rand() * max_wheel
    while pick_2 > wheel[idx_2]:
        idx_2 += 1
    return idx_1, idx_2

# create the relationshop and 100 plans
relation = generate_relationship_matrix(n)
groups = generate_group(n, pop_size)
fitness = get_fitness(groups)
ranked_fitness = np.argsort(fitness) # sort fitness
new_fitness = np.zeros(pop_size)
new_groups = generate_group(n, pop_size)

for j in range(n_generations):
    max_idx = ranked_fitness[-1]
    new_groups[0, :] = groups[max_idx, :]
    new_fitness[0] = fitness[max_idx]

    if elitism: start = 1
    else: start = 0
    for i in range(start, pop_size):
        idx_1, idx_2 = choose_by_wheel()
        idx_1 = ranked_fitness[idx_1]
        idx_2 = ranked_fitness[idx_2]
        if crossover:
            parent_1 = groups[idx_1, :half]
            parent_2 = groups[idx_2, half:]
            child = np.hstack((parent_1, parent_2))
        else:
            idx = max(idx_1, idx_2)
            child = groups[idx, :]

        if mutation:
            for idx in range(len(child)):
                if np.random.rand() < mutation_rate:
                    child[idx] = 1 - child[idx]

        new_groups[i, :] = child

    new_fitness = get_fitness(new_groups)
    groups = new_groups
    ranked_fitness = np.argsort(new_fitness)
    select_fitness[j] = new_fitness[ranked_fitness[-1]]

plt.plot(select_fitness)
plt.show()
