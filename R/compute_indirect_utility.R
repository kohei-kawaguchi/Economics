compute_indirect_utility <- function(df, beta, sigma, mu, omega){
  beta_c <- data.frame(matrix(nrow = nrow(df), ncol = K))
  upsilon <- data.frame(df$v_x_1, df$v_x_2, df$v_x_3)
  for (i in 1:K) {
    beta_c[,i] <- beta[i] + sigma[i]*upsilon[,i]
  }
  alpha <- -exp(mu + omega*df$v_p)
  u <- df$xi + alpha*df$p
  XX <- data.frame(df$x_1, df$x_2, df$x_3)
  for (i in 1:K) {
    u <- u + beta_c[,i]*XX[,i]
  }
  return(u)
}