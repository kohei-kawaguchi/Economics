compute_p_second_w <- function(w, r, m, n, alpha, beta){
  if (m > 1){
    pp = n*(n-1)*(pbeta(w,alpha, beta)^(n-2))*(1-pbeta(w,alpha, beta))*dbeta(w,alpha, beta) 
  }else if (m == 1){
    pp = n*(pbeta(r,alpha, beta)^(n-1))*(1-pbeta(r,alpha, beta))
  }
  return(pp)
}