compute_bids_first<- function(valuation, reserve, alpha, beta){
  record <- NULL
  for (tt in 1:nrow(valuation)){
    t <- valuation[tt, "t"] %>% as.numeric()
    i <- valuation[tt, "i"] %>% as.numeric()
    x <- valuation[tt, "x"] %>% as.numeric()
    r <- 0.2
    n <- N[t]
    m <- sum(valuation[which(valuation[,1] == t),"x"]>0.2)
    b <- bid_first(x, r, alpha, beta, n)
    record <- rbind(record,c(t,i,x,r,n,m,b))

  }
  record <- as_tibble(record)
  colnames(record) <- c("t","i","x","r","n","m","b")
  return(record)
}


