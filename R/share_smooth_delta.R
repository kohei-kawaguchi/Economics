compute_share_smooth_delta <- function(X, M, V, delta, sigma, mu, omega){
  df_choice_smooth_delta <- compute_choice_smooth_delta(X, M, V, delta, sigma, mu, omega)
  S <- aggregate(q ~ t+j, data = df_choice_smooth_delta, mean)
  df_share_smooth_delta <- dplyr::left_join(M,X,by="j") %>%
    dplyr::left_join(S,by=c("j","t")) %>% dplyr::rename(s=q) %>%
    dplyr::group_by(t) %>%
    dplyr::mutate(y = log(s/first(s))) %>%
    dplyr::ungroup()
  return(df_share_smooth_delta)
}