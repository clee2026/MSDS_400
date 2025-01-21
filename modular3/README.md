# Maintenance Scheduling Problem

This repository provides a Python script to solve a maintenance scheduling problem using linear programming. The goal is to minimize total costs while ensuring that transformers are maintained at least once during high-risk months.

## Overview

The problem involves:

- Three transformers with specific failure probabilities for each month.
- Maintenance costs and failure costs associated with each transformer.
- Decision variables indicating whether maintenance is performed in a given month.
- A constraint ensuring that each transformer is maintained at least once during high-risk months.

## Code Structure

The script:

1. Defines the problem as a linear programming model using PuLP.
2. Sets up decision variables for scheduling maintenance for each transformer.
3. Defines the objective function to minimize total costs (maintenance + expected failure costs).
4. Includes constraints to ensure compliance with the maintenance policy.
5. Solves the problem and prints the optimal schedule.

## Dependencies

To run the script, you need the following Python package:

- [PuLP](https://pypi.org/project/PuLP/): A Python library for linear programming.

You can install PuLP using pip:

```bash
pip install pulp
```

## Usage

To use the script, follow these steps:

1. Clone the repository or copy the script to your local environment.
2. Run the script using Python:

```bash
python pdm_lp.py
```

3. View the optimal maintenance schedule printed in the console.

## Example Output

The script outputs an optimal maintenance schedule. For example:

```
Optimal Maintenance Schedule:
Transformer_1:
  Maintenance scheduled in month 6
Transformer_2:
  Maintenance scheduled in month 7
Transformer_3:
  Maintenance scheduled in month 8
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve the script or add new features.
