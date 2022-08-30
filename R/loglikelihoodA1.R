loglikelihood_A1 <- function(b){
  l <- 0
  x1 <- 0
  x2 <- 1
  p1 = exp(b*x1)/(exp(b*x1)+exp(b*x2)) #likelihood to choose k=1
  y1 <- df$y[seq(1,2000,by=2)]
  for (i in 1:length(y1)) {
    l = (l + y1[i]*log(p1) + (1-y1[i])*log(1-p1))
    ll = l/length(y1)
  }
  return(ll)
}