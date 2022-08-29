compute_p_first_w <- function(w, r, alpha, beta, n){
  if(w >= bid_first(1, r, alpha, beta, n) ){
    ht = 10^(-6)
  }
  else{
    inverse = inverse_bid_first(w, r, alpha, beta, n)$root
    ht = n*(pbeta(inverse, alpha, beta)^n) / ((n-1)*(inverse - w))
  }
  return(ht)
}