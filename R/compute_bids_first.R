compute_bids_first<- function(valuation, reserve, alpha, beta){

  dt <- 
    valuation %>% 
    dplyr::left_join(df_second_w) %>% 
    dplyr::select(-w) 
  
  b_col <-  NULL
  for (tt in 1:nrow(dt)){
    x <- dt[tt, ]$x
    r <- dt[tt, ]$r
    n <- dt[tt, ]$n
    b_val <- bid_first(x, r, alpha, beta, n)
    b_col <- rbind(b_col, b_val)
  }
  
  dff <- 
    dt %>% 
    dplyr::mutate(b = b_col[,1])
  
  return(dff)
}


