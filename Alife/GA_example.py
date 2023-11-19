import numpy as np
import matplotlib.pyplot as plt

# setup variables
pop_size = 100
n_genes = 8
n_generations = 100
mutation_rate = 1/n_genes
fitness_over_time = np.zeros(n_generations)
elitism = True

# initial population
population = np.random.choice([0, 1], size=(pop_size, n_genes))
print(population)
target = np.random.choice([0, 1], size=(1, n_genes))

print(population[0, :])
# get initial fitness
fitness = np.zeros(pop_size)

for i in range(pop_size):
    fitness[i] = n_genes - np.sum(np.abs(target - population[i, :]))
print(fitness)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

for i in range(n_generations):
    # create new population
    new_pop = np.zeros((pop_size, n_genes))
    new_fitness = np.zeros(pop_size)

    # sort population by fitness
    ranked_fitness = np.argsort(fitness)

    # roulette wheel
    wheel = np.cumsum(range(pop_size))
    max_wheel = sum(range(pop_size))

    # elitism (add the best individual to new population)
    max_ind = ranked_fitness[-1]
    new_pop[0, :] = population[max_ind, :]
    new_fitness[0] = fitness[max_ind]

    start_point = 1 if elitism else 0
    for j in range(start_point, pop_size):
        # pick first individual
        pick_1 = np.random.rand() * max_wheel
        ind_1 = 1
        while pick_1 > wheel[ind_1]:
            ind_1 += 1

        pick_2 = np.random.rand() * max_wheel
        ind_2 = 1
        while pick_2 > wheel[ind_2]:
            ind_2 += 1

        ind_1 = int(ranked_fitness[ind_1])
        ind_2 = int(ranked_fitness[ind_2])

        # create daughter from crossover
        cross_over_point = np.random.choice(range(n_genes))
        parent_1_genes = population[ind_1, :][0:cross_over_point]
        parent_2_genes = population[ind_2, :][cross_over_point:]
        daughter = np.hstack([parent_1_genes, parent_2_genes])

        # ...
        for k in range(n_genes):
            if np.random.rand() < mutation_rate:
                daughter[k] = 1 - daughter[k]

        new_pop[j, :] = daughter
        new_fitness[j] = n_genes - np.sum(np.abs(target - daughter))

    fitness_over_time[i] = max(new_fitness)
    population = new_pop
    fitness = new_fitness

plt.plot(fitness_over_time)
plt.show()
