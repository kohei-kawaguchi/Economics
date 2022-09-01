solve_xi <- function(df_share_smooth, delta, beta, mu, omega){
  
  df_share_delta <- dplyr::inner_join(df_share_smooth,delta,by = c("t","j")) %>%
    dplyr::filter(j != 0) %>%
    mutate(xi_new = delta - beta[1]*x_1 - beta[2] *x_2 - beta[3]*x_3 
           + exp(mu+omega^2/2)*p)
  return(df_share_delta$xi_new)
}

compute_theta_linear <- function(df_share_smooth, delta, mu, omega, Psi){
  XX <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(c(x_1, x_2, x_3))  %>%
    as.matrix()
  W <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(c(x_1, x_2, x_3, c)) %>%
    as.matrix()
  alpha <- -exp(mu+omega^2/2)
  delta_v <- dplyr::filter(delta, j != 0) %>% 
    select(delta) %>% as.matrix()
  p <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(p) %>% 
    as.matrix()
  theta_linear <- solve(t(XX) %*% W %*% solve(Psi) %*% t(W) %*% XX) %*%
    t(XX) %*% W %*% solve(Psi) %*% t(W) %*% (delta_v - alpha*p)
  return(theta_linear)
}

GMM_objective_A4 <- function(theta_nonlinear, delta, df_share_smooth, 
                             Psi, X, M, V_mcmc, kappa, lamda){
  delta_new <- solve_delta(df_share_smooth, X, M, V_mcmc, delta,
                           theta_nonlinear[3:5], theta_nonlinear[1],
                           theta_nonlinear[2], kappa, lamda)
  theta_linear <- compute_theta_linear(df_share_smooth, delta_new,theta_nonlinear[1],
                                       theta_nonlinear[2], Psi) 
  xi_new <- solve_xi(df_share_smooth, delta_new, theta_linear, 
                     theta_nonlinear[1], theta_nonlinear[2])
  W <- dplyr::filter(df_share_smooth, j != 0) %>%
    dplyr::select(c(x_1,x_2,x_3,c)) %>% 
    as.matrix()
  objective <- t(xi_new) %*% W %*% solve(Psi) %*% t(W) %*% xi_new
  return(objective)
}

solve_delta <- 
  function(df_share_smooth, X, M, V, delta, sigma, mu, omega, kappa,lamda){
    distance <- 10
    delta_new <- delta
    while (distance > lamda) {
      delta_old <- delta_new
      df_share_delta <- compute_share_smooth_delta(X,M,V,delta_old,sigma,mu,omega)
      delta_new$delta <- delta_old$delta + kappa*log(df_share_smooth$s) -
        kappa*log(df_share_delta$s)
      distance <- max(abs(delta_new$delta - delta_old$delta))
      
    }
    return(delta_new)
  }

NLLS_objective_A3 <- function(theta, df_share, X, M, V_mcmc, e_mcmc){
  df_mcmc <- compute_share(X, M, V_mcmc, e_mcmc, theta[1:3], 
                           theta[4:6], theta[7], theta[8])
  MSE <- mean((df_mcmc$s-df_share$s)^2)
  return(MSE)
}


compute_indirect_utility <- function(df, beta, sigma, mu, omega){
  beta_c <- data.frame(matrix(nrow = nrow(df), ncol = K))
  upsilon <- data.frame(df$v_x_1, df$v_x_2, df$v_x_3)
  for (i in 1:K) {
    beta_c[,i] <- beta[i] + sigma[i]*upsilon[,i]
  }
  alpha <- -exp(mu + omega*df$v_p)
  u <- df$xi + alpha*df$p
  XX <- data.frame(df$x_1, df$x_2, df$x_3)
  for (i in 1:K) {
    u <- u + beta_c[,i]*XX[,i]
  }
  return(u)
}

compute_indirect_utility_delta <- function(df, delta, sigma, mu, omega){
  df <- left_join(df, delta, by=c("t","j")) 
  u_delta <- df$delta + sigma[1]*df$v_x_1*df$x_1 + sigma[2]*df$v_x_2*df$x_2 +
    sigma[3]*df$v_x_3*df$x_3 - exp(mu+omega*df$v_p)*df$p +
    exp(mu+omega^2/2)*df$p
  
  return(u_delta)
}


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

compute_choice_smooth_delta <- function(X, M, V, delta, sigma, mu, omega){
  df <- M %>% 
    dplyr::left_join(X, by="j") %>% 
    dplyr::left_join(V, by="t") %>%
    dplyr::arrange(t, i, j) 
  u <- compute_indirect_utility_delta(df, delta, sigma, mu, omega)
  df_choice_smooth <- df %>% 
    cbind(u) %>% 
    dplyr::group_by(t, i) %>%
    dplyr::mutate(q = exp(u)/sum(exp(u))) %>% 
    dplyr::ungroup() 
  return(df_choice_smooth)
}

compute_share <- function(X, M, V, e, beta, sigma, mu, omega){
  df_choice <- compute_choice(X, M, V, e, beta, sigma, mu, omega)
  S <- aggregate(q ~ t+j, data = df_choice, mean)
  df_share <- dplyr::left_join(M,X,by="j") %>%
    dplyr::left_join(S,by=c("j","t")) %>%
    dplyr::rename(s=q) %>%
    dplyr::group_by(t) %>%
    dplyr::mutate(y = log(s/first(s))) %>%
    dplyr::ungroup()
  return(df_share)
}

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

compute_share_smooth_delta <- function(X, M, V, delta, sigma, mu, omega){
  df_choice_smooth_delta <- compute_choice_smooth_delta(X, M, V, delta, sigma, mu, omega)
  S <- aggregate(q ~ t+j, data = df_choice_smooth_delta, mean)
  df_share_smooth_delta <- dplyr::left_join(M,X,by="j") %>%
    dplyr::left_join(S, by=c("j", "t")) %>% 
    dplyr::rename(s=q) %>%
    dplyr::group_by(t) %>%
    dplyr::mutate(y = log(s/first(s))) %>%
    dplyr::ungroup()
  return(df_share_smooth_delta)
}

loglikelihood_A1 <- function(b){
  l <- 0
  x1 <- 0
  x2 <- 1
  p1 = exp(b*x1)/(exp(b*x1)+exp(b*x2)) #likelihood to choose k=1
  y1 <- df$y[seq(1,2000,by=2)]
  for (i in 1:length(y1)) {
    l = (l + y1[i]*log(p1) + (1-y1[i])*log(1-p1))
    ll = l/length(y1)
  }
  return(ll)
}
