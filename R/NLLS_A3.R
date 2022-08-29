NLLS_objective_A3 <- function(theta, df_share, X, M, V_mcmc, e_mcmc){
  df_mcmc <- compute_share(X, M, V_mcmc, e_mcmc, theta[1:3], 
                           theta[4:6], theta[7], theta[8])
  MSE <- mean((df_mcmc$s-df_share$s)^2)
  return(MSE)
}