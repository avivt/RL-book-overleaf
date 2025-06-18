import numpy as np
import matplotlib.pyplot as plt

# 1. Green line: All possible policies as a function of x in [0, 1].
x_vals = np.linspace(0, 1, 200)
V_S1_green = (9*x_vals + 1) / (6 + 4.5*x_vals)
V_S2_green = (11 + 9*x_vals) / (6 + 4.5*x_vals)

# 2. Policy Iteration Steps:
# pi_0 (always A2, i.e., x=0):
pi0_VS1 = 1/6         # ≈0.16667
pi0_VS2 = 11/6        # ≈1.83333

# pi_1 (choose A1, i.e., x=1):
pi1_VS1 = 10/10.5     # ≈0.95238
pi1_VS2 = 20/10.5     # ≈1.90476

# 3. Value Iteration:
def bellman_update(v1, v2):
    """
    Performs one Bellman update for the two states.
    
    For S1, we consider:
      - A1: goes to S2 (reward 0): 0.5*v2.
      - A2: with probability 0.1 goes to S2 and 0.9 stays in S1 (reward 0): 0.5*(0.1*v2 + 0.9*v1).
    For S2, the update is:
      V(S2) = 1 + 0.5*(0.9*v2 + 0.1*v1).
    """
    new_v1 = max(0.5 * v2, 0.5 * (0.1*v2 + 0.9*v1))
    new_v2 = 1 + 0.5 * (0.9*v2 + 0.1*v1)
    return new_v1, new_v2

def greedy_action(v1, v2):
    """
    Computes the greedy action for S1 given current estimates.
    Returns 1 if A1 (which is optimal) is chosen, else returns 0.
    """
    Q_A1 = 0.5 * v2
    Q_A2 = 0.5 * (0.1*v2 + 0.9*v1)
    # Tie-breaker: if equal, choose A1 (the optimal action).
    if Q_A1 >= Q_A2:
        return 1  # A1 chosen: optimal.
    else:
        return 0  # A2 chosen: suboptimal.

# Run value iteration starting from V0 = [0, 0].
v1, v2 = 5.0, -1.0
value_iterates = [(v1, v2)]
colors = []

# Determine color for the initial iterate.
if greedy_action(v1, v2) == 1:
    colors.append('red')
else:
    colors.append('orange')

num_iterations = 6
for i in range(num_iterations):
    v1, v2 = bellman_update(v1, v2)
    value_iterates.append((v1, v2))
    if greedy_action(v1, v2) == 1:
        colors.append('red')
    else:
        colors.append('orange')

value_iterates = np.array(value_iterates)
colors = np.array(colors)

# Create the plot.
plt.figure(figsize=(8,6))
# (i) Green line: The continuum of policies.
plt.plot(V_S1_green, V_S2_green, color='green', label='All policies (parametrized by $x$)')
# (ii) Blue circles: Policy iteration steps.
plt.scatter([pi0_VS1, pi1_VS1], [pi0_VS2, pi1_VS2],
            color='blue', s=100, label='PI iterate')
# (iii) Value iteration iterates: Red if greedy action is optimal, orange otherwise.
red_mask = (colors == 'red')
orange_mask = (colors == 'orange')
plt.scatter(value_iterates[red_mask, 0], value_iterates[red_mask, 1],
            color='red', s=50, label='VI iterate (greedy optimal)')
plt.scatter(value_iterates[orange_mask, 0], value_iterates[orange_mask, 1],
            color='orange', s=50, label='VI iterate (greedy not optimal)')
# (iv) Dotted gray line: Value iteration iterates.
plt.plot(value_iterates[:, 0], value_iterates[:, 1], color='gray', linestyle='dotted')

plt.xlabel("$\mathcal{V}({s}_1)$")
plt.ylabel("$\mathcal{V}({s}_2)$")
plt.title("Policy & Value Iteration in $\mathcal{V}({s}_1)$-$\mathcal{V}({s}_2)$ Space")
plt.legend()
plt.grid(True)
plt.savefig('/Users/aviv/Repositories/scripts/vi_vs_pi.png', dpi=600)
