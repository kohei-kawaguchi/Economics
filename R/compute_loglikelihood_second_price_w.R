compute_loglikelihood_second_price_w <- function(theta, df_second_w,T){
  alpha <- theta[1]
  beta <- theta[2]
  ll <- 0
  for (tt in 1:T){
    w <- df_second_w[tt,]$w
    r <- df_second_w[tt,]$r
    m <- df_second_w[tt,]$m
    n <- df_second_w[tt,]$n
    ll <- ll + log(compute_p_second_w(w, r, m, n, alpha, beta) 
                  / (1-compute_m0(r, n, alpha, beta)))
  }
  logll <- ll/100
  return (logll)
}