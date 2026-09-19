import random


# Initialize population:
def initialize_population(population_size, number_of_genes):
    population = [
        [random.randint(0, 1) for gene_index in range(number_of_genes)]
        for chromosome_index in range(population_size)
    ]
    return population


# Decode chromosome:
def decode_chromosome(chromosome, number_of_variables, maximum_variable_value):
    m = len(chromosome)
    n = number_of_variables
    k = int(m / n)

    x = []
    for variable in range(n):
        variable_value = 0
        for bit in range(k):
            variable_value += chromosome[variable * k + bit] * pow(2, -bit - 1)
        variable_value = (
            -maximum_variable_value
            + 2 * maximum_variable_value * variable_value / (1 - pow(2, -k))
        )
        x.append(variable_value)

    return x


# Evaluate indviduals:
def evaluate_individual(x):
    x1 = x[0]
    x2 = x[1]
    g = (
        (1.5 - x1 + x1 * x2) ** 2
        + (2.25 - x1 + x1 * x2**2) ** 2
        + (2.625 - x1 + x1 * x2**3) ** 2
    )
    F = 1 / (g + 1)
    return F


# Select individuals:
def tournament_select(fitness_list, tournament_probability, tournament_size):
    population_size = len(fitness_list)
    individuals = []
    for i in range(tournament_size):
        individual_index = random.randint(0, population_size - 1)
        individuals.append(individual_index)

    # Sort individuals indices by fitness scores
    individuals.sort(key=lambda i: fitness_list[i], reverse=True)

    for i in range(tournament_size - 1):
        r = random.random()
        if r < tournament_probability:
            return individuals[i]
    return individuals[-1]


# Carry out crossover:
def cross(chromosome1, chromosome2):

    number_of_genes = len(chromosome1)
    cross_point = random.randint(1, number_of_genes - 1)

    new_chromosome_1 = chromosome1[:cross_point] + chromosome2[cross_point:]
    new_chromosome_2 = chromosome2[:cross_point] + chromosome1[cross_point:]

    return [new_chromosome_1, new_chromosome_2]


# Mutate individuals:
def mutate(chromosome, mutation_probability):

    number_of_genes = len(chromosome)
    mutated_chromosome = chromosome.copy()
    for gene_index in range(number_of_genes):
        r = random.random()
        if r < mutation_probability:
            mutated_chromosome[gene_index] = 1 - chromosome[gene_index]
    return mutated_chromosome


# Genetic algorithm


def run_function_optimization(
    population_size,
    number_of_genes,
    number_of_variables,
    maximum_variable_value,
    tournament_size,
    tournament_probability,
    crossover_probability,
    mutation_probability,
    number_of_generations,
):

    population = initialize_population(population_size, number_of_genes)

    for generation_index in range(number_of_generations):
        maximum_fitness = 0
        best_chromosome = []
        best_individual = []
        fitness_list = []
        for chromosome in population:
            individual = decode_chromosome(
                chromosome, number_of_variables, maximum_variable_value
            )
            fitness = evaluate_individual(individual)
            if fitness > maximum_fitness:
                maximum_fitness = fitness
                best_chromosome = chromosome.copy()
                best_individual = individual.copy()
            fitness_list.append(fitness)

        temp_population = []
        for i in range(0, population_size, 2):
            index_1 = tournament_select(
                fitness_list, tournament_probability, tournament_size
            )
            index_2 = tournament_select(
                fitness_list, tournament_probability, tournament_size
            )
            chromosome1 = population[index_1].copy()
            chromosome2 = population[index_2].copy()
            r = random.random()
            if r < crossover_probability:
                [new_chromosome_1, new_chromosome_2] = cross(chromosome1, chromosome2)
                temp_population.append(new_chromosome_1)
                temp_population.append(new_chromosome_2)
            else:
                temp_population.append(chromosome1)
                temp_population.append(chromosome2)

        for i in range(population_size):
            original_chromosome = temp_population[i]

            mutated_chromosome = mutate(original_chromosome, mutation_probability)
            temp_population[i] = mutated_chromosome

        temp_population[0] = best_chromosome
        population = temp_population.copy()

    return [maximum_fitness, best_individual]
