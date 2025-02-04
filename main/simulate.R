# initialize ------------------------------------------------
rm(list = ls())
devtools::load_all()
library(magrittr)
library(foreach)
library(codetools)
set.seed(1)

# set constant -----------------------------------------------

prefix <- "output/simulate/"
dir.create(
  prefix, 
  showWarnings = FALSE, 
  recursive = TRUE
)

num_simulation <- 100
num_alternative <- 3
num_covariate <- 2
seed <- 10

# simulate ----------------------------------------------------

equilibrium <-
  make_equilibrium(
    num_simulation = num_simulation,
    num_alternative = num_alternative,
    num_covariate = num_covariate
  )

equilibrium <-
  simulate_choice(
    seed = seed,
    equilibrium = equilibrium
  )

saveRDS(
  equilibrium,
  file = 
    paste0(
      prefix, 
      "equilibrium.rds"
    )
)
