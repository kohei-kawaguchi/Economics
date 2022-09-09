
compute_winning_bids_first <- function(valuation, reserve, alpha, beta){
  dt <- 
    df_first %>% 
    dplyr::select(t,n,m,r,b) %>% 
    dplyr::group_by(t) %>% 
    dplyr::filter(b == max(b))
  
  colnames(dt)[5] <- "w"
  
  return(dt)
}

