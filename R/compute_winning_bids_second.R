
compute_winning_bids_second <- function(valuation, reserve){
  record <- NULL
  for (i in 1:T){
    val <- valuation[which(valuation[,1] == i),"x"]
    t <- i
    n <- N[i]
    m <- sum(valuation[which(valuation[,1] == i),"x"]>0.2)
    r <- 0.2
    w <- max(max(val[val != max(val)]),0.2)
    record <- rbind(record,c(t,n,m,r,w))
  }
  record <- as_tibble(record)
  colnames(record) <- c("t","n","m","r","w")
  return(record)
}
