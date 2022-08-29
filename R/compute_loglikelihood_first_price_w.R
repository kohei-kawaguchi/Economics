compute_loglikelihood_first_price_w <- function(theta, df_first_w){
  alpha = theta[1]
  beta = theta[2]
  ll = 0
  for (i in 1:T){
    w <- df_first_w[i,]$w %>% as.numeric()
    r <- df_first_w[i,]$r %>% as.numeric()
    n <- df_first_w[i,]$n %>% as.numeric()
    ll = ll + log(compute_p_first_w(w, r, alpha, beta, n) / (1-pbeta(r, alpha, beta)^n))
  }
  logll = ll/T
  return (logll)
}