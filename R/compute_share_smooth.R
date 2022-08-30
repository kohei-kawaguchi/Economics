compute_share_smooth <- function(X, M, V, beta, sigma, mu, omega){
  df_choice_smooth <- compute_choice_smooth(X, M, V, beta, sigma, mu, omega)
  S <- aggregate(q ~ t+j, data = df_choice_smooth, mean)
  df_share_smooth <- dplyr::left_join(M, X, by="j") %>%
    dplyr::left_join(S, by=c("j", "t")) %>% 
    dplyr::rename(s=q) %>%
    dplyr::group_by(t) %>%
    dplyr::mutate(y = log(s/first(s))) %>%
    dplyr::ungroup()
  return(df_share_smooth)
}