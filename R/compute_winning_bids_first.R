compute_winning_bids_first <- function(valuation, reserve, alpha, beta){
  record <- NULL
  for (tt in 1:100){
    val <- df_first[which(df_first[,1] == tt), "b"]
    t <- tt
    n <- N[tt]
    m <- sum(valuation[which(valuation[,1] == tt), "x"] > 0.2)
    r <- c(0.2)
    w <- max(val)
    record <- rbind(record, c(t, n, m, r, w))
  }
  record <- as_tibble(record)
  colnames(record) <- c("t","n","m","r","w")
  return(record)
}
