compute_loglikelihood_second_price_w <- function(theta, df_second_w){
  alpha = theta[1]
  beta = theta[2]
  ll = 0
  for (i in 1:T){
    w <- df_second_w[i,]$w
    r <- df_second_w[i,]$r
    m <- df_second_w[i,]$m
    n <- df_second_w[i,]$n
    ll = ll + log(compute_p_second_w(w, r, m, n, alpha, beta) 
                  / (1-compute_m0(r, n, alpha, beta)))
  }
  logll = ll/T
  return (logll)
}