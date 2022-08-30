compute_choice <- function(X, M, V, e, beta, sigma, mu, omega){
  # join df
  df <- M %>% 
    dplyr::left_join(X, by="j") %>% 
    dplyr::left_join(V, by="t") %>% 
    dplyr::arrange(t,i,j) 
  u <- compute_indirect_utility(df, beta, sigma, mu, omega) #compute utility
  # compute choice
  df_choice <- df %>% 
    cbind(e,u) %>% 
    dplyr::group_by(t, i) %>%
    dplyr::mutate(q = as.integer(u+e == max(u+e))) %>% 
    dplyr::ungroup() 
  return(df_choice)
}