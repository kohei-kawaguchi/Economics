compute_loglikelihood_first_price_w <- function(theta, df_first_w){
  alpha <- theta[1]
  beta <- theta[2]
  ll <- 0
  for (tt in 1:100){
    w <- df_first_w[tt,]$w %>% as.numeric()
    r <- df_first_w[tt,]$r %>% as.numeric()
    n <- df_first_w[tt,]$n %>% as.numeric()
    ll <- ll + log(compute_p_first_w(w, r, alpha, beta, n) / (1 - pbeta(r, alpha, beta)^n))
  }
  logll <- ll / 100
  return (logll)
}