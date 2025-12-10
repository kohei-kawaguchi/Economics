import os
import numpy as np
import pickle
from economics.simulate import make_equilibrium, simulate_choice

# Set constants
prefix = "output/simulate/"
os.makedirs(prefix, exist_ok=True)

num_simulation = 100
num_alternative = 3
num_covariate = 2
seed = 10

# Run simulation
np.random.seed(1)  # Set seed similar to R's set.seed(1)

# Create equilibrium structure
equilibrium = make_equilibrium(
    num_simulation=num_simulation,
    num_alternative=num_alternative,
    num_covariate=num_covariate
)

# Simulate choices
equilibrium = simulate_choice(
    seed=seed,
    equilibrium=equilibrium
)

# Save results
with open(os.path.join(prefix, "equilibrium.pkl"), "wb") as f:
    pickle.dump(equilibrium, f)

print(f"Simulation completed and saved to {os.path.join(prefix, 'equilibrium.pkl')}")

