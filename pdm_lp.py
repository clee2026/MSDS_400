from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Define the problem
problem = LpProblem("Maintenance_Scheduling", LpMinimize)

# Define variables for three transformers and 12 months
transformers = ["Transformer_1", "Transformer_2", "Transformer_3"]
months = range(1, 13)
failure_costs = {t: 5000 for t in transformers}  # Cost of failure per transformer
maintenance_costs = {t: 800 for t in transformers}  # Cost of maintenance per transformer

# Hypothetical failure probabilities (lower overall probabilities)
failure_probs = {
    "Transformer_1": [0.05, 0.1, 0.1, 0.15, 0.2, 0.25, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05],
    "Transformer_2": [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.35, 0.3, 0.2, 0.15, 0.1],
    "Transformer_3": [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.45, 0.4, 0.3, 0.25, 0.2],
}

# Decision variables: 1 if maintenance is performed in a given month, 0 otherwise
x = {(t, m): LpVariable(f"x_{t}_{m}", 0, 1, cat="Binary") for t in transformers for m in months}

# Objective: Minimize total costs (maintenance + expected failure costs)
problem += lpSum(
    maintenance_costs[t] * x[t, m] + failure_costs[t] * (1 - x[t, m]) * failure_probs[t][m - 1]
    for t in transformers for m in months
)

# Constraints: Each transformer must be maintained at least once in high-risk months (failure_prob > 0.3)
for t in transformers:
    problem += lpSum(x[t, m] for m in months if failure_probs[t][m - 1] > 0.3) >= 1

# Solve the problem
problem.solve()

# Print the schedule
print("Optimal Maintenance Schedule:")
for t in transformers:
    print(f"{t}:")
    for m in months:
        if x[t, m].varValue > 0.5:
            print(f"  Maintenance scheduled in month {m}")
