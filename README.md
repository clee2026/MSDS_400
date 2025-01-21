# MSDS_400
## Explanation of the Program

This program demonstrates how to use **Linear Programming (LP)** with the PuLP library to optimize maintenance scheduling for three power transformers. The objective is to minimize the total costs associated with maintenance and potential downtime due to failures. Below is an explanation of the program components:

### Objective
The goal is to minimize the total cost, which includes:
- **Maintenance Costs**: Fixed costs for performing maintenance on each transformer.
- **Expected Failure Costs**: Costs incurred if a transformer fails, scaled by the probability of failure in each month.

### Decision Variables
The binary decision variable \( x_{t,m} \) is defined for each transformer \( t \) and month \( m \). It indicates whether maintenance is performed (\( x_{t,m} = 1 \)) or not (\( x_{t,m} = 0 \)).

### Constraints
1. **Maintenance in High-Risk Months**: Each transformer must be maintained at least once during months where the probability of failure exceeds a threshold (in this example, 0.3).
2. **Logical Assignment**: Maintenance can only be performed once per transformer in a given month.

### Hypothetical Failure Probabilities
Failure probabilities are assigned for each transformer across 12 months to simulate realistic scenarios. These probabilities vary to reflect seasonal risks:
- **Transformer_1**: Low risk overall, with slightly elevated probabilities in summer.
- **Transformer_2**: Moderate risk with peaks in mid-year.
- **Transformer_3**: High risk, especially in the summer months.

### Output
The program outputs the **optimal maintenance schedule**. For each transformer, it lists the months in which maintenance should be performed to minimize costs while ensuring reliability.

### Example Output
If the program is run, the output might look like this:

### How It Works
1. **Define Costs**: Maintenance and failure costs are assigned for each transformer.
2. **Set Probabilities**: Monthly failure probabilities are input for each transformer.
3. **Define Objective**: The total cost (maintenance + expected failure costs) is minimized using LP.
4. **Add Constraints**: Logical and practical constraints are added to ensure feasibility.
5. **Solve the Problem**: The PuLP solver determines the optimal schedule.
6. **Print Results**: The program outputs the maintenance schedule for each transformer.

### Technologies Used
- **Python**: Programming language used for implementation.
- **PuLP**: Linear programming library for defining and solving optimization problems.

### Usage
To use this program:
1. Ensure Python and the PuLP library are installed.
2. Copy the code into a `.py` file.
3. Run the file to see the optimized maintenance schedule.

