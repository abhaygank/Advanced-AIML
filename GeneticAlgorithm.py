import random

# --- Parameters ---
POP_SIZE = 6        # number of individuals
GENES = 5           # bits per individual (for 0-31)
GENERATIONS = 20
MUTATION_RATE = 0.1

# --- Fitness Function ---
def fitness(x):
    return x ** 2  # maximizing x^2

# --- Convert binary to integer ---
def decode(binary):
    return int(binary, 2)

# --- Initialize Population ---
def init_population():
    return [''.join(random.choice('01') for _ in range(GENES)) for _ in range(POP_SIZE)]

# --- Selection (Roulette Wheel) ---
def select(pop, fitnesses):
    total_fit = sum(fitnesses)
    pick = random.uniform(0, total_fit)
    current = 0
    for individual, fit in zip(pop, fitnesses):
        current += fit
        if current > pick:
            return individual

# --- Crossover ---
def crossover(parent1, parent2):
    if random.random() < 0.8:  # crossover probability
        point = random.randint(1, GENES - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2

# --- Mutation ---
def mutate(individual):
    return ''.join(
        bit if random.random() > MUTATION_RATE else random.choice('01')
        for bit in individual
    )

# --- Main Genetic Algorithm ---
def genetic_algorithm():
    population = init_population()

    for gen in range(GENERATIONS):
        decoded = [decode(ind) for ind in population]
        fitnesses = [fitness(x) for x in decoded]

        print(f"Generation {gen+1}: Best = {max(decoded)} ({max(fitnesses)})")

        # New population
        new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population += [mutate(child1), mutate(child2)]

        population = new_population[:POP_SIZE]

    # Final best solution
    decoded = [decode(ind) for ind in population]
    fitnesses = [fitness(x) for x in decoded]
    best_x = decoded[fitnesses.index(max(fitnesses))]
    print("\n✅ Best solution found:")
    print(f"x = {best_x}, f(x) = {fitness(best_x)}")

# --- Run ---
if __name__ == "__main__":
    genetic_algorithm()