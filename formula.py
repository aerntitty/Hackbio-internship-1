import math

def logistic_growth(time, P0, K, r, lag_phase, exp_phase):
    population = []
    for t in time:
        if t < lag_phase:
            population.append(P0)
        else:
            P_t = K / (1 + ((K - P0) / P0) * math.exp(-r * (t - lag_phase)))
            population.append(P_t)
    return population

test_time = list(range(0, 100, 1))
test_population = logistic_growth(test_time, 1, 100, 0.2, 5, 15)
print("Test logistic_growth function:")
print(test_population[:10])  

# Generate 100 different growth curves
data = []
time = list(range(0, 100, 1))
for i in range(100):
    import random
    P0 = random.uniform(0.1, 10)  # Random initial population
    K = random.uniform(50, 100)   # Random carrying capacity
    r = random.uniform(0.1, 0.5)  # Random growth rate
    lag_phase = random.randint(5, 15)  # Random lag phase
    exp_phase = random.randint(20, 40)  # Random exponential phase
    growth = logistic_growth(time, P0, K, r, lag_phase, exp_phase)
    for t, population in zip(time, growth):
        data.append((i, t, population))

import pandas as pd
df = pd.DataFrame(data, columns=["Curve_ID", "Time", "Population"])
print("First few rows of the data frame:")
print(df.head(20))






def time_to_80_percent_max(time, population, K):
    threshold = 0.8 * K
    for i, pop in enumerate(population):
        if pop >= threshold:
            return time[i]
    return None
# Call the time_to_80_percent_max function to ensure it works
test_time_to_80 = time_to_80_percent_max(test_time, test_population, 100)
print("time_to_80_percent_max function:")
print(f"{test_time_to_80}s to reach 80% of max population")

