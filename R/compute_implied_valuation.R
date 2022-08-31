compute_implied_valuation <- function(b, n, r, F_b, f_b){
  if(b < r){
    x <- 0
  }else{
    x <- b + H_b(0.4, n, F_b) / h_b(0.4, n, F_b, f_b)
  }
  return(x)
}