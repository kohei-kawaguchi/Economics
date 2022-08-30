compute_theta_linear <- function(df_share_smooth, delta, mu, omega, Psi){
  XX <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(c(x_1, x_2, x_3))  %>%
    as.matrix()
  W <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(c(x_1, x_2, x_3, c)) %>%
    as.matrix()
  alpha <- -exp(mu+omega^2/2)
  delta_v <- dplyr::filter(delta, j != 0) %>% 
    select(delta) %>% as.matrix()
  p <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(p) %>% 
    as.matrix()
  theta_linear <- solve(t(XX) %*% W %*% solve(Psi) %*% t(W) %*% XX) %*%
    t(XX) %*% W %*% solve(Psi) %*% t(W) %*% (delta_v - alpha*p)
  return(theta_linear)
}