import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def logistic_growth(t, K, r, t0, lag_factor, exp_factor):
    return K / (1 + np.exp(-r * (t - t0) * exp_factor)) * (1 - np.exp(-r * t * lag_factor))

def generate_growth_curve(num_points=100, K=1.0, r=0.5, t0=10, 
                          lag_range=(0.5, 2.0), exp_range=(0.5, 2.0), 
                          noise_level=0.02):
    t = np.linspace(0, 50, num_points)
    
    # Randomize lag and exponential phase lengths
    lag_factor = np.random.uniform(*lag_range)
    exp_factor = np.random.uniform(*exp_range)
    
    # Generate the base curve
    y = logistic_growth(t, K, r, t0, lag_factor, exp_factor)
    
    # Add some noise
    noise = np.random.normal(0, noise_level, num_points)
    y += noise
    
    # Ensure non-negative values
    y = np.maximum(y, 0)
    
    return t, y

def generate_growth_curves_df(num_curves=100, num_points=100):
    df = pd.DataFrame()
    
    for i in range(num_curves):
        t, y = generate_growth_curve(num_points)
        df[f'Curve_{i+1}'] = y
    
    df['Time'] = t
    return df

# Generate the DataFrame with 100 growth curves
df = generate_growth_curves_df(num_curves=100)

# Plot a few random curves for visualization
plt.figure(figsize=(12, 6))
for _ in range(5):
    curve = np.random.choice(df.columns[:-1])
    plt.plot(df['Time'], df[curve], label=curve)

plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Sample Logistic Growth Curves')
plt.legend()
plt.grid(True)
plt.show()

# Display basic statistics of the generated curves
print(df.describe())

# Save the DataFrame to a CSV file
df.to_csv('logistic_growth_curves.csv', index=False)
print("DataFrame saved to 'logistic_growth_curves.csv'")