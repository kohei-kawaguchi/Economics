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
  make_equilibrium(
    num_simulation = num_simulation,
    num_alternative = num_alternative,
    num_covariate = num_covariate
  )
equilibrium

is.list(equilibrium)
names(equilibrium) %in% c("covariate", "beta", "choice")
dim(equilibrium$covariate) == c(num_alternative, num_covariate)
dim(equilibrium$beta) == c(num_covariate, 1)
dim(equilibrium$choice) == c(num_simulation, num_alternative)

utility <-
  compute_utility(
    covariate = equilibrium$covariate,
    beta = equilibrium$beta
  )
utility

dim(utility) == c(num_alternative, 1)

utility_rcpp <-
  compute_utility_rcpp(
    covariate = equilibrium$covariate,
    beta = equilibrium$beta
  )
utility_rcpp

all.equal(utility, utility_rcpp)

choice_probability <-
  compute_choice_probability(
    covariate = equilibrium$covariate,
    beta = equilibrium$beta
  )
choice_probability

dim(choice_probability) == c(num_alternative, 1)

equilibrium <-
  simulate_choice(
    seed = seed,
    equilibrium = equilibrium
  )
equilibrium

dim(equilibrium$choice) == c(num_simulation, num_alternative)

equilibrium$choice %>%
  apply(
    MARGIN = 1,
    FUN = function(x) {
      sum(x) == 1
    }
  ) %>%
  all()



