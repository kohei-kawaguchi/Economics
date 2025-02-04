testthat::test_that("make_equilibrium creates correct structure and dimensions", {
  num_simulation <- 100
  num_alternative <- 3
  num_covariate <- 2
  
  equilibrium <-
    make_equilibrium(
      num_simulation = num_simulation,
      num_alternative = num_alternative,
      num_covariate = num_covariate
    )
  
  expect_true(is.list(equilibrium))
  expect_true(all(names(equilibrium) %in% c("covariate", "beta", "choice")))
  
  dims <- purrr::map(equilibrium, dim)
  expect_equal(
    dims$covariate,
    c(num_alternative, num_covariate)
  )
  expect_equal(
    dims$beta,
    c(num_covariate, 1)
  )
  expect_equal(
    dims$choice,
    c(num_simulation, num_alternative)
  )
})

testthat::test_that("compute_utility returns correct dimensions", {
  num_simulation <- 100
  num_alternative <- 3
  num_covariate <- 2
  
  equilibrium <-
    make_equilibrium(
      num_simulation = num_simulation,
      num_alternative = num_alternative,
      num_covariate = num_covariate
    )
  
  utility <-
    compute_utility(
      covariate = equilibrium$covariate,
      beta = equilibrium$beta
    )
  
  expect_equal(
    dim(utility),
    c(num_alternative, 1)
  )
})

testthat::test_that("compute_choice_probability returns correct dimensions", {
  num_simulation <- 100
  num_alternative <- 3
  num_covariate <- 2
  
  equilibrium <-
    make_equilibrium(
      num_simulation = num_simulation,
      num_alternative = num_alternative,
      num_covariate = num_covariate
    )
  
  choice_probability <-
    compute_choice_probability(
      covariate = equilibrium$covariate,
      beta = equilibrium$beta
    )
  
  expect_equal(
    dim(choice_probability),
    c(num_alternative, 1)
  )
})

testthat::test_that("simulate_choice generates valid choices", {
  num_simulation <- 100
  num_alternative <- 3
  num_covariate <- 2
  seed <- 10
  
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
  
  expect_equal(
    dim(equilibrium$choice),
    c(num_simulation, num_alternative)
  )
  
  row_sums <-
    apply(
      equilibrium$choice,
      MARGIN = 1,
      FUN = sum
    )
  expect_true(
    all(row_sums == 1)
  )
}) 