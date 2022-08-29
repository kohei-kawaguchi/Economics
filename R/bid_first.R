bid_first <- function(x, r, alpha, beta, n){
  int_dist = integrate(function(q) pbeta(q, alpha, beta)^(n-1), r, x)$value
  beta_x = x - int_dist/pbeta(x, alpha, beta)^(n-1)
  if(x < r) beta_x = 0
  return(beta_x)
}