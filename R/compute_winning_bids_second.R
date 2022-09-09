
compute_winning_bids_second <- function(valuation, reserve, T){
  record <- NULL
  for (tt in 1:T){
    val <-
      valuation %>%
      dplyr::filter(t == tt) %>%
      dplyr::select(x)
    t <- tt
    n <- N[tt]
    m <- sum(val > 0.2)
    r <- 0.2
    w <- max(max(val[val != max(val)]),0.2)
    record <- rbind(record,c(t,n,m,r,w))
  }
  record <- as_tibble(record)
  colnames(record) <- c("t","n","m","r","w")
  return(record)
}


