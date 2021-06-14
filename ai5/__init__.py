import math

import numpy as np


def aimFunction(x):
    y = x + 5 * math.sin(5 * x) + 2 * math.cos(3 * x)
    return y


def decode(x):
    y = 0 + int(x, 2) / (2 ** 17 - 1) * 9
    return y


def fitness(population, aim_function):
    value = []
    for i in range(len(population)):
        value.append(aim_function(decode(population[i])))
        # weed out negative value
        if value[i] < 0:
            value[i] = 0
    return value


def selection(population, value):
    # 轮盘赌选择
    fitness_sum = []
    for i in range(len(value)):
        if i == 0:
            fitness_sum.append(value[i])
        else:
            fitness_sum.append(fitness_sum[i - 1] + value[i])

    for i in range(len(fitness_sum)):
        fitness_sum[i] /= sum(value)

    # select new population
    population_new = []
    for i in range(len(value)):
        rand = np.random.uniform(0, 1)
        for j in range(len(value)):
            if j == 0:
                if 0 < rand <= fitness_sum[j]:
                    population_new.append(population[j])

            else:
                if fitness_sum[j - 1] < rand <= fitness_sum[j]:
                    population_new.append(population[j])
    return population_new


def crossover(population_new, pc):
    half = int(len(population_new) / 2)
    father = population_new[:half]
    mother = population_new[half:]
    np.random.shuffle(father)
    np.random.shuffle(mother)
    offspring = []
    for i in range(half):
        if np.random.uniform(0, 1) <= pc:
            co_pint = np.random.randint(0, int(len(father[i]) / 2))
            son = father[i][:co_pint] + (mother[i][co_pint:])
            daughter = mother[i][:co_pint] + (father[i][co_pint:])
        else:
            son = father[i]
            daughter = mother[i]
        offspring.append(son)
        offspring.append(daughter)
    return offspring


def mutation(offspring, pm):
    for i in range(len(offspring)):
        if np.random.uniform(0, 1) <= pm:
            position = np.random.randint(0, len(offspring[i]))
            # 'str' object does not support item assignment,cannot use = to change value
            if position != 0:
                if offspring[i][position] == '1':
                    offspring[i] = offspring[i][:position - 1] + '0' + offspring[i][position:]
                else:
                    offspring[i] = offspring[i][:position - 1] + '1' + offspring[i][position:]
            else:
                if offspring[i][position] == '1':
                    offspring[i] = '0' + offspring[i][1:]
                else:
                    offspring[i] = '1' + offspring[i][1:]
    return offspring
