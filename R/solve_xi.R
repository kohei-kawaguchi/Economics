solve_xi <- function(df_share_smooth, delta, beta, mu, omega){
  
  df_share_delta <- dplyr::inner_join(df_share_smooth,delta,by = c("t","j")) %>%
    dplyr::filter(j != 0) %>%
    mutate(xi_new = delta - beta[1]*x_1 - beta[2] *x_2 - beta[3]*x_3 
           + exp(mu+omega^2/2)*p)
  return(df_share_delta$xi_new)
}