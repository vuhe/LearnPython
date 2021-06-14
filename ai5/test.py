import matplotlib.pyplot as plt

from ai5 import *

x = [i / 100 for i in range(900)]
y = [0 for i in range(900)]
for i in range(900):
    y[i] = aimFunction(x[i])
plt.plot(x, y)
plt.show()

# initiate population
population = []
for i in range(10):
    entity = ''
    for j in range(17):
        entity = entity + str(np.random.randint(0, 2))
    population.append(entity)

t = []
for i in range(1000):
    # selection
    value = fitness(population, aimFunction)
    population_new = selection(population, value)
    # crossover
    offspring = crossover(population_new, 0.7)
    # mutation
    population = mutation(offspring, 0.02)
    result = []
    for j in range(len(population)):
        result.append(aimFunction(decode(population[j])))
    t.append(max(result))

plt.plot(t)
plt.axhline(max(y), linewidth=1, color='r')
plt.show()
