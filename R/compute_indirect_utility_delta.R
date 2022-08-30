
compute_indirect_utility_delta <- function(df, delta, sigma, mu, omega){
  df <- left_join(df, delta, by=c("t","j")) 
  u_delta <- df$delta + sigma[1]*df$v_x_1*df$x_1 + sigma[2]*df$v_x_2*df$x_2 +
             sigma[3]*df$v_x_3*df$x_3 - exp(mu+omega*df$v_p)*df$p +
             exp(mu+omega^2/2)*df$p
 
  return(u_delta)
}

