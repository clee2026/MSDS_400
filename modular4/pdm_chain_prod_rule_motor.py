"""Use Case:
Chain Rule: Used to compute the rate of change of engine efficiency over time, considering temperature and vibration effects.
Product Rule: Applied to compute how engine efficiency changes when multiple variables (like load and wear rate) interact."""

import numpy as np

def engine_efficiency(temp, vibration, load):
    """A sample function to estimate engine efficiency based on temperature, vibration, and load."""
    return np.exp(-0.01 * temp) * np.exp(-0.05 * vibration) * (1 - 0.02 * load)

def partial_derivative_temp(temp, vibration, load):
    """Derivative of engine efficiency w.r.t. temperature (Chain Rule)."""
    return -0.01 * np.exp(-0.01 * temp) * np.exp(-0.05 * vibration) * (1 - 0.02 * load)

def partial_derivative_vibration(temp, vibration, load):
    """Derivative of engine efficiency w.r.t. vibration (Chain Rule)."""
    return -0.05 * np.exp(-0.01 * temp) * np.exp(-0.05 * vibration) * (1 - 0.02 * load)

def product_rule_derivative(load, wear_rate):
    """Derivative using the Product Rule: d(Load * WearRate)/dt = Load' * WearRate + Load * WearRate'"""
    d_load_dt = -0.02  # Assume load decreases over time
    d_wear_rate_dt = 0.03  # Assume wear rate increases over time
    return d_load_dt * wear_rate + load * d_wear_rate_dt

# Simulated time-based data
time_points = np.linspace(0, 10, 5)  # 5 time steps from 0 to 10 hours
temperature_data = [60, 65, 70, 72, 75]  # Degrees Celsius
vibration_data = [2.0, 2.5, 3.0, 3.2, 3.5]  # Vibration intensity
load_data = [50, 48, 46, 45, 44]  # Load percentage
wear_rate_data = [0.1, 0.12, 0.15, 0.18, 0.2]  # Wear rate factor

print("Time (hrs) | Efficiency | dEff/dTemp | dEff/dVib | Product Rule d(Load*Wear)/dt")
print("-" * 80)

for i in range(len(time_points)):
    temp, vib, load, wear = temperature_data[i], vibration_data[i], load_data[i], wear_rate_data[i]
    efficiency = engine_efficiency(temp, vib, load)
    d_eff_temp = partial_derivative_temp(temp, vib, load)
    d_eff_vib = partial_derivative_vibration(temp, vib, load)
    product_rule_result = product_rule_derivative(load, wear)

    print(f"{time_points[i]:<10.1f} | {efficiency:<10.4f} | {d_eff_temp:<10.4f} | {d_eff_vib:<10.4f} | {product_rule_result:<10.4f}")
