make_equilibrium <-
  function(
    num_simulation,
    num_alternative,
    num_covariate
  ) {
    covariate <-
        rnorm(
          n = num_alternative * num_covariate,
        ) %>%
    matrix(
      nrow = num_alternative,
      ncol = num_covariate
    )

    beta <-
      rep(
        1,
        num_covariate
      ) %>%
      as.matrix()

    choice <-
      rep(
        0,
        num_simulation * num_alternative
      ) %>%
      matrix(
        nrow = num_simulation
      )
      

    equilibrium <-
      list(
        covariate = covariate,
        beta = beta,
        choice = choice
      )

    return(equilibrium)
  }


compute_utility <-
  function(
    covariate,
    beta
  ) {
    utility <-
      covariate %*% beta
    return(utility)
  }


compute_choice_probability <-
  function(
    covariate,
    beta
  ) {

    utility <-
      compute_utility(
        covariate = covariate, 
        beta = beta
      )

    choice_probability <-
      exp(utility) / sum(exp(utility))
    return(choice_probability)
  }

simulate_choice <-
  function(
    seed,
    equilibrium
  ) {
    set.seed(seed)
    choice_probability <-
      compute_choice_probability(
        covariate = equilibrium$covariate,
        beta = equilibrium$beta
      )
    equilibrium$choice <-
      rmultinom(
        n = nrow(equilibrium$choice),
        size = 1,
        prob = choice_probability
      ) %>%
      t()
    return(equilibrium)
  }