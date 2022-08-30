compute_choice_smooth <- function(X, M, V, beta, sigma, mu, omega){
  # create df
  df <- M %>% 
    dplyr::left_join(X, by="j") %>% 
    dplyr::left_join(V, by="t") %>% 
    dplyr::arrange(t, i, j) 
  u <- compute_indirect_utility(df,beta,sigma,mu,omega) 
  #compute choice
  df_choice_smooth <- df %>% 
    cbind(u) %>% 
    dplyr::group_by(t, i) %>%
    dplyr::mutate(q = exp(u)/sum(exp(u))) %>% 
    dplyr::ungroup() 
  return(df_choice_smooth)
}