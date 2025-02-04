# initialize ------------------------------------------------
rm(list = ls())
devtools::load_all()
library(magrittr)
library(foreach)
library(codetools)
set.seed(1)

# set constant -----------------------------------------------

num_simulation <- 100
num_alternative <- 3
num_covariate <- 2
seed <- 10

# simulate ----------------------------------------------------

equilibrium <-
  simulate_choice(
    seed = seed,
    equilibrium = equilibrium
  )
equilibrium
