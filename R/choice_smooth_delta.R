compute_choice_smooth_delta <- function(X, M, V, delta, sigma, mu, omega){
  df <- M %>% dplyr::left_join(X,by="j") %>% 
    dplyr::left_join(V,by="t") %>% dplyr::arrange(t,i,j) # create df
  u <- compute_indirect_utility_delta(df,delta,sigma,mu,omega) #compute utility
  df_choice_smooth <- df %>% cbind(u) %>% dplyr::group_by(t,i) %>%
    dplyr::mutate(q = exp(u)/sum(exp(u))) %>% 
    dplyr::ungroup() #compute choice
  return(df_choice_smooth)
}
