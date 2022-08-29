compute_m0 <- function(r, n, alpha, beta){
  pp = pbeta(r, alpha, beta)^n
  return (pp)
}