def simulate_population_growth(initial_pop,growth_rate,generation):
    for generation in range (generation):
        population=initial_pop
        
        population =initial_pop*generation**growth_rate
        if population < 108:
            exit
        print(f"Generation {generation + 1}: Population = {population:.2f}")



pop =simulate_population_growth(100, 1.05, 10)
print(pop)
              
