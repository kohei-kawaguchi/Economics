inverse_bid_equation <- function(x, b, r, alpha, beta, n){
  res_bid <-  bid_first(x, r, alpha, beta, n) - b
  return(res_bid)
}