compute_share <- function(X, M, V, e, beta, sigma, mu, omega){
  df_choice <- compute_choice(X, M, V, e, beta, sigma, mu, omega)
  S <- aggregate(q ~ t+j, data = df_choice, mean)
  df_share <- dplyr::left_join(M,X,by="j") %>%
              dplyr::left_join(S,by=c("j","t")) %>% dplyr::rename(s=q) %>%
              dplyr::group_by(t) %>%
              dplyr::mutate(y = log(s/first(s))) %>%
              dplyr::ungroup()
  return(df_share)
}