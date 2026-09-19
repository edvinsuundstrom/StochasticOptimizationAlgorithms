import math
from genetic_algorithm import run_function_optimization
import matplotlib.pyplot as plt

number_of_runs = 100                # Do NOT change
population_size = 100               # Do NOT change
maximum_variable_value = 5          # Do NOT change: (x_i in [-a,a], where a = maximumVariableValue)
number_of_genes = 50                # Do NOT change
number_of_variables = 2  	    # Do NOT change
tournament_size = 2                 # Do NOT change
tournament_probability = 0.75       # Do NOT change
crossover_probability = 0.8         # Do NOT change
number_of_generations = 2000        # Do NOT change


mutation_probability_list = [0.000, 0.005, 0.010, 0.020, 0.050, 0.100]
median_fitness_list = []

for mutation_probability in mutation_probability_list:
    print("=====================================")
    print(f"mutation probability: {mutation_probability:.3f}")
    fitness_scores = []
    
    for run_index in range(number_of_runs):
        [maximum_fitness, x_best] = run_function_optimization(
            population_size, number_of_genes, number_of_variables, maximum_variable_value, 
            tournament_size, tournament_probability, crossover_probability, 
            mutation_probability, number_of_generations
        )
        output = f"Run index: {run_index}, fitness: {maximum_fitness:.4f}, x = ({x_best[0]:.8f},{x_best[1]:.8f})"
        fitness_scores.append(maximum_fitness)

    fitness_scores.sort()
    
    mid = number_of_runs // 2
    median = (fitness_scores[mid - 1] + fitness_scores[mid]) / 2
    median_fitness_list.append(median)
    print(f"Median fitness score: {median:.6f}")
    print("=====================================")

plt.figure()
plt.plot(mutation_probability_list, median_fitness_list, marker='o')
plt.xlabel("Mutation probability")
plt.ylabel("Median fitness")
plt.title("Median Fitness vs Mutation Probability")
plt.grid(True)
plt.show()

