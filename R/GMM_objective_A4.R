GMM_objective_A4 <- function(theta_nonlinear, delta, df_share_smooth, 
                             Psi, X, M, V_mcmc, kappa, lamda){
  delta_new <- solve_delta(df_share_smooth, X, M, V_mcmc, delta,
                           theta_nonlinear[3:5], theta_nonlinear[1],
                           theta_nonlinear[2], kappa, lamda)
  theta_linear <- compute_theta_linear(df_share_smooth, delta_new,theta_nonlinear[1],
                                       theta_nonlinear[2], Psi) 
  xi_new <- solve_xi(df_share_smooth, delta_new, theta_linear, 
                     theta_nonlinear[1], theta_nonlinear[2])
  W <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(c(x_1,x_2,x_3,c)) %>% as.matrix()
  objective <- t(xi_new) %*% W %*% solve(Psi) %*% t(W) %*% xi_new
  return(objective)
}