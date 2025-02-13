from rpm.rpm.core import Equilibrium

# set parameter 

parameter = {
  "theta": 4
}

exogenous = {
  "n": 10
}

# define equilibrium

equilibrium = Equilibrium(
  parameter, 
  exogenous
)

# solve equilibrium

equilibrium.solve_vertically_integrated()

equilibrium.endogenous
equilibrium.surplus


# theta >= 3

equilibrium.solve_wholesale()

equilibrium.endogenous
equilibrium.surplus

equilibrium.solve_maximum_rpm()

equilibrium.endogenous
equilibrium.surplus

equilibrium.solve_minimum_rpm()

equilibrium.endogenous
equilibrium.surplus

# theta < 3

equilibrium.parameter["theta"] = 2

equilibrium.solve_wholesale()

equilibrium.endogenous
equilibrium.surplus

equilibrium.solve_maximum_rpm()

equilibrium.endogenous
equilibrium.surplus

equilibrium.solve_minimum_rpm()

equilibrium.endogenous
equilibrium.surplus

