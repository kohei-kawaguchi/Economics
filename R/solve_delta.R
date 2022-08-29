solve_delta <- 
  function(df_share_smooth, X, M, V, delta, sigma, mu, omega, kappa,lamda){
   distance <- 10
   delta_new <- delta
  while (distance > lamda) {
    delta_old <- delta_new
    df_share_delta <- compute_share_smooth_delta(X,M,V,delta_old,sigma,mu,omega)
    delta_new$delta <- delta_old$delta + kappa*log(df_share_smooth$s) -
                       kappa*log(df_share_delta$s)
    distance <- max(abs(delta_new$delta - delta_old$delta))
   
  }
  return(delta_new)
}