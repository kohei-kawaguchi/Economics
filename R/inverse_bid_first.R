inverse_bid_first <- function(b, r, alpha, beta, n){
  uniroot(function(x) (bid_first(x, r, alpha, beta, n) - b),
          lower = r, 
          upper = bid_first(1, r, alpha, beta, n),
          extendInt = "yes")[1]
}